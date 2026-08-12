import ollama

from argos.config.identity import ARGOS_IDENTITY


MODEL = "qwen3:8b"


def ask_argos(message: str) -> str:
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": ARGOS_IDENTITY,
            },
            {
                "role": "user",
                "content": message,
            },
        ],
    )

    return response["message"]["content"]


def main() -> None:
    print()
    print("=" * 60)
    print("ARGOS")
    print("Autonomous Business & Growth Pilot")
    print("=" * 60)
    print()
    print(f"Model: {MODEL}")
    print("Status: ONLINE")
    print()

    message = input("Toni > ")

    print()
    print("ARGOS >")
    print()

    answer = ask_argos(message)

    print(answer)
    print()


if __name__ == "__main__":
    main()