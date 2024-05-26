from tkinter import *
import tkinter as tk
import os
root =  Tk()
def show_history():

    history_window = Toplevel(root) 
    history_window.title("Search History")
    history_window.geometry("500x600")
    history_window.resizable(False,False)

    history_text = Text(history_window, width=60, height=40,bg="#009688")
    history_text.pack()

    with open("search_history.txt", "r") as f:
        history_text.config(state=NORMAL)
        history_text.insert(END, f.read())
        history_text.config(state=DISABLED)
    # This function clears the search history file and updates the GUI.
    def clear_history():
        if os.path.exists("search_history.txt"):
            os.remove("search_history.txt")
            print("Search history cleared.")
            history_text.config(state=NORMAL)
            history_text.delete('1.0', tk.END)
            # Display a confirmation message
            history_text.insert(tk.END, "HISTORY has been cleared\n")
            history_text.config(state=DISABLED)
    # clear button on history window
    clear_button = Button(history_window, text="CLEAR HISTORY", command=clear_history,padx=10,pady=10,bg="#008080",borderwidth=2,border=2,relief=SOLID, font=("aerial",8),fg="white")
    clear_button.place(relx=0.7660, rely=0, anchor="nw")
