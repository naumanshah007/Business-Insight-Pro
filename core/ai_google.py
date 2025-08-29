# core/ai_google.py
import os
import time
import random
import requests
from typing import Optional, List

try:
    import streamlit as st
except Exception:
    st = None

# ---------------- Google Gemini SDK ----------------
try:
    from google import genai
    from google.genai import types
except Exception:
    genai = None
    types = None

# ---------------- Defaults ----------------
DEFAULT_MODEL_NAME = "gemini-2.5-pro"  # can be overridden via secrets: MODEL_NAME
KEY_NAMES = ["OMNI_AI_API_KEY", "GEMINI_API_KEY", "GOOGLE_API_KEY", "ONNI_AI_API_KEY"]

DEFAULT_SYSTEM_CONTEXT = """
You are OmniInsights, a business analytics copilot for SMBs.
Respond with this exact structure and brevity:

## Key Observations
- Core numbers and deltas (MoM / YoY) in bold (e.g., **$12,340**, **−18% MoM**).

## Possible Causes (ranked)
- 3–5 bullets, most likely first. Call out incomplete data if suspected.

## Recommended Actions (do now)
- 3 short, concrete steps with checkmarks (✅). No disclaimers.

Constraints:
- ≤ 250 words. Use Markdown bullets and brief headings.
""".strip()

# ---------------- Secret & Env helpers ----------------
def _get_secret(name: str, default: str = "") -> str:
    """Safely read from Streamlit secrets, then env vars."""
    try:
        if st is not None and hasattr(st, "secrets"):
            if name in st.secrets and str(st.secrets[name]).strip():
                return str(st.secrets[name]).strip()
            v = st.secrets.get(name, None)
            if isinstance(v, str) and v.strip():
                return v.strip()
    except Exception:
        pass
    v = os.environ.get(name, default)
    return v.strip() if isinstance(v, str) else default

def _truncate(md: str, max_chars: int = 3500) -> str:
    if not isinstance(md, str):
        return ""
    return md.strip()[:max_chars]

# ---------------- Provider selection ----------------
AI_PROVIDER = (_get_secret("AI_PROVIDER") or "HF").upper()
MODEL_NAME = _get_secret("MODEL_NAME") or DEFAULT_MODEL_NAME

# ---------------- Google (Gemini) helpers ----------------
def _get_api_key() -> Optional[str]:
    for k in KEY_NAMES:
        v = _get_secret(k)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return None

def _google_is_ready() -> bool:
    return bool(_get_api_key()) and (genai is not None) and (types is not None)

def ask_ai_google(prompt: str, system_context: str = "", max_context_chars: int = 3500) -> str:
    """No-thinking (fast) Gemini call with streaming aggregation."""
    api_key = _get_api_key()
    if not api_key:
        return ("AI is not configured. Set OMNI_AI_API_KEY in .streamlit/secrets.toml "
                "or as an environment variable. (Also accepted: GEMINI_API_KEY / GOOGLE_API_KEY)")
    if genai is None or types is None:
        return "AI SDK is not installed. Run: pip install google-genai"

    try:
        client = genai.Client(api_key=api_key)

        combined = DEFAULT_SYSTEM_CONTEXT
        if system_context:
            combined = f"{combined}\n\n{_truncate(system_context, max_context_chars)}"

        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=f"{combined}\n\n{prompt or ''}")]
            ),
        ]
        # ⚡ Fastest config: no thinking_config
        cfg = types.GenerateContentConfig()

        chunks: List[str] = []
        for chunk in client.models.generate_content_stream(
            model=MODEL_NAME, contents=contents, config=cfg
        ):
            if getattr(chunk, "text", None):
                chunks.append(chunk.text)
        return ("".join(chunks).strip()) or "No response received."
    except Exception as e:
        return f"AI error: {e}"

# ---------------- Hugging Face (free tier) ----------------
def _hf_token() -> str:
    return _get_secret("HF_TOKEN")

def _hf_model() -> str:
    return _get_secret("HF_MODELID")

def _hf_is_ready() -> bool:
    return bool(_hf_token()) and bool(_hf_model())

def _hf_compose_prompt(prompt: str, system_context: str) -> str:
    header = DEFAULT_SYSTEM_CONTEXT
    if system_context:
        header = f"{header}\n\n{system_context.strip()[:3000]}"
    return f"{header}\n\n{prompt or ''}"

def _hf_generate(payload: dict, retries: int = 2, backoff_base: float = 1.4) -> dict:
    token = _hf_token()
    model = _hf_model()
    if not token or not model:
        return {"error": "HF token/model not set."}

    url = f"https://api-inference.huggingface.co/models/{model}"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}

    last_err = None
    for attempt in range(retries + 1):
        try:
            r = requests.post(url, headers=headers, json=payload, timeout=60)
            if r.status_code == 200:
                return r.json()
            # Transient (queue/ratelimit): 429/503 (and some edges like 524)
            if r.status_code in (429, 503, 524):
                last_err = {"status": r.status_code, "text": r.text[:200]}
                time.sleep((backoff_base ** attempt) + random.random())
                continue
            return {"error": f"HF error {r.status_code}: {r.text[:300]}"}
        except Exception as e:
            last_err = {"exception": str(e)}
            time.sleep((backoff_base ** attempt) + random.random())
    return {"error": f"HF request failed after retries: {last_err}"}

def ask_ai_hf(prompt: str, system_context: str = "", max_context_chars: int = 2500, max_new_tokens: int = 320) -> str:
    """Hugging Face Inference API (no-thinking)."""
    if not _hf_is_ready():
        return "Hugging Face is not configured. Set HF_TOKEN and HF_MODELID in secrets."

    text = _hf_compose_prompt(prompt, _truncate(system_context, max_context_chars))
    payload = {
        "inputs": text,
        "parameters": {
            "max_new_tokens": max_new_tokens,
            "temperature": 0.2,
            "top_p": 0.9,
            "repetition_penalty": 1.05,
            "return_full_text": False
        }
    }
    data = _hf_generate(payload)
    if "error" in data:
        return f"AI error (HF): {data['error']}"

    # Typical HF text-gen response: [{"generated_text": "..."}]
    try:
        if isinstance(data, list) and data and "generated_text" in data[0]:
            return data[0]["generated_text"].strip() or "No response received."
        if isinstance(data, dict) and "generated_text" in data:
            return str(data["generated_text"]).strip() or "No response received."
        return f"AI error (HF): Unexpected response shape: {str(data)[:240]}"
    except Exception as e:
        return f"AI error (HF parse): {e}"

# ---------------- Public API ----------------
def is_configured() -> bool:
    """Router-aware readiness check used by the UI."""
    if AI_PROVIDER == "HF":
        return _hf_is_ready()
    return _google_is_ready()

def ask_ai(prompt: str, system_context: str = "", max_context_chars: int = 3500) -> str:
    """Router entrypoint used by the app."""
    if AI_PROVIDER == "HF" and _hf_is_ready():
        return ask_ai_hf(prompt, system_context, max_context_chars=max_context_chars)
    return ask_ai_google(prompt, system_context, max_context_chars=max_context_chars)
