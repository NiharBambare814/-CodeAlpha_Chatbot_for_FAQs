import tkinter as tk
from similarity import FAQModel
from tkinter import scrolledtext
import ttkbootstrap as ttk
from preprocessing import preprocess_text
from similarity import FAQModel

class FAQChatbotApp:
    def __init__(self):
        self.root = ttk.Window(themename="cosmo")
        self.root.title("FAQ Chatbot")
        self.root.geometry("600x500")

        self.faq_model = FAQModel("faqs.csv", preprocess_text)

        self._build_widgets()
    
    def _build_widgets(
            
            self):
        # Chat display area
        self.chat_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Arial", 12))
        self.chat_box.config(state=tk.DISABLED)
        self.chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Entry box
        self.entry_var = tk.StringVar()
        self.entry_box = ttk.Entry(self.root, textvariable=self.entry_var, font=("Arial", 14))
        self.entry_box.pack(padx=10, pady=(0,10), fill=tk.X)
        self.entry_box.focus()
        self.entry_box.bind("<Return>", self._on_enter)

        # Send button
        self.send_button = ttk.Button(self.root, text="Send", command=self._on_send)
        self.send_button.pack(padx=10, pady=(0,10))

    def _on_enter(self, event):
        self._handle_user_message()

    def _on_send(self):
        self._handle_user_message()

    def _handle_user_message(self):
        user_msg = self.entry_var.get().strip()
        if not user_msg:
            return
        self._insert_chat_message("You", user_msg)
        self.entry_var.set("")
        # Get chatbot response
        bot_response = self.faq_model.get_best_answer(user_msg)
        self._insert_chat_message("Bot", bot_response)

    def _insert_chat_message(self, sender, message):
        self.chat_box.config(state=tk.NORMAL)
        self.chat_box.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_box.config(state=tk.DISABLED)
        self.chat_box.see(tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FAQChatbotApp()
    app.run()
