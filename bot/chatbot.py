print("Bot:hello")
while True:
    user=input("You:").lower()
    if "hi" in user or "hello" in user:
        print("Bot:hello")
    elif "name" in user:
        print("Bot:my name is chatbot")
    elif "help" in user:
        print("Bot:here iam gonna help you tell me what you need")  
    elif "bye" in user:
        print("Bot: bye")
        break
    else:
        print("trouble")          
