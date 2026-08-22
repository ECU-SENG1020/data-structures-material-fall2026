import tkinter as tk

class UniqueItemCollector:
    def __init__(self, root):
        self.root = root
        self.root.title("Unique Item Collector")

        self.items = set()

        # Entry and Button
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.pack(pady=5)

        # Display area
        self.display_label = tk.Label(root, text="Items: {}", font=("Arial", 12))
        self.display_label.pack(pady=10)

    def add_item(self):
        item = self.entry.get().strip()
        if item:
            self.items.add(item)
            self.entry.delete(0, tk.END)
            self.display_label.config(text=f"Items: {', '.join(self.items)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UniqueItemCollector(root)
    root.mainloop()