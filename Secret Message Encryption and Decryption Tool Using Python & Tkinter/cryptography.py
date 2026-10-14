import tkinter as tk
from tkinter import messagebox
import base64


# -----------------------------
# Encryption Function
# -----------------------------
def encrypt_message():
    message = message_entry.get("1.0", tk.END).strip()
    key = key_entry.get()

    if message == "" or key == "":
        messagebox.showwarning("Warning", "Enter message and secret key!")
        return

    # Convert message to bytes
    message_bytes = message.encode("utf-8")

    # Encode message using Base64
    encrypted = base64.b64encode(message_bytes).decode("utf-8")

    # Add key to the encrypted message
    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, encrypted)


# -----------------------------
# Decryption Function
# -----------------------------
def decrypt_message():
    encrypted_message = message_entry.get("1.0", tk.END).strip()
    key = key_entry.get()

    if encrypted_message == "" or key == "":
        messagebox.showwarning("Warning", "Enter encrypted message and secret key!")
        return

    try:
        # Decode Base64
        decrypted = base64.b64decode(
            encrypted_message.encode("utf-8")
        ).decode("utf-8")

        result_entry.delete("1.0", tk.END)
        result_entry.insert(tk.END, decrypted)

    except Exception:
        messagebox.showerror("Error", "Invalid encrypted message!")


# -----------------------------
# Clear Function
# -----------------------------
def clear_all():
    message_entry.delete("1.0", tk.END)
    key_entry.delete(0, tk.END)
    result_entry.delete("1.0", tk.END)


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()

root.title("Secret Message Encryption Tool")
root.geometry("600x550")
root.resizable(False, False)
root.configure(bg="#1e1e1e")


# -----------------------------
# Title
# -----------------------------
title_label = tk.Label(
    root,
    text="🔐 Secret Message Tool",
    font=("Arial", 22, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title_label.pack(pady=20)


# -----------------------------
# Message Label
# -----------------------------
message_label = tk.Label(
    root,
    text="Enter Message:",
    font=("Arial", 12, "bold"),
    bg="#1e1e1e",
    fg="white"
)

message_label.pack(anchor="w", padx=40)


# -----------------------------
# Message Entry
# -----------------------------
message_entry = tk.Text(
    root,
    height=6,
    width=60,
    font=("Arial", 12)
)

message_entry.pack(pady=8)


# -----------------------------
# Key Label
# -----------------------------
key_label = tk.Label(
    root,
    text="Secret Key:",
    font=("Arial", 12, "bold"),
    bg="#1e1e1e",
    fg="white"
)

key_label.pack(anchor="w", padx=40)


# -----------------------------
# Key Entry
# -----------------------------
key_entry = tk.Entry(
    root,
    width=45,
    font=("Arial", 12),
    show="*"
)

key_entry.pack(pady=8)


# -----------------------------
# Buttons
# -----------------------------
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=15)


encrypt_button = tk.Button(
    button_frame,
    text="🔐 Encrypt",
    font=("Arial", 12, "bold"),
    width=12,
    command=encrypt_message
)

encrypt_button.grid(row=0, column=0, padx=8)


decrypt_button = tk.Button(
    button_frame,
    text="🔓 Decrypt",
    font=("Arial", 12, "bold"),
    width=12,
    command=decrypt_message
)

decrypt_button.grid(row=0, column=1, padx=8)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    width=12,
    command=clear_all
)

clear_button.grid(row=0, column=2, padx=8)


# -----------------------------
# Result Label
# -----------------------------
result_label = tk.Label(
    root,
    text="Result:",
    font=("Arial", 12, "bold"),
    bg="#1e1e1e",
    fg="white"
)

result_label.pack(anchor="w", padx=40)


# -----------------------------
# Result Box
# -----------------------------
result_entry = tk.Text(
    root,
    height=6,
    width=60,
    font=("Arial", 12)
)

result_entry.pack(pady=8)


# -----------------------------
# Run Application
# -----------------------------
root.mainloop()