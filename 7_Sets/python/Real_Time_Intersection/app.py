import tkinter as tk

class SetOperationsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Set Operations Demo")

        # Input fields
        tk.Label(root, text="Set A (comma-separated):").pack()
        self.entry_a = tk.Entry(root, width=40)
        self.entry_a.pack(pady=5)

        tk.Label(root, text="Set B (comma-separated):").pack()
        self.entry_b = tk.Entry(root, width=40)
        self.entry_b.pack(pady=5)

        # Button
        self.compare_button = tk.Button(root, text="Compare Sets", command=self.compare_sets)
        self.compare_button.pack(pady=10)

        # Results
        self.result_label = tk.Label(root, text="", justify="left", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def compare_sets(self):
        set_a = set(self.entry_a.get().split(","))
        set_b = set(self.entry_b.get().split(","))

        union = set_a | set_b
        intersection = set_a & set_b
        difference = set_a - set_b
        symmetric_difference = set_a ^ set_b

        result_text = (
            f"Union: {union}\n"
            f"Intersection: {intersection}\n"
            f"Difference (A - B): {difference}\n"
            f"Symmetric Difference: {symmetric_difference}"
        )
        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = SetOperationsApp(root)
    root.mainloop()