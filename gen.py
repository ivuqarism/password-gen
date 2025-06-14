import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_upper, use_numbers, use_symbols):
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    if length < 1:
        return ""

    return "".join(random.choice(characters) for _ in range(length))

def on_generate():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Hata", "Lütfen pozitif bir sayı girin.")
            return
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")
        return

    use_upper = var_upper.get()
    use_numbers = var_numbers.get()
    use_symbols = var_symbols.get()

    password = generate_password(length, use_upper, use_numbers, use_symbols)
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

app = tk.Tk()
app.title("Basit Şifre Üretici")
app.geometry("350x250")
app.resizable(False, False)

tk.Label(app, text="Şifre uzunluğu:").pack(pady=(10,0))
entry_length = tk.Entry(app)
entry_length.pack()

var_upper = tk.BooleanVar(value=True)
chk_upper = tk.Checkbutton(app, text="Büyük harf kullan", variable=var_upper)
chk_upper.pack()

var_numbers = tk.BooleanVar(value=True)
chk_numbers = tk.Checkbutton(app, text="Rakam kullan", variable=var_numbers)
chk_numbers.pack()

var_symbols = tk.BooleanVar(value=True)
chk_symbols = tk.Checkbutton(app, text="Sembol kullan", variable=var_symbols)
chk_symbols.pack()

tk.Label(app, text="Oluşan şifre:").pack(pady=(10,0))
entry_password = tk.Entry(app, width=30)
entry_password.pack()

btn_generate = tk.Button(app, text="Şifre Oluştur", command=on_generate)
btn_generate.pack(pady=10)

app.mainloop()
