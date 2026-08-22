import tkinter as tk


class KeyValueCollector:
    def __init__(self, root):
        self.root = root
        self.root.title("Key/Value Collector")

        self.items = {}

        tk.Label(root, text="Key:").pack(pady=2)
        self.key_entry = tk.Entry(root, width=30)
        self.key_entry.pack(pady=4)

        tk.Label(root, text="Value:").pack(pady=2)
        self.value_entry = tk.Entry(root, width=30)
        self.value_entry.pack(pady=4)

        self.add_button = tk.Button(root, text="Add / Update", command=self.add_item)
        self.add_button.pack(pady=6)

        self.display_label = tk.Label(root, text="Items: {}", font=("Arial", 12), justify="left")
        self.display_label.pack(pady=10)

    def add_item(self):
        key = self.key_entry.get().strip()
        value = self.value_entry.get().strip()
        if not key:
            return

        self.items[key] = value
        self.key_entry.delete(0, tk.END)
        self.value_entry.delete(0, tk.END)

        pretty = ", ".join(f"{k}: {self.items[k]}" for k in sorted(self.items))
        self.display_label.config(text=f"Items: {{{pretty}}}")


if __name__ == "__main__":
    root = tk.Tk()
    app = KeyValueCollector(root)
    root.mainloop()
