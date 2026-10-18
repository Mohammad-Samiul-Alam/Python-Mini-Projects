import tkinter as tk
from tkinter import messagebox
import base64

class SecretMessageTool:
    # Constructor
    def __init__(self, root):
        self.root = root

        # set window properties
        self.root.title("secret message tool")
        self.root.geometry("600x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#010101")

        # Create GUI Components
        self.create_widgets()

    # create widget
    def create_widgets(self):
        # create title
        self.title_label = tk.Label(
            self.root,
            text="🔐 Secret Message Tool",
            font=("Arial", 24, "bold"),
            bg="#3f3f3f",
            fg="#ffffff"
        )
        self.title_label.pack(
            pady=22,
            ipadx=10,
            ipady=10
        )
        # Message label
        self.message_label = tk.Label(
            self.root,
            text="Enter message:",
            font=("Arial", 14, "bold"),
            bg="#010101",
            fg="white"

        )
        self.message_label.pack(
            padx=30,
            anchor="w"
        )
        # Message Entry
        self.message_entry = tk.Text(
            self.root,
            height=6,
            width=60,
            font=("Arial", 12)
        )
        self.message_entry.pack(pady=8)
        # Secret key
        self.secret_label = tk.Label(
            self.root,
            font=("Arial", 14, "bold"),
            text="Secret key:",
            bg="#010101",
            fg="white"
        )
        self.secret_label.pack(
            anchor="w",
            padx=30
        )
        # secret key
        self.secret_key = tk.Entry(
            self.root,
            font=("Arial", 14, "bold"),
            show="*",
            width=45
        )
        self.secret_key.pack(
            pady=8
        )
        # button frame
        self.button_frame = tk.Frame(
            self.root,
            bg="#010101",
        )
        self.button_frame.pack(
            pady=10
        )
        # encryption button
        self.encrypt_button = tk.Button(
            self.button_frame,
            text="🔐 Encrypt",
            font=("Arial", 12, "bold"),
            bg="green",
            fg="white",
            width=12,
            bd=0,
            relief="flat",
            overrelief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=self.encrypt_message
        )
        self.encrypt_button.grid(
            row=0,
            column=0,
            padx=8
        )
        # decrypt button
        self.decrypt_button = tk.Button(
            self.button_frame,
            text="🔓 Decrypt",
            font=("Arial", 12, "bold"),
            width=12,
            bg="blue",
            fg="white",
            bd=0,
            relief="flat",
            overrelief="flat",
            highlightthickness=0,
            borderwidth=0,
            command=self.decrypt_message
        )
        self.decrypt_button.grid(
            row=0,
            column=1,
            padx=8
        )
        # Clear button
        self.clear_button = tk.Button(
            self.button_frame,
            text="Clear",
            font=("Arial", 12, "bold"),
            width=12,
            bg="Red",
            fg="White",
            bd=0,
            relief="flat",
            overrelief="flat",
            highlightthickness=0,
            borderwidth=0,
            command=self.clear
        )
        self.clear_button.grid(
            row=0,
            column=2,
            padx=8
        )
        # Result label
        self.result_label = tk.Label(
            self.root,
            text="Result:",
            font=("Arial", 14, "bold"),
            bg="#010101",
            fg="white"
        )
        self.result_label.pack(
            padx=30,
            anchor="w"
        )

        # Result Box
        self.result_box = tk.Text(
            self.root,
            height=6,
            width=60,
            font=("Arial", 12)
        )
        self.result_box.pack(
            pady=8
        )

    # Clear Method
    def clear(self):
        self.message_entry.delete("1.0", tk.END)
        self.secret_key.delete("0", tk.END),
        self.result_box.delete("1.0", tk.END)

    # Ecryption method
    def encrypt_message(self):
        # Get message and Secret key
        message = self.message_entry.get(
            "1.0", tk.END
        ).strip()

        key = self.secret_key.get()

        if(message == "" or key == ""):
            messagebox.showwarning("Warning", "Enter Message & Secret key!")

        # convert message into bytes
        message_bytes = message.encode("utf-8")

        # encoding message using Base64
        encrypted = base64.b64encode(
            message_bytes
        ).decode("utf-8")

        # display result
        self.result_box.delete("1.0", tk.END)
        self.result_box.insert(tk.END, encrypted)
        
    # decrypt message
    def decrypt_message(self):
        # get message & secret key
        encrypted_message = self.message_entry.get(
            "1.0", tk.END
        ).strip()

        key = self.secret_key.get()

        # validate input
        if(encrypted_message == "" or key==""):
            messagebox.showwarning("Warning", "Enter message & secret key!")

        try:
            decrypted = base64.b64decode(
                encrypted_message.encode("utf-8"),
                validate=True
            ).decode("utf-8")

            # show result
            self.result_box.delete("1.0", tk.END)
            self.result_box.insert(tk.END, decrypted)
        except Exception:
            messagebox.showerror("Error", "Invalid Encrypted Message")

# Main Program
if __name__ == "__main__":
    # Create main window
    root = tk.Tk()
    
    # Create object of the class
    app = SecretMessageTool(root)

    # Run application
    root.mainloop()
