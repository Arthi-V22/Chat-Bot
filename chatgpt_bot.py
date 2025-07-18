import tkinter as tk
from tkinter import scrolledtext

def get_bot_response():
    user_input = user_entry.get().strip().lower()
    user_entry.delete(0, tk.END)

    if not user_input:
        return

    chat_window.insert(tk.END, f"You: {user_input}\n")

    if "hello" in user_input or "hi" in user_input:
        bot_response = "Hello! How can I help you today?"
    elif "how are you" in user_input:
        bot_response = "I'm just a bot, but I'm doing great! 😊"
    elif "your name" in user_input:
        bot_response = "I'm a simple Python chatbot."
    elif "bye" in user_input:
        bot_response = "Goodbye! 👋 Have a great day!"
    else:
        bot_response = "Sorry, I didn't understand that. 🤖"

    chat_window.insert(tk.END, f"Bot: {bot_response}\n\n")

window = tk.Tk()
window.title("Offline AI Chatbot")
window.geometry("500x500")

chat_window = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

user_entry = tk.Entry(window, font=("Arial", 12))
user_entry.pack(padx=10, pady=5, fill=tk.X)
user_entry.bind("<Return>", lambda event=None: get_bot_response())

send_button = tk.Button(window, text="Send", command=get_bot_response, font=("Arial", 12))
send_button.pack(pady=5)

window.mainloop()