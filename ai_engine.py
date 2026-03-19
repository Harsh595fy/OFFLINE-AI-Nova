import os
import requests
from typing import List, Dict

# ================= CONFIG =================
# Replace with your actual OpenRouter Key
OPENROUTER_API_KEY = "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"
BASE_URL = "https://openrouter.ai/api/v1"
MODEL_FILENAME = "mistral-7b-instruct-v0.2.Q4_K_M.gguf"

# Language mapping for system prompts
LANGUAGE_PROMPTS = {
    "english": "You are Professor Nova, an intelligent AI assistant.",
    "spanish": "Eres el profesor Nova, un asistente de IA inteligente. Responde en español.",
    "french": "Vous êtes le professeur Nova, un assistant IA intelligent. Répondez en français.",
    "german": "Sie sind Professor Nova, ein intelligenter KI-Assistent. Antworten Sie auf Deutsch.",
    "hindi": "आप प्रोफेसर नोवा हैं, एक बुद्धिमान एआई सहायक। हिंदी में जवाब दें।",
    "chinese": "你是Nova教授，一个智能AI助手。请用中文回答。",
    "japanese": "あなたは教授Novaです。インテリジェントなAIアシスタントです。日本語で答えてください。",
    "arabic": "أنت الأستاذ نوفا، مساعد ذكاء اصطناعي ذكي. أجب باللغة العربية."
}

# ================= OFFLINE SETUP =================
try:
    from llama_cpp import Llama
    LLAMA_AVAILABLE = True
except ImportError:
    LLAMA_AVAILABLE = False
    print("⚠️  'llama-cpp-python' not found. Offline mode will be disabled.")

class AIService:
    def __init__(self):
        self.local_llm = None
        self.offline_ready = False

        # Path to models folder
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.model_path = os.path.join(base_dir, "models", MODEL_FILENAME)

        print("\n--- AI SYSTEM INITIALIZING ---")
        if LLAMA_AVAILABLE:
            self._load_local_model()

    def _load_local_model(self):
        if not os.path.exists(self.model_path):
            print(f"❌ Model file not found at: {self.model_path}")
            print("   (Online mode will still work)")
            return

        try:
            print("🧠 Loading Local Model (This may take a moment)...")
            self.local_llm = Llama(
                model_path=self.model_path,
                n_ctx=2048,
                n_threads=os.cpu_count(),
                verbose=False
            )
            self.offline_ready = True
            print("✅ Offline AI READY")
        except Exception as e:
            print(f"❌ Failed to load local model: {e}")

    def chat(self, messages: List[Dict], force_offline=False):
        # 1. Try Online first (unless forced offline)
        if not force_offline and OPENROUTER_API_KEY and "sk-or" in OPENROUTER_API_KEY:
            online_response = self._online_chat(messages)
            if online_response:
                return online_response

        # 2. Fallback to Offline
        if self.offline_ready:
            print("⚡ Using Offline Model")
            return self._offline_chat(messages)

        return "Error: AI Service Unavailable. Check internet connection or model file."

    def _online_chat(self, messages):
        try:
            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:5000",
            }
            payload = {
                "model": "mistralai/mistral-7b-instruct",
                "messages": messages,
                "max_tokens": 1000
            }
            r = requests.post(
                f"{BASE_URL}/chat/completions",
                headers=headers,
                json=payload,
                timeout=10
            )
            if r.status_code == 200:
                return r.json()["choices"][0]["message"]["content"]
            else:
                print(f"🌐 API Error: {r.status_code} - {r.text}")
        except Exception as e:
            print(f"🌐 Connection failed: {e}")
        return None

    def _offline_chat(self, messages):
        # Format prompt for Mistral/Llama
        system_msg = next((m["content"] for m in messages if m["role"] == "system"), "You are a helpful assistant.")
        user_msg = next((m["content"] for m in messages if m["role"] == "user"), "")
        
        prompt = f"<s>[INST] {system_msg}\n\n{user_msg} [/INST]"

        try:
            output = self.local_llm(
                prompt,
                max_tokens=800,
                stop=["</s>", "[/INST]"],
                echo=False
            )
            return output["choices"][0]["text"].strip()
        except Exception as e:
            return f"❌ Offline processing error: {e}"

# Initialize Engine
ai_engine = AIService()

def get_ai_response(message, subject="General", use_local=False, language="english"):
    # Get base system prompt
    base_prompt = LANGUAGE_PROMPTS.get(language.lower(), LANGUAGE_PROMPTS["english"])
    
    # Add subject specialization
    if subject != "General":
        if language == "english":
            system_prompt = f"{base_prompt} Specialized in {subject}. Keep answers clear and concise."
        elif language == "spanish":
            system_prompt = f"{base_prompt} Especializado en {subject}. Mantén las respuestas claras y concisas."
        elif language == "french":
            system_prompt = f"{base_prompt} Spécialisé en {subject}. Gardez les réponses claires et concises."
        elif language == "hindi":
            system_prompt = f"{base_prompt} {subject} में विशेषज्ञ। उत्तर स्पष्ट और संक्षिप्त रखें।"
        elif language == "chinese":
            system_prompt = f"{base_prompt} 专注于{subject}。保持回答清晰简洁。"
        else:
            system_prompt = f"{base_prompt} Specialized in {subject}. Keep answers clear and concise."
    else:
        system_prompt = base_prompt
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": message}
    ]
    return ai_engine.chat(messages, force_offline=use_local)
