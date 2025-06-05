from archive.ollama_func import send_ollama

def main():
    print("Welcome to the chatbot! (type 'exit' to quit)\n")
    model = 'mistral'

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response = send_ollama(model, user_input)
        print("Ollama:", response, "\n")

if __name__ == '__main__':
    main()