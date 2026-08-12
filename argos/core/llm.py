import json
import urllib.request

from argos.config.identity import ARGOS_IDENTITY


class OllamaClient:
    """Client for the local Ollama LLM."""

    def __init__(
        self,
        model: str = "qwen3:8b",
        host: str = "http://localhost:11434",
    ) -> None:
        self.model = model
        self.host = host.rstrip("/")

    def generate(self, prompt: str) -> str:
        full_prompt = f"""
{ARGOS_IDENTITY}

---

CURRENT USER REQUEST:

{prompt}

---

IMPORTANT:
You are ARGOS.
Do not confuse ARGOS with other systems, companies,
satellites, projects or organisations that share the name.
Your identity above defines what ARGOS means in this system.

Respond according to the ARGOS identity and mission.
"""

        payload = json.dumps(
            {
                "model": self.model,
                "prompt": full_prompt,
                "stream": False,
            }
        ).encode("utf-8")

        request = urllib.request.Request(
            f"{self.host}/api/generate",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        with urllib.request.urlopen(request, timeout=600) as response:
            data = json.loads(response.read().decode("utf-8"))

        return data["response"]