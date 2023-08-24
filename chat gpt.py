import openai

openai.api_key = "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"

messages = []
system_msg = input('''                                  HI I AM TECHTALK
                     What type of chatbot would you like me to be?\n''')
messages.append({"role": "system", "content": system_msg})

print("Your brand new assistant is ready to roll !")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")