import re
import datetime as _dt
from typing import List, Tuple

class RuleBasedChatbot:
    """A small extensible rule-based chatbot using regex patterns."""

    _RULES: List[Tuple[re.Pattern, str]] = [
        (re.compile(r"\b(hi|hello|hey|hola)\b", re.I), "Hello! How can I assist you today?"),
        (re.compile(r"\b(bye|goodbye|see you|exit)\b", re.I), "Goodbye! Have a productive day!"),
        (re.compile(r"\btime\b", re.I), lambda: f"The current time is {_dt.datetime.now().strftime('%H:%M:%S')}."),
        (re.compile(r"\bdate\b", re.I), lambda: f"Today's date is {_dt.datetime.now().strftime('%Y-%m-%d')}."),
        (re.compile(r"\b(developer|creator|author)\b", re.I), "I was developed by Roy for the Codsoft AI internship."),
    ]

    _FALLBACK = "I'm not sure I understand. Could you please rephrase?"

    def get_response(self, user_input: str) -> str:
        for pattern, reply in self._RULES:
            if pattern.search(user_input):
                return reply() if callable(reply) else reply
        return self._FALLBACK

    def chat(self) -> None:
        print("💬  Rule-Based Chatbot (type 'bye' to quit)\n")
        while True:
            user = input("You: ").strip()
            if not user:
                continue
            response = self.get_response(user)
            print(f"Bot: {response}")
            if re.search(r"\b(bye|goodbye|exit)\b", user, re.I):
                break
