import ollama

messages = []  # persistent message history

def send_ollama(input_model, user_input):
    #append user input to message history
    messages.append({'role': 'user', 'content': user_input})
    
    # get ollama response
    response = ollama.chat(model=input_model, messages=messages)
    
    # make sure the reponse knows convo history
    assistant_msg = response['message']['content']
    messages.append({'role': 'assistant', 'content': assistant_msg})
    
    return assistant_msg