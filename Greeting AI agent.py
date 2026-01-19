
print("=== GREETING AI AGENT ===")
print("Type 'exit' to stop the program")
print("Agent: Hello! Welcome. How can I help you today?")

while True:
    user_input = input("\nYou: ").lower()

    if user_input == "exit":
        print("Agent: Thank you for chatting with me. Goodbye!")
        break

    elif "what is ai" in user_input or "define ai" in user_input:
        print("Agent: AI stands for Artificial Intelligence. It allows machines to think and act like humans.")

    elif "hi" in user_input or "hello" in user_input:
        print("Agent: Hello! Nice to meet you!")

    elif "how are you" in user_input:
        print("Agent: I am fine. What about you?")

    elif "fine" in user_input or "good" in user_input:
        print("Agent: That's good!")

    elif "what is greeting" in user_input:
        print("Agent: A greeting is a polite way of saying hello to someone.")

    elif "your name" in user_input:
        print("Agent: My name is Greeting AI Agent.")

    elif "who created you" in user_input or "creator" in user_input:
        print("Agent: I was created using Python programming.")

    elif "what are you doing" in user_input:
        print("Agent: I am here to greet users and answer simple questions.")

    elif "purpose" in user_input:
        print("Agent: My purpose is to interact with users politely.")

    elif "help" in user_input:
        print("Agent: You can ask simple questions like what is AI, greeting, date, or time.")

    elif "date" in user_input:
        from datetime import date
        print("Agent: Today's date is", date.today())

    elif "time" in user_input:
        from datetime import datetime
        print("Agent: Current time is", datetime.now().strftime("%H:%M:%S"))

    elif "weather" in user_input:
        print("Agent: I cannot access live weather yet.")

    elif "study" in user_input:
        print("Agent: Studying consistently leads to success!")

    elif "thank" in user_input:
        print("Agent: You are welcome!")

    else:
        print("Agent: I am still learning. Please ask a simple basic question.")

