responses = {
    'hello': "Hi there! How can I help you?",
    'hi': "Hello! How's it going?",
    'how are you': "I'm doing great, thank you for asking!",
    'your name': "I'm just a simple chatbot. You can call me Converso!",
    "product": "We have a wide variety of products available! You can check our catalog on the website.",
    "buy": "We offer a range of items for sale, please check our website for more details.",
    "return": "You can return most products within 30 days of receiving them. Please contact customer service for a return label.",
    "refund": "Refunds are processed after we receive the returned items. Please allow up to 10 business days for processing.",
    "hours": "We are open Monday to Friday, from 9 AM to 6 PM.",
    "open": "Our store is open from Monday to Friday, 9 AM to 6 PM.",
    "contact": "You can reach us at +123-456-7890 or email support@xyzstore.com.",
    "phone": "You can contact us at +123-456-7890 or via email at support@xyzstore.com.",
    "thank": "You're welcome! Let me know if you need anything else.",
    "thanks": "You're welcome! Let me know if you need further assistance.",
    "bye": "Goodbye! Have a great day!",
    'goodbye': "Goodbye! See you soon!",
    'help': "I can answer questions like 'How are you?', 'What's your name?', or say 'Bye' to exit."
}

# This is a dictionary where:

# The keys are keywords you expect the user to type ("hello", "refund", "buy", etc.)

# The values are the bot's responses when those keywords are found in the user input.




def chat():
    print("Welcome to Converso, How may I help you?")
    while True:
        user_input = input("You: ").lower()

        matched = False
        for keyword in responses: #This loop iterates over the keys of the responses dictionary. # In Python, when you loop over a dictionary directly (for x in some_dict:), it defaults to iterating over the keys. for value in responses.values()
            if keyword in user_input:
                print("Converso:", responses[keyword])
                matched = True
                if keyword in ['bye', 'goodbye']:
                    return  # exit the chat
                break

        if not matched:
            print("Converso: Sorry, I couldn't understand that. Please try again.")


chat()

