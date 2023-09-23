import tkinter as tk

def button_click(event):
    current = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

app = tk.Tk()
app.title("Calculator")
#headline
headline_label = tk.Label(app, text="Calculator", font=("Helvetica", 16, "bold"))
headline_label.pack()

entry = tk.Entry(app, font=("Helvetica", 8))
entry.pack(fill=tk.BOTH, expand=True)

button_frame = tk.Frame(app)
button_frame.pack()
#button keys
button_texts = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row, col = 1,0
for text in button_texts:
    button = tk.Button(button_frame, text=text, font=("Helvetica", 8), width=5, height=5)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

app.mainloop()
