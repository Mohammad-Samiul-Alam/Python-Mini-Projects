import tkinter as tk

def click(value):
    entry.insert(tk.END, value)
def clear():
    entry.delete(0, tk.END)
def calculate():
    try:
        result = eval(entry.get(), {"__builtins__": {}}, {})
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "div by zero")
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
# block typing in entry(button only)
def block_keys(event):
    return "break"
# create window
root = tk.Tk()
# set window
root.title("calculator")
root.geometry("500x500")

# create widget
entry = tk.Entry(
    root,
    font=("Arial", 24)
)
entry.pack(
    fill="both",
    padx=5,
    pady=5
)
# prevent typing directly into the entry
entry.bind("<Key>", block_keys)
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", "-"]
]
for rows in buttons:
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)
    for btn in rows:
        if(btn == "="):
            command = calculate
        else:
            command = lambda x = btn: click(x)
        tk.Button(
            frame,
            text = btn,
            font = ("Arial", 24),
            command= command
        ).pack(
            fill="both",
            side="left",
            padx=5,
            pady=5,
            expand=True
        )
tk.Button(
    root,
    text="Clear",
    font=("Arial", 18),
    bg="red",
    fg="white",
    activebackground="green",
    activeforeground="yellow",
    command=clear
).pack(
    fill="both",
    padx=5,
    pady=5
)
root.mainloop()