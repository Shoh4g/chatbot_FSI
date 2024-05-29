import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from chatbot_backend import load_knowledgebase, find_best_match, get_answer_for_question

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")

        self.knowledge_base = load_knowledgebase('knowledge_base.json')
        self.current_organization = None

        self.chat_history = scrolledtext.ScrolledText(master, width=60, height=20)
        self.chat_history.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.user_input = tk.Entry(master, width=50)
        self.user_input.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.switch_org_button = tk.Button(master, text="Switch Organization", command=self.switch_organization)
        self.switch_org_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def send_message(self):
        user_input_text = self.user_input.get()
        self.user_input.delete(0, tk.END)

        if not self.current_organization:
            self.current_organization = user_input_text.strip()
            self.add_to_chat_history("Bot: You are now exploring " + self.current_organization)
            return

        if user_input_text.lower() == 'quit':
            self.master.quit()
            return

        best_match = find_best_match(user_input_text, [q['question'] for q in self.knowledge_base[self.current_organization]])

        if best_match:
            answer = get_answer_for_question(best_match, self.knowledge_base, self.current_organization)
            self.add_to_chat_history("Bot: " + answer)
        else:
            self.add_to_chat_history("Bot: Unfortunately, I am not aware of the answer. Kindly review your question.")

    def switch_organization(self):
        self.current_organization = None
        self.add_to_chat_history("Bot: You have switched to a new organization. Please enter the organization name.")

    def add_to_chat_history(self, message):
        self.chat_history.insert(tk.END, message + '\n')
        self.chat_history.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    my_gui = ChatbotGUI(root)
    root.mainloop()
