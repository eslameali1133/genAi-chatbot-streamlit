"""Localization module — all UI strings for supported languages."""

TRANSLATIONS = {
    "en": {
        "title": "💬 Generative AI Chatbot",
        "subtitle": "Powered by Groq + LangChain",
        "input_placeholder": "Ask AI...",
        "system_prompt": "You are a helpful assistant. Always answer in English.",
        "settings": "⚙️ Settings",
        "language": "Language",
        "model": "Model",
        "temperature": "Creativity (temperature)",
        "clear_chat": "🗑️ Clear chat",
        "export_chat": "⬇️ Export chat",
        "export_pdf": "📄 Export as PDF",
        "thinking": "Thinking...",
        "messages_count": "Messages",
        "welcome": "👋 Hi! Ask me anything in English or Arabic.",
        "export_pdf": "📄 Export as PDF",
    },
    "ar": {
        "title": "💬 روبوت المحادثة بالذكاء الاصطناعي",
        "subtitle": "مدعوم بواسطة Groq و LangChain",
        "input_placeholder": "اسأل الذكاء الاصطناعي...",
        "system_prompt": "أنت مساعد ذكي ومفيد. أجب دائماً باللغة العربية الفصحى.",
        "settings": "⚙️ الإعدادات",
        "language": "اللغة",
        "model": "النموذج",
        "temperature": "درجة الإبداع",
        "clear_chat": "🗑️ مسح المحادثة",
        "export_chat": "⬇️ تصدير المحادثة",
        "export_pdf": "📄 تصدير كملف PDF",
        "thinking": "جارٍ التفكير...",
        "messages_count": "عدد الرسائل",
        "welcome": "👋 أهلاً! اسألني أي شيء بالعربية أو الإنجليزية.",
        "export_pdf": "📄 تصدير كملف PDF",
    },
}


def get_translations(lang: str) -> dict:
    base = TRANSLATIONS["en"]
    selected = TRANSLATIONS.get(lang, base)
    # fall back to English, then to the key itself
    return {**{k: k for k in base}, **base, **selected}