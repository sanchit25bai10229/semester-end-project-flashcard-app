import tkinter as tk
from tkinter import messagebox
import csv
import random
import os

class Flashcard:
    
    def __init__(self, question, answer):
        
        self.question = question
        
        self.answer = answer
        
        self.is_known = False
        
    def mark_known(self, known):
        
        self.is_known = known
        

class quizdeck:
    
    def __init__(self):
        self.cards = []
        
    def load_from_csv(self, filepath):
        
        self.cards = []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                
                
                try:
                    header = [h.strip().lower() for h in next(reader)]
                except StopIteration:
                    messagebox.showerror("Loading Error", "The 'cards.csv' file is empty.")
                    return False
                
                if 'question' not in header or 'answer' not in header:
                    messagebox.showerror("Loading Error", 
                                         "CSV file is missing required headers. Please ensure the first row contains 'Question' and 'Answer' (case-insensitive).")
                    return False

                q_index = header.index('question')
                a_index = header.index('answer')
                
                for row_data in reader:
                    
                    if len(row_data) < max(q_index, a_index) + 1:
                        continue 
                        
                    question = row_data[q_index].strip()
                    answer = row_data[a_index].strip()
                    
                    if question and answer:
                        card = Flashcard(question, answer)
                        self.cards.append(card)
            return True
        except FileNotFoundError:
            messagebox.showerror("Loading Error", f"The file '{filepath}' was not found. Check the directory printed in your console.")
            return False
        except Exception as e:
            
            messagebox.showerror("Loading Error", 
                                 f"Failed to load cards due to a system error. \nError: {e}")
            return False
    
    def shuffle_deck(self):
        
        random.shuffle(self.cards)
        
        
class F_App:
    
    def __init__(self, master):
        
        self.master = master
        
        master.title("Flashcard Tutor")
        
        master.config(padx = 30, pady = 30, bg = '#1e1e1e')
        
        self.deck = quizdeck()
                
        self.current_card_index = 0
        
        self.known_count = 0
        
        
        print("-" * 50)
        print(f"Current Working Directory: {os.getcwd()}")
        print(f"Looking for file: {os.path.join(os.getcwd(), 'cards.csv')}")
        print("-" * 50)
        
        
        if not self.deck.load_from_csv('cards.csv'):
            
            master.destroy()
            
            return
        
        self.deck.shuffle_deck()
        
        self.total_cards = len(self.deck.cards)
        
        self.status_label = tk.Label(master, text = "Loading...", font = ('Arial', 12, 'bold'), bg = '#1e1e1e', fg = '#ecf0f1')
        
        self.status_label.grid(row = 0, column = 0, columnspan = 2, pady = (0, 20))
        
        self.card_frame = tk.Frame(master, padx = 20, pady = 40, bg = '#2c3e50', relief = tk.RAISED, borderwidth = 2)
        
        self.card_frame.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = "ew")
        
        self.question_label = tk.Label(self.card_frame, text="", wraplength=450, font=('Arial', 18, 'bold'), bg='#2c3e50', fg='#ecf0f1')
        
        self.question_label.pack(pady=10)

        self.answer_label = tk.Label(self.card_frame, text="[ANSWER HIDDEN]", wraplength=450, font=('Arial', 16, 'italic'), bg='#2c3e50', fg='#4CAF50')
        
        self.answer_label.pack(pady=10)
        
        self.control_frame = tk.Frame(master, bg='#1e1e1e')
        
        self.control_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.reveal_button = tk.Button(self.control_frame, text="REVEAL ANSWER", command=self.reveal_answer, 
                                       width=18, font=('Arial', 10, 'bold'), bg='#00BFFF', fg='white')
        
        self.reveal_button.grid(row=0, column=0, columnspan=2, pady=10)

        self.known_button = tk.Button(self.control_frame, text="I KNEW IT (Y)", command=lambda: self.evaluate_answer(True), 
                                      width=15, font=('Arial', 10), bg='#4CAF50', fg='#ecf0f1', state=tk.DISABLED)
        
        self.known_button.grid(row=1, column=0, padx=5, pady=10)

        self.unknown_button = tk.Button(self.control_frame, text="I MISSED IT (N)", command=lambda: self.evaluate_answer(False), 
                                        width=15, font=('Arial', 10), bg='#F44336', fg='#ecf0f1', state=tk.DISABLED)
        
        self.unknown_button.grid(row=1, column=1, padx=5, pady=10)
        
        self.next_card()
        
    def update_status(self):
        
        if self.current_card_index <= self.total_cards:
            
            status_text = f"Card {self.current_card_index}/{self.total_cards} | Known : {self.known_count}"
        
        else:
            
            status_text = f"SESSION COMPLETED | Final Score: {self.known_count}/{self.total_cards}"
            
        self.status_label.config(text = status_text)
        
    def enable_evaluation_buttons(self, state):
        
        self.known_button.config(state = state)
        
        self.unknown_button.config(state = state)
        
        self.reveal_button.config(state=tk.DISABLED if state == tk.NORMAL else tk.NORMAL)
        
    def next_card(self):
        
        if self.current_card_index >= self.total_cards:
            
            self.question_label.config(text = "Session Completed!")
            
            self.answer_label.config(text = "Review finished. Close the window to exit.")
            
            self.reveal_button.config(state=tk.DISABLED)
            
            self.known_button.config(state=tk.DISABLED)
            
            self.unknown_button.config(state=tk.DISABLED)
            
            self.update_status()
            
            return
        
        current_card = self.deck.cards[self.current_card_index]
        
        self.question_label.config(text = current_card.question)
        
        self.answer_label.config(text = "[ANSWER HIDDEN]", fg = '#4CAF50')
        
        self.enable_evaluation_buttons(tk.DISABLED)
        
        self.reveal_button.config(state = tk.NORMAL)
        
        self.current_card_index += 1
        
        self.update_status()
        
    def reveal_answer(self):
        
        current_card = self.deck.cards[self.current_card_index - 1]
        
        self.answer_label.config(text=current_card.answer)
        
        self.enable_evaluation_buttons(tk.NORMAL)
        
        self.reveal_button.config(state=tk.DISABLED)

        
    def evaluate_answer(self, known):
        
        card_to_mark = self.deck.cards[self.current_card_index - 1]
        
        card_to_mark.mark_known(known)
        
        if known:
            
            self.known_count += 1
            
        self.next_card()
        


if __name__ == '__main__':
    
    root = tk.Tk()
    
    app = F_App(root)
    
    def key_press(event):
        
        if event.char == 'r' and app.reveal_button['state'] == tk.NORMAL:
            
            app.reveal_answer()
            
        elif event.char == 'y' and app.known_button['state'] == tk.NORMAL:
            
            app.evaluate_answer(True)
            
        elif event.char == 'n' and app.unknown_button['state'] == tk.NORMAL:
            
            app.evaluate_answer(False)
            
    root.bind('<Key>', key_press)

    root.mainloop()