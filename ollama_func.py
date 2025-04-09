import ollama

messages = []  # persistent message history

def send_ollama(input_model, user_input):
    messages.append({'role': 'user', 'content': user_input})
    
    response = ollama.chat(model=input_model, messages=messages)
    
    assistant_msg = response['message']['content']
    messages.append({'role': 'assistant', 'content': assistant_msg})
    
    return assistant_msg