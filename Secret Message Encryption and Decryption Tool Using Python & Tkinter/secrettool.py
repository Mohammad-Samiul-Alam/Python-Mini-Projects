
import tkinter as tk
from tkinter import messagebox
import base64


# ==========================================
# CLASS: Secret Message Encryption Tool
# ==========================================
class SecretMessageTool:

    # ======================================
    # CONSTRUCTOR
    # ======================================
    def __init__(self, root):

        self.root = root

        self.root.title("Secret Message Encryption Tool")
        self.root.geometry("600x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")

        # Create GUI components
        self.create_widgets()

    # ======================================
    # CREATE GUI COMPONENTS
    # ======================================
    def create_widgets(self):

        # Title
        self.title_label = tk.Label(
            self.root,
            text="🔐 Secret Message Tool",
            font=("Arial", 22, "bold"),
            bg="#1e1e1e",
            fg="white"
        )
        self.title_label.pack(pady=20)

        # Message Label
        self.message_label = tk.Label(
            self.root,
            text="Enter Message:",
            font=("Arial", 12, "bold"),
            bg="#1e1e1e",
            fg="white"
        )
        self.message_label.pack(anchor="w", padx=40)

        # Message Text Box
        self.message_entry = tk.Text(
            self.root,
            height=6,
            width=60,
            font=("Arial", 12)
        )
        self.message_entry.pack(pady=8)

        # Secret Key Label
        self.key_label = tk.Label(
            self.root,
            text="Secret Key:",
            font=("Arial", 12, "bold"),
            bg="#1e1e1e",
            fg="white"
        )
        self.key_label.pack(anchor="w", padx=40)

        # Secret Key Entry
        self.key_entry = tk.Entry(
            self.root,
            width=45,
            font=("Arial", 12),
            show="*"
        )
        self.key_entry.pack(pady=8)

        # Button Frame
        self.button_frame = tk.Frame(
            self.root,
            bg="#1e1e1e"
        )
        self.button_frame.pack(pady=15)

        # Encrypt Button
        self.encrypt_button = tk.Button(
            self.button_frame,
            text="🔐 Encrypt",
            font=("Arial", 12, "bold"),
            width=12,
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            command=self.encrypt_message
        )
        self.encrypt_button.grid(
            row=0, column=0, padx=8
        )

        # Decrypt Button
        self.decrypt_button = tk.Button(
            self.button_frame,
            text="🔓 Decrypt",
            font=("Arial", 12, "bold"),
            width=12,
            bg="#2196F3",
            fg="white",
            activebackground="#1976D2",
            command=self.decrypt_message
        )
        self.decrypt_button.grid(
            row=0, column=1, padx=8
        )

        # Clear Button
        self.clear_button = tk.Button(
            self.button_frame,
            text="Clear",
            font=("Arial", 12, "bold"),
            width=12,
            bg="#f44336",
            fg="white",
            activebackground="#d32f2f",
            command=self.clear_all
        )
        self.clear_button.grid(
            row=0, column=2, padx=8
        )

        # Result Label
        self.result_label = tk.Label(
            self.root,
            text="Result:",
            font=("Arial", 12, "bold"),
            bg="#1e1e1e",
            fg="white"
        )
        self.result_label.pack(
            anchor="w", padx=40
        )

        # Result Text Box
        self.result_entry = tk.Text(
            self.root,
            height=6,
            width=60,
            font=("Arial", 12)
        )
        self.result_entry.pack(pady=8)

    # ======================================
    # ENCRYPTION METHOD
    # ======================================
    def encrypt_message(self):

        # Get message and secret key
        message = self.message_entry.get(
            "1.0", tk.END
        ).strip() # শুরু ও শেষের whitespace সরায় - Remove leading and trailing whitespace

        key = self.key_entry.get()

        # Validate input
        if message == "" or key == "":
            messagebox.showwarning(
                "Warning",
                "Enter message and secret key!"
            )
            return

        # Convert message into bytes
        message_bytes = message.encode("utf-8")

        # Encode message using Base64
        encrypted = base64.b64encode(
            message_bytes
        ).decode("utf-8")

        # Display result
        self.result_entry.delete(
            "1.0", tk.END
        )

        self.result_entry.insert(
            tk.END, encrypted
        )

    # ======================================
    # DECRYPTION METHOD
    # ======================================
    def decrypt_message(self):

        # Get encrypted message and key
        encrypted_message = self.message_entry.get(
            "1.0", tk.END
        ).strip()

        key = self.key_entry.get()

        # Validate input
        if encrypted_message == "" or key == "":
            messagebox.showwarning(
                "Warning",
                "Enter encrypted message and secret key!"
            )
            return

        try:
            # Decode Base64
            decrypted = base64.b64decode(
                encrypted_message.encode("utf-8"),
                validate=True
            ).decode("utf-8")

            # Display decrypted message
            self.result_entry.delete(
                "1.0", tk.END
            )

            self.result_entry.insert(
                tk.END, decrypted
            )

        except Exception:
            messagebox.showerror(
                "Error",
                "Invalid encrypted message!"
            )

    # ======================================
    # CLEAR METHOD
    # ======================================
    def clear_all(self):

        # Clear message box
        self.message_entry.delete(
            "1.0", tk.END
        )

        # Clear secret key
        self.key_entry.delete(
            0, tk.END
        )

        # Clear result box
        self.result_entry.delete(
            "1.0", tk.END
        )


# ==========================================
# MAIN PROGRAM
# ==========================================
if __name__ == "__main__":

    # Create main window
    root = tk.Tk()

    # Create object of the class
    app = SecretMessageTool(root)

    # Run application
    root.mainloop()
