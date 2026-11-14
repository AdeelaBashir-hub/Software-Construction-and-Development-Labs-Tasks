import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")
        root.resizable(False, False)

        self.display = tk.StringVar(value="0")
        self.first = None
        self.op = None
        self.new_entry = True

        entry = tk.Entry(root, textvariable=self.display, justify="right",
                         font=("Segoe UI", 18), state="readonly",
                         readonlybackground="white", bd=2, relief="groove")
        entry.grid(row=0, column=0, columnspan=5, sticky="nsew",
                   padx=5, pady=5, ipady=8)

        # (text, row, col, rowspan, colspan, command)
        layout = [
            ("7", 1, 0, 1, 1, lambda: self.digit("7")),
            ("8", 1, 1, 1, 1, lambda: self.digit("8")),
            ("9", 1, 2, 1, 1, lambda: self.digit("9")),
            ("/", 1, 3, 1, 1, lambda: self.operator("/")),
            ("CE", 1, 4, 1, 1, self.clear_entry),

            ("4", 2, 0, 1, 1, lambda: self.digit("4")),
            ("5", 2, 1, 1, 1, lambda: self.digit("5")),
            ("6", 2, 2, 1, 1, lambda: self.digit("6")),
            ("*", 2, 3, 1, 1, lambda: self.operator("*")),
            ("C", 2, 4, 1, 1, self.clear_all),

            ("1", 3, 0, 1, 1, lambda: self.digit("1")),
            ("2", 3, 1, 1, 1, lambda: self.digit("2")),
            ("3", 3, 2, 1, 1, lambda: self.digit("3")),
            ("-", 3, 3, 1, 1, lambda: self.operator("-")),
            ("=", 3, 4, 2, 1, self.equals),

            ("0", 4, 0, 1, 2, lambda: self.digit("0")),
            (".", 4, 2, 1, 1, self.dot),
            ("+", 4, 3, 1, 1, lambda: self.operator("+")),
        ]

        for text, r, c, rs, cs, cmd in layout:
            tk.Button(root, text=text, font=("Segoe UI", 12), width=4, height=2,
                      command=cmd).grid(row=r, column=c, rowspan=rs,
                                        columnspan=cs, sticky="nsew",
                                        padx=2, pady=2)

    # ---------- helpers ----------
    def fmt(self, num):
        return str(int(num)) if num == int(num) else str(round(num, 10))

    # ---------- handlers ----------
    def digit(self, d):
        if self.new_entry or self.display.get() in ("0", "Error"):
            self.display.set(d)
            self.new_entry = False
        else:
            self.display.set(self.display.get() + d)

    def dot(self):
        if self.new_entry or self.display.get() == "Error":
            self.display.set("0.")
            self.new_entry = False
        elif "." not in self.display.get():
            self.display.set(self.display.get() + ".")

    def operator(self, o):
        if self.display.get() == "Error":
            return
        if self.op and not self.new_entry:
            self.equals()          # chain: 2 + 3 + ... works
            if self.display.get() == "Error":
                return
        self.first = float(self.display.get())
        self.op = o
        self.new_entry = True

    def equals(self):
        if self.op is None or self.new_entry and self.first is None:
            return
        second = float(self.display.get())
        try:
            if self.op == "+":
                result = self.first + second
            elif self.op == "-":
                result = self.first - second
            elif self.op == "*":
                result = self.first * second
            else:
                result = self.first / second
            self.display.set(self.fmt(result))
        except ZeroDivisionError:
            self.display.set("Error")
        self.first = None
        self.op = None
        self.new_entry = True

    def clear_entry(self):          # CE: clears current number only
        self.display.set("0")
        self.new_entry = True

    def clear_all(self):            # C: resets everything
        self.display.set("0")
        self.first = None
        self.op = None
        self.new_entry = True


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()