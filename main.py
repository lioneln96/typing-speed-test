import tkinter as tk
from tkinter import font
import time

SAMPLE_TEXT = "The world you wish for"


def start_test():
    start_time = time.time()
    input_entry.config(state=tk.NORMAL)
    input_entry.delete(0, tk.END)
    input_entry.focus()
    input_entry.bind("<Return>", lambda event: end_test(start_time))
    start_button.config(state=tk.DISABLED)


def end_test(start_time):
    typed_text = input_entry.get()
    if typed_text == SAMPLE_TEXT:
        elapsed_time = time.time() - start_time
        typed_words = len(typed_text.split())
        speed = int(typed_words / (elapsed_time / 60))
        result_label.config(text=f"Your typing speed: {speed} words per minute")
    else:
        result_label.config(text="Incorrect text. Please retype the sample.")
    input_entry.config(state=tk.DISABLED)
    start_button.config(state=tk.NORMAL)
    input_entry.unbind("<Return>")


window = tk.Tk()
window.title("Typing Speed Test")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width / 2) - (600 / 2)
y = (screen_height / 2) - (400 / 2)

window.geometry(f"600x400+{int(x)}+{int(y)}")
window.configure(bg="#0F52BA")

text_label_font = font.Font(family="Helvetica", size=20, weight="bold")
text_label = tk.Label(window, text="Type the following text:", fg="white", bg="#0F52BA", font=text_label_font)
text_label.pack(pady=20)

sample_text_font = font.Font(family="Helvetica", size=16)
sample_text_label = tk.Label(window, text=SAMPLE_TEXT, fg="white", bg="#0F52BA", wraplength=550, font=sample_text_font)
sample_text_label.pack(pady=20)

input_entry_font = font.Font(family="Helvetica", size=16)
input_entry = tk.Entry(window, font=input_entry_font)
input_entry.pack(pady=20)

start_button_font = font.Font(family="Helvetica", size=16)
start_button = tk.Button(window, text="Start", command=start_test, bg="#0F52BA", fg="black", font=start_button_font, borderwidth=0)
start_button.pack(pady=20)

result_label_font = font.Font(family="Helvetica", size=20)
result_label = tk.Label(window, text="", fg="white", bg="#0F52BA", font=result_label_font)
result_label.pack(pady=20)

window.mainloop()





