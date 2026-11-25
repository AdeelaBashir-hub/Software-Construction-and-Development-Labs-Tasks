
import tkinter as tk
from tkinter import messagebox

# Custom Exceptions
class TooHotCoffeeCupException(Exception):
    pass

class TooColdCoffeeCupException(Exception):
    pass

# Main Function
def check_temperature():

    try:
        temperature = float(temp_entry.get())

        if temperature >= 85:
            raise TooHotCoffeeCupException(
                "Too Hot Coffee Cup Exception!"
            )

        elif temperature <= 65:
            raise TooColdCoffeeCupException(
                "Too Cold Coffee Cup Exception!"
            )

        else:
            result_label.config(
                text="✓ Coffee Served Successfully!\nTemperature is Normal.",
                fg="#2E8B57"
            )

    except TooHotCoffeeCupException as e:
        result_label.config(
            text=str(e),
            fg="#D32F2F"
        )

    except TooColdCoffeeCupException as e:
        result_label.config(
            text=str(e),
            fg="#1976D2"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid temperature!"
        )

# Main Window
root = tk.Tk()
root.title("Coffee Temperature Checker")
root.geometry("550x450")
root.configure(bg="#3E2723")
root.resizable(False, False)

# Heading
heading = tk.Label(
    root,
    text="☕ COFFEE TEMPERATURE CHECKER",
    font=("Arial", 19, "bold"),
    bg="#3E2723",
    fg="#FFCC80"
)
heading.pack(pady=30)

# Instruction
instruction = tk.Label(
    root,
    text="Enter Coffee Temperature (°C)",
    font=("Arial", 13),
    bg="#3E2723",
    fg="#FFF3E0"
)
instruction.pack(pady=10)

# Input Box
temp_entry = tk.Entry(
    root,
    font=("Arial", 18),
    justify="center",
    width=18,
    bg="#FFF8E1",
    fg="#3E2723"
)
temp_entry.pack(pady=10)

# Button
check_button = tk.Button(
    root,
    text="CHECK TEMPERATURE",
    font=("Arial", 12, "bold"),
    bg="#FF9800",
    fg="#FFFFFF",
    activebackground="#FFB74D",
    command=check_temperature,
    width=22,
    height=2,
    cursor="hand2"
)
check_button.pack(pady=20)

# Result
result_label = tk.Label(
    root,
    text="Waiting for Temperature...",
    font=("Arial", 13, "bold"),
    bg="#3E2723",
    fg="#FFF3E0",
    wraplength=450
)
result_label.pack(pady=20)

# Footer
footer = tk.Label(
    root,
    text="Standard Temperature: 66°C - 84°C",
    font=("Arial", 10),
    bg="#3E2723",
    fg="#BCAAA4"
)
footer.pack(pady=10)

root.mainloop()
