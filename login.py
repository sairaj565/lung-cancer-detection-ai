import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

# -----------------------------
# LOGIN FUNCTION
# -----------------------------
def login():

    username = user_entry.get()
    password = pass_entry.get()

    # Default credentials
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Success", "Welcome Doctor")

        root.destroy()

        # Open Lung Cancer System
        subprocess.Popen([sys.executable, "lcd_cnn.py"])

    else:
        messagebox.showerror("Login Failed",
                             "Invalid Username or Password")


# -----------------------------
# UI WINDOW
# -----------------------------
root = tk.Tk()
root.title("Medical Login Portal")
root.geometry("450x350")
root.resizable(True, True) 
root.configure(bg="black")

# Title
title = tk.Label(root,
                 text="Lung Cancer Detection Login",
                 font=("Arial",18,"bold"),
                 fg="white",
                 bg="black")
title.pack(pady=20)

# Username
tk.Label(root,text="Username",
         fg="white",bg="black",
         font=("Arial",12)).pack()

user_entry = tk.Entry(root,font=("Arial",12))
user_entry.pack(pady=5)

# Password
tk.Label(root,text="Password",
         fg="white",bg="black",
         font=("Arial",12)).pack()

pass_entry = tk.Entry(root,
                      show="*",
                      font=("Arial",12))
pass_entry.pack(pady=5)

# Login Button
login_btn = tk.Button(root,
                      text="LOGIN",
                      font=("Arial",14,"bold"),
                      bg="green",
                      fg="white",
                      command=login)
login_btn.pack(pady=25)

# Footer
tk.Label(root,
         text="Authorized Medical Access Only",
         fg="yellow",
         bg="black").pack()

root.mainloop()