# Takes a users prompt
# Feeds users prompt to AI
# AI prints response to file or console

import subprocess


def user_prompt():

    # ask user a question
    user_question = input("What is your question >> ")

    # return string

    return user_question


def model_answer(prompt):

    result = subprocess.run(["ollama", "run", "qwen3:0.6b", prompt],
                            capture_output=True,
                            text=True
                            )

    

    if result.returncode == 0:
        print("Model worked")
        response = result.stdout
    else:
        print("Command failed")
        print(response.stderr)
        response = "Error: could not contact model"

    return response


def file_console(response):

    print()
    print("AI Response:")
    print()

    print(response)
    print("Do you want to print this to file? ")
    file_out = input("(y/n) >> ")

    if file_out.lower() == "y":
        with open("response_out.txt", "w", encoding="utf-8") as file:
            file.write(response)

        print("Response saved to response_out.txt")



def main():

    # get prompt and save

    prompt = user_prompt()

    # feed prompt to AI and save response

    response = model_answer(prompt)

    # decide to print to file or console

    file_console(response)


if __name__ == "__main__":
    main()
