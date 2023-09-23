
import tkinter as tk
import tkinter.font as tkFont
import random
import string

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Password Generator")
        self.geometry("400x200")
        self.homepage()

    def homepage(self):
#Headline         
        bold_font = tkFont.Font(family="Helvetica", size=20, weight="bold")  
        self.password_generator = tk.Label(self, text="Password Generator",font=bold_font, borderwidth=60, cursor="hand2")
        self.password_generator.pack()
#Make subtile ,box , or button
        self.password_length = tk.Label(self, text="Password Length:")
        self.password_length.pack(side="top")

        self.p_length_entry = tk.Entry(self)
        self.p_length_entry.pack(side="top")

        self.generate_password_button= tk.Button(self, text="Generate Password",borderwidth=-10, cursor="hand2", bg="#9933ff" , command=self.generate_password)
        
        self.generate_password_button.pack(side="top", padx=30, pady=80)

        self.password_display = tk.Label(self, text="")
        self.password_display.pack()

    def generate_password(self):
        password_length = int(self.p_length_entry.get())
#Error
        if password_length < 8:
            tk.messagebox.showerror("Error", "Password length must be at least 8 characters.")
            return
#password charactars types
        password_charac = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(password_charac) 
        for i in range(password_length))

        self.password_display.config(text=password)

if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()