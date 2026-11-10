# fake_ai.py

# This function pretends to be an AI model.
# It receives a prompt.
# It returns a response.

def fake_model(prompt):
    response = "You said: " + prompt
    return response


def main():
    user_prompt = input("Enter your prompt >> ")

    ai_response = fake_model(user_prompt)

    print(ai_response)


main()
