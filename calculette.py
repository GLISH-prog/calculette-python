import tkinter as tk

# Fonction pour ajouter un caractère
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Fonction pour calculer
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Fonction clear
def clear():
    entry.delete(0, tk.END)

# Fenêtre principale
window = tk.Tk()
window.title("Calculator")
window.geometry("300x350")

# Zone affichage
entry = tk.Entry(window, font=("Arial", 20), justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, pady=10)

# Frame boutons
frame = tk.Frame(window)
frame.pack()

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+","%"
]

row = 0
col = 0

for button in buttons:

    if button == "=":
        action = calculate
    else:
        action = lambda x=button: click(x)

    tk.Button(frame, text=button, width=5, height=2,
              command=action).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Bouton clear
tk.Button(window, text="Clear", command=clear).pack(fill="both")

window.mainloop()
