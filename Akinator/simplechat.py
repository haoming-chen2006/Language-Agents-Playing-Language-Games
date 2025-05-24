import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# Load environment variable
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the model
model = init_chat_model("gpt-4o-mini", model_provider="openai")

# Initial system message
system_instruction = {
    "role": "system",
    "content": (
        "You are a guessing game AI. Try to guess the identity (real celebrity, fictional character, game character, etc.) the user has in mind. "
        "You can ask yes/no questions step by step to narrow things down. "
        "You can only make one final guess of the actual identity by saying 'My final guess is that ...'. "
        "You cannot guess the identity directly (like saying 'Is it LeBron James?') except in the final guess. Don;t make a guess until you are very certain."
    )
}

# Conversation history
history = [system_instruction]
guessed = False
guess_count = 0
last_summarized = -1

# Main game loop
while not guessed:
    # 🧠 Every 5 questions: summarize reasoning
    if guess_count > 0 and guess_count % 5 == 0 and guess_count != last_summarized:
        print("summarizing reasoning...")

        summary_instruction = {
            "role": "system",
            "content": (
                "You are summarizing what you know so far about the identity from the previous yes/no questions. "
                "DO NOT GUESS the identity or continue the game. Just give one paragraph describing the traits of the identity. "
                "Example: 'The identity is a real person, not an actor or musician, and is known for their work in sports. Possibly an athlete.'"
            )
        }

        summary_messages = history + [summary_instruction]
        summary_response = model.invoke(summary_messages)
        summary_text = summary_response.content
        summary_prefix = "Summary of reasoning so far, future question focus on this: "

        history.append({"role": "assistant", "content": summary_prefix + summary_text})
        last_summarized = guess_count
        continue  # Skip new question this turn

    # 🗣️ AI asks next question
    ai_response = model.invoke(history)
    ai_text = ai_response.content
    print("\nAI:", ai_text)

    history.append({"role": "assistant", "content": ai_text})

    # 🤔 Check if it's making a final guess
    if "My final guess is that" in ai_text:
        user_input = input("User (yes/no or 'correct'): ").strip().lower()
        history.append({"role": "user", "content": user_input})
        if user_input == "correct":
            print("🎉 The AI guessed correctly!")
            guessed = True
        else:
            print("❌ The AI guessed incorrectly!")
            break
    else:
        user_input = input("User (yes/no): ").strip().lower()
        history.append({"role": "user", "content": user_input})
        guess_count += 1
        print(history)



