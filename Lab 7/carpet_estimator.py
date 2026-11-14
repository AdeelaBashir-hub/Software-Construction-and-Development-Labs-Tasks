import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import random

SHOP_NAME = "Adeela's Wooven Dreams"
CARPET_PRICES = {          # Rs. per square foot
    "Nylon": 120,
    "Polyester": 180,
    "Wool": 350,
    "Silk": 600,
}
TAX_LIMIT = 30000
LOW_TAX = 0.10
HIGH_TAX = 0.15


class CarpetEstimator:
    def __init__(self, root):
        self.root = root
        root.title("Carpet Cost Estimator")
        root.resizable(False, False)
        root.configure(bg="#f4f1ea")

        self.result = None   # stores the last calculation

        # ---------- variables ----------
        self.name_var = tk.StringVar()
        self.length_var = tk.StringVar()
        self.width_var = tk.StringVar()
        self.type_var = tk.StringVar()

        # any change to the inputs makes the old result invalid
        for v in (self.name_var, self.length_var, self.width_var, self.type_var):
            v.trace_add("write", self.invalidate)

        # ---------- header ----------
        tk.Label(root, text=SHOP_NAME, font=("Segoe UI", 18, "bold"),
                 bg="#5b3a29", fg="white", pady=10).grid(
            row=0, column=0, columnspan=2, sticky="nsew")

        # ---------- input form ----------
        form = tk.Frame(root, bg="#f4f1ea", padx=20, pady=15)
        form.grid(row=1, column=0, columnspan=2)

        labels = ["Customer Name:", "Room Length (ft):",
                  "Room Width (ft):", "Carpet Type:"]
        for i, text in enumerate(labels):
            tk.Label(form, text=text, font=("Segoe UI", 11),
                     bg="#f4f1ea").grid(row=i, column=0, sticky="w", pady=6)

        tk.Entry(form, textvariable=self.name_var, width=24,
                 font=("Segoe UI", 11)).grid(row=0, column=1, pady=6)
        tk.Entry(form, textvariable=self.length_var, width=24,
                 font=("Segoe UI", 11)).grid(row=1, column=1, pady=6)
        tk.Entry(form, textvariable=self.width_var, width=24,
                 font=("Segoe UI", 11)).grid(row=2, column=1, pady=6)

        combo = ttk.Combobox(form, textvariable=self.type_var, width=22,
                             font=("Segoe UI", 11), state="readonly",
                             values=[f"{k}  (Rs. {v}/sq ft)"
                                     for k, v in CARPET_PRICES.items()])
        combo.grid(row=3, column=1, pady=6)
        combo.current(0)

        # ---------- buttons ----------
        btns = tk.Frame(root, bg="#f4f1ea")
        btns.grid(row=2, column=0, columnspan=2, pady=5)

        tk.Button(btns, text="Calculate", width=12, bg="#5b3a29", fg="white",
                  font=("Segoe UI", 10, "bold"),
                  command=self.calculate).grid(row=0, column=0, padx=5)
        self.invoice_btn = tk.Button(btns, text="Generate Invoice", width=16,
                                     font=("Segoe UI", 10, "bold"),
                                     state="disabled",
                                     command=self.show_invoice)
        self.invoice_btn.grid(row=0, column=1, padx=5)
        tk.Button(btns, text="Clear", width=10,
                  font=("Segoe UI", 10, "bold"),
                  command=self.clear).grid(row=0, column=2, padx=5)

        # ---------- results ----------
        res = tk.LabelFrame(root, text=" Cost Summary ", bg="#f4f1ea",
                            font=("Segoe UI", 10, "bold"), padx=20, pady=10)
        res.grid(row=3, column=0, columnspan=2, padx=20, pady=15, sticky="ew")

        self.out = {}
        for i, key in enumerate(["Area", "Subtotal", "Tax", "Final Cost"]):
            tk.Label(res, text=key + ":", font=("Segoe UI", 11),
                     bg="#f4f1ea").grid(row=i, column=0, sticky="w", pady=3)
            lbl = tk.Label(res, text="-", font=("Segoe UI", 11, "bold"),
                           bg="#f4f1ea", width=22, anchor="e")
            lbl.grid(row=i, column=1, sticky="e")
            self.out[key] = lbl

    # ---------- logic ----------
    def money(self, x):
        return f"Rs. {x:,.2f}"

    def invalidate(self, *args):
        """Inputs changed -> old result is no longer valid."""
        self.result = None
        self.invoice_btn.config(state="disabled")

    def calculate(self):
        try:
            length = float(self.length_var.get())
            width = float(self.width_var.get())
        except ValueError:
            messagebox.showerror("Invalid Input",
                                 "Please enter numbers for length and width.")
            return
        if length <= 0 or width <= 0:
            messagebox.showerror("Invalid Input",
                                 "Length and width must be greater than zero.")
            return

        carpet = self.type_var.get().split("  ")[0]
        price = CARPET_PRICES[carpet]

        area = length * width
        subtotal = area * price
        tax_rate = LOW_TAX if subtotal < TAX_LIMIT else HIGH_TAX
        tax = subtotal * tax_rate
        total = subtotal + tax

        self.result = dict(carpet=carpet, price=price, length=length,
                           width=width, area=area, subtotal=subtotal,
                           tax_rate=tax_rate, tax=tax, total=total)

        self.out["Area"].config(text=f"{area:,.2f} sq ft")
        self.out["Subtotal"].config(text=self.money(subtotal))
        self.out["Tax"].config(text=f"{self.money(tax)} ({tax_rate*100:.0f}%)")
        self.out["Final Cost"].config(text=self.money(total))

        # invalidate() ran when typing; re-enable only after a good calculation
        self.invoice_btn.config(state="normal")

    def clear(self):
        self.name_var.set("")
        self.length_var.set("")
        self.width_var.set("")
        for lbl in self.out.values():
            lbl.config(text="-")
        self.result = None
        self.invoice_btn.config(state="disabled")

    # ---------- invoice ----------
    def build_invoice_text(self):
        r = self.result
        w = 46
        name = self.name_var.get().strip() or "Walk-in Customer"
        inv_no = f"INV-{random.randint(1000, 9999)}"
        date = datetime.now().strftime("%d-%m-%Y  %H:%M")

        def row(label, value):
            return f"{label:<16}: {value}"

        lines = [
            "=" * w,
            SHOP_NAME.upper().center(w),
            "SALES INVOICE".center(w),
            "=" * w,
            row("Invoice No", inv_no),
            row("Date", date),
            row("Customer", name),
            "-" * w,
            row("Carpet Type", r["carpet"]),
            row("Room Length", f"{r['length']:.2f} ft"),
            row("Room Width", f"{r['width']:.2f} ft"),
            row("Area", f"{r['area']:,.2f} sq ft"),
            row("Rate", f"{self.money(r['price'])} / sq ft"),
            "-" * w,
            row("Subtotal", self.money(r["subtotal"])),
            row(f"Tax ({r['tax_rate']*100:.0f}%)", self.money(r["tax"])),
            "-" * w,
            row("TOTAL", self.money(r["total"])),
            "=" * w,
            "Thank you for shopping with us!".center(w),
        ]
        return "\n".join(lines)

    def show_invoice(self):
        if self.result is None:
            return
        text = self.build_invoice_text()

        win = tk.Toplevel(self.root)
        win.title("Invoice")
        win.configure(bg="white")

        box = tk.Text(win, font=("Courier New", 11), width=48, height=21,
                      bd=0, padx=15, pady=15)
        box.insert("1.0", text)
        box.config(state="disabled")
        box.pack()

        def save():
            path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text file", "*.txt")],
                initialfile="invoice.txt")
            if path:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(text)
                messagebox.showinfo("Saved", "Invoice saved successfully.")

        tk.Button(win, text="Save Invoice", command=save, bg="#5b3a29",
                  fg="white", font=("Segoe UI", 10, "bold")).pack(pady=8)


if __name__ == "__main__":
    root = tk.Tk()
    CarpetEstimator(root)
    root.mainloop()