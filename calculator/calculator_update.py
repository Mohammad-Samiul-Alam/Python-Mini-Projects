import tkinter as tk

# calculator class
class Calculator:
    def __init__(self, root):
        self.root = root
        # window setting
        self._window_setting()

        # create variable for entry
        # self.display = tk.StringVar(value="0")


        # create entry
        self.entry = tk.Entry(
            self.root,
            justify="right",
            font=("Arial", 24),
            bd=0,
            # User cannot directly type into Entry
            # state="readonly",
            # Background when readonly
            # readonlybackground="red",
            fg="#ffffff",
            bg="#161616"
        )
        self.entry.pack(
            fill="both",
            padx=(5, 5),
            pady=(20, 20)
        )
        # prevent direct typing
        self.entry.bind("<Key>", self.block_keys)

        self.create_buttons()

        # create clear button
        self.button = tk.Button(
            self.root,
            text="Clear",
            font=("Arial", 24),
            # Remove default border
            bd=0,
            bg="red",
            fg="white",
            activebackground="yellow",
            activeforeground="black",
            command=self.clear
        )
        self.button.pack(
            fill="both",
            padx=5,
            pady=5
        )

    # set window properties
    def _window_setting(self):
        self.root.title("calculator")
        self.root.geometry("500x500")
        self.root.configure(bg = "#141524")
    # block keyword typing
    def block_keys(self, event):
        return "break"
    
    # clear entry
    # def clear(self):
    #     self.display.set("0")
    

    # Function: clear the entry
    def click(self, value):
        self.entry.insert(tk.END, value)
    def clear(self):
        self.entry.delete("0", tk.END)
    # calculate result
    def calculate(self):
        try:
            result = eval(
                self.entry.get(),
                {"__builtins__": {}},
                {}
            )
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
        except ZeroDivisionError:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "div by 0")
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
    # Create calculator buttons
    def create_buttons(self):
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", "-"]
        ]
        for rows in buttons:
            # create frames
            frame = tk.Frame(
                self.root,           
            )
            frame.pack(
                fill="both",
                expand=True
            )
            for btn in rows:
                if(btn == "="):
                    command = self.calculate
                else:
                    command = lambda x=btn: self.click(x)
                # create button
                tk.Button(
                    frame,
                    text=btn,
                    font=("Arial", 24),
                    command=command
                ).pack(
                    fill='both',
                    padx=5,
                    pady = 5,
                    side="left",
                    expand=True
                )


if __name__ == "__main__":
    # create main window
    root = tk.Tk()
    # create calculator object
    calculator = Calculator(root)
    # start application
    root.mainloop()
