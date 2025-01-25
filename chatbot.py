user_input=input("Your question")
print("Chatbot is online:")
if "hello" in user_input or "hi" in user_input:
    print("Hello! how can I help You.")
elif "weather" in user_input:
    print("The weather will be hot today")
elif "Weather" in user_input:
    print("The weather will be rainy today")
elif "Coding" in user_input:
    print("Refer to external links")
