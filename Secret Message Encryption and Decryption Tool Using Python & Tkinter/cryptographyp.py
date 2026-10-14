import tkinter as tk
from tkinter import messagebox
import base64
# function
def clear_all():
    message_entry.delete("1.0", tk.END),
    result_entry.delete("1.0", tk.END)
    key_entry.delete("0", tk.END)

def encrypt_message():
    message = message_entry.get("1.0", tk.END).strip()
    key = key_entry.get()

    if message == "" or key=="":
        messagebox.showwarning("Warning", "Eneter message and secret key!")
        return
    # convert message in bytes
    message_bytes = message.encode("utf-8")
    # Encode message using Base64
    encrypted = base64.b64encode(message_bytes).decode("utf-8")

    # add key to encrypted message
    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, encrypted)
def decrypt_message():
    encrypted_message = message_entry.get("1.0", tk.END).strip()
    key = key_entry.get()

    if encrypted_message == "" or key == "":
        messagebox.showwarning("Warning", "Enter encrypted message and secret key!")
        return
    try:
        # decode base64
        decrypted = base64.b64decode(
            encrypted_message.encode("utf-8")
        ).decode("utf-8")

        result_entry.delete("1.0", tk.END)
        result_entry.insert(tk.END, decrypted)
    except Exception:
        messagebox.showerror("Error", "Invalid encrypted message!")


# create window
root = tk.Tk()
# set window properties
root.title("cryptograpy")
root.geometry("600x550")
root.resizable(False, False)
root.configure(bg="#000000")

# set properties
# title
title_label = tk.Label(
    root,
    text="🔐 Secret Message Tool",
    font=("Arial", 22, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title_label.pack(
    pady=20,
    ipady=10,
    ipadx=10
)
# Message label
message_label = tk.Label(
    root,
    text="Enter Message:",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="black"
)
message_label.pack(
    anchor="w",
    padx=40
)
# message entry
message_entry = tk.Text(
    root,
    height=6,
    width=60,
    font=("Arial", 12),
)
message_entry.pack(
    pady=8,
)
# key label
key_label = tk.Label(
    root,
    text="Secret Key:",
    font=("Arial", 12, "bold"),
    bg="black",
    fg="white"
)
key_label.pack(
    anchor="w", 
    padx=40
)
# key entry
key_entry = tk.Entry(
    root,
    width=45,
    font=("Arial", 12),
    show="*"
)
key_entry.pack(
    pady=8
)
# buttons
button_frame = tk.Frame(
    root,
    bg="black"
)
button_frame.pack(
    pady=15
)
encrypt_button = tk.Button(
    button_frame,
    text="🔐 Encrypt",
    font=("Arial", 12, "bold"),
    width=12,
    activebackground="blue",
    activeforeground="white",
    command=encrypt_message
)
encrypt_button.grid(
    row=0,
    column=0,
    padx=8
)
decrypt_button = tk.Button(
    button_frame,
    text="🔓 Decrypt",
    font=("Arial", 12, "bold"),
    width=12,
    activebackground="green",
    activeforeground="white",
    command=decrypt_message
)
decrypt_button.grid(
    row=0,
    column=1,
    padx=8
)
clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    width=12,
    activebackground="red",
    activeforeground="white",
    command=clear_all
)
clear_button.grid(
    row=0,
    column=2,
    padx=8
)
# reseult label
result_label = tk.Label(
    root,
    text="Result:",
    font=("Arial", 12, "bold"),
    bg="black",
    fg="white"
)
result_label.pack(padx=40, anchor="w")
result_entry = tk.Text(
    root,
    height=6,
    width=60,
    font=("Arial", 12, "bold")
)
result_entry.pack(pady=8)
root.mainloop()
