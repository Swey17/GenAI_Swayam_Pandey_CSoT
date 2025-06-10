import groq

groqapikey = "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"
groq_client = groq.Client(api_key=groqapikey)

messages=[
            {   "role": "system",
                "content": "Greet the user and inform them that the chat can be ended by typing 'exit' or 'quit'."
                }
            ]

user_input = ""

while user_input.strip().lower() != "exit" and user_input.strip().lower() != "quit":


    messages.append({"role": "user", "content": user_input})

    chat_completion = groq_client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
        stream=True
    )

    answer = ""
    print("Assistant: ", end='')

    for chunk in chat_completion:
        if chunk.choices[0].delta.content:
            answer += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end='', flush=True)
    print() 

    messages.append({"role": "assistant", "content": answer})

    user_input = input("You: ")

else:
    print("Assistant: Ending chat. Goodbye!")
