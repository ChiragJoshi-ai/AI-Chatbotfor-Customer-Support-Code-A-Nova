"""
chatbot.py
NLP engine for the customer support chatbot.
- TF-IDF based intent matching
- Context-aware follow-up handling
- Conversation memory (last 3 turns)
"""

import re
import random
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Knowledge import KNOWLEDGE_BASE


# ── Text Preprocessing ────────────────────────────────────────────────────────

def preprocess(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


# ── Intent Classifier ─────────────────────────────────────────────────────────

class IntentClassifier:
    def __init__(self, knowledge_base: dict):
        self.kb = knowledge_base
        self.intents = []
        self.all_patterns = []
        self.pattern_to_intent = []

        for intent, data in knowledge_base.items():
            if intent == "fallback":
                continue
            for pattern in data["patterns"]:
                self.all_patterns.append(preprocess(pattern))
                self.pattern_to_intent.append(intent)
                self.intents.append(intent)

        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), analyzer="word")
        self.tfidf_matrix = self.vectorizer.fit_transform(self.all_patterns)

    def predict(self, user_input: str, threshold: float = 0.25):
        cleaned = preprocess(user_input)
        try:
            vec = self.vectorizer.transform([cleaned])
        except Exception:
            return "fallback", 0.0

        similarities = cosine_similarity(vec, self.tfidf_matrix).flatten()
        best_idx = int(np.argmax(similarities))
        best_score = float(similarities[best_idx])

        if best_score < threshold:
            return "fallback", best_score

        return self.pattern_to_intent[best_idx], best_score


# ── Context Manager ───────────────────────────────────────────────────────────

class ContextManager:
    def __init__(self, max_turns: int = 3):
        self.history = []       # list of (user_msg, bot_response, intent)
        self.max_turns = max_turns
        self.last_intent = None

    def update(self, user_msg: str, bot_response: str, intent: str):
        self.last_intent = intent
        self.history.append({
            "user": user_msg,
            "bot": bot_response,
            "intent": intent
        })
        if len(self.history) > self.max_turns:
            self.history.pop(0)

    def get_context(self):
        return self.history

    def is_followup(self, user_input: str) -> bool:
        """Detect if the user is asking a follow-up without a clear new intent."""
        followup_triggers = [
            "more", "tell me more", "elaborate", "explain",
            "what else", "anything else", "and", "also", "furthermore",
            "can you explain", "more details", "how"
        ]
        cleaned = preprocess(user_input)
        return any(t in cleaned for t in followup_triggers) and len(cleaned.split()) <= 5

    def reset(self):
        self.history = []
        self.last_intent = None


# ── Main Chatbot ──────────────────────────────────────────────────────────────

class CustomerSupportBot:
    def __init__(self):
        self.classifier = IntentClassifier(KNOWLEDGE_BASE)
        self.context = ContextManager()
        self.kb = KNOWLEDGE_BASE

    def get_response(self, user_input: str) -> dict:
        if not user_input.strip():
            return {"response": "Please type something so I can help you!", "intent": None, "confidence": 0}

        # Check for follow-up using context
        if self.context.is_followup(user_input) and self.context.last_intent:
            intent = self.context.last_intent
            confidence = 0.9
        else:
            intent, confidence = self.classifier.predict(user_input)

        responses = self.kb.get(intent, self.kb["fallback"])["responses"]
        response = random.choice(responses)

        self.context.update(user_input, response, intent)

        return {
            "response": response,
            "intent": intent,
            "confidence": round(confidence * 100, 1)
        }

    def reset_context(self):
        self.context.reset()


# ── CLI mode ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    bot = CustomerSupportBot()
    print("\n🤖 Customer Support Bot — type 'quit' to exit\n")
    print("-" * 50)

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Bot: Goodbye! Have a great day! 👋")
            break
        if not user_input:
            continue

        result = bot.get_response(user_input)
        print(f"Bot: {result['response']}")
        print(f"     [intent: {result['intent']} | confidence: {result['confidence']}%]\n")