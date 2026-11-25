
import tkinter as tk
from tkinter import ttk, messagebox

# Custom Exceptions
class LowHemoglobinException(Exception):
    pass

class HighHemoglobinException(Exception):
    pass

# Check Hemoglobin Function
def check_hemoglobin():

    try:
        category = patient_var.get()
        hb = float(hb_entry.get())

        if category == "":
            messagebox.showwarning(
                "Missing Information",
                "Please select patient category!"
            )
            return

        # Simplified educational ranges (g/dL)
        if category == "Men":
            minimum = 13.5
            maximum = 17.5

        elif category == "Women":
            minimum = 12.0
            maximum = 15.5

        else:
            minimum = 11.0
            maximum = 16.0

        if hb < minimum:
            raise LowHemoglobinException(
                "Low Hemoglobin Level!"
            )

        elif hb > maximum:
            raise HighHemoglobinException(
                "High Hemoglobin Level!"
            )

        else:
            result_label.config(
                text="✓ Hemoglobin Level is NORMAL!",
                fg="#00897B"
            )

        range_label.config(
            text=f"Normal Range: {minimum} - {maximum} g/dL"
        )

    except LowHemoglobinException as e:
        result_label.config(
            text=str(e),
            fg="#E53935"
        )

    except HighHemoglobinException as e:
        result_label.config(
            text=str(e),
            fg="#E53935"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid Hb level!"
        )

# Main Window
root = tk.Tk()
root.title("Hemoglobin Level Checker")
root.geometry("600x520")
root.configure(bg="#004D40")
root.resizable(False, False)

# Heading
heading = tk.Label(
    root,
    text="HEMOGLOBIN LEVEL CHECKER",
    font=("Arial", 21, "bold"),
    bg="#004D40",
    fg="#80CBC4"
)
heading.pack(pady=30)

# Patient Category
category_label = tk.Label(
    root,
    text="Select Patient Category",
    font=("Arial", 13, "bold"),
    bg="#004D40",
    fg="white"
)
category_label.pack(pady=10)

patient_var = tk.StringVar()

category_box = ttk.Combobox(
    root,
    textvariable=patient_var,
    values=["Men", "Women", "Children"],
    font=("Arial", 12),
    state="readonly",
    width=25
)
category_box.pack(pady=8)

# Hb Input
hb_label = tk.Label(
    root,
    text="Enter Hemoglobin Level (g/dL)",
    font=("Arial", 13, "bold"),
    bg="#004D40",
    fg="white"
)
hb_label.pack(pady=15)

hb_entry = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center",
    width=20,
    bg="#E0F2F1",
    fg="#004D40"
)
hb_entry.pack(pady=8)

# Check Button
check_button = tk.Button(
    root,
    text="CHECK Hb LEVEL",
    font=("Arial", 12, "bold"),
    bg="#00BFA5",
    fg="#FFFFFF",
    activebackground="#4DB6AC",
    command=check_hemoglobin,
    width=22,
    height=2,
    cursor="hand2"
)
check_button.pack(pady=25)

# Normal Range
range_label = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    bg="#004D40",
    fg="#B2DFDB"
)
range_label.pack(pady=5)

# Result
result_label = tk.Label(
    root,
    text="Waiting for Patient Information...",
    font=("Arial", 13, "bold"),
    bg="#004D40",
    fg="white"
)
result_label.pack(pady=20)

# Footer
footer = tk.Label(
    root,
    text="Exception Handling - Lab 08",
    font=("Arial", 10),
    bg="#004D40",
    fg="#80CBC4"
)
footer.pack(pady=10)

root.mainloop()


