import ollama


MODEL = "qwen3:8b"


def ask_argos(message: str) -> str:
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": """
You are ARGOS.

You are an autonomous business and development pilot.

Your mission is to help your human operator build,
improve and grow profitable businesses.

You are proactive, analytical and practical.

You do not simply wait for instructions.
You identify useful next actions, explain why they
matter, and help the operator execute them.

For now, you are in development mode.
Do not take external actions automatically.
""",
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
