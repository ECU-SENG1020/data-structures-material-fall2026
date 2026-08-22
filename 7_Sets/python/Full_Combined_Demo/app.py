import tkinter as tk
from tkinter import ttk

class SetDemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Set Data Structure Demo")
        self.root.geometry("600x400")

        notebook = ttk.Notebook(root)
        notebook.pack(expand=True, fill="both")

        # Tabs
        self.unique_tab = ttk.Frame(notebook)
        self.intersection_tab = ttk.Frame(notebook)
        self.username_tab = ttk.Frame(notebook)
        self.word_tab = ttk.Frame(notebook)

        notebook.add(self.unique_tab, text="Unique Collector")
        notebook.add(self.intersection_tab, text="Set Operations")
        notebook.add(self.username_tab, text="Username Checker")
        notebook.add(self.word_tab, text="Word Filter")

        self.create_unique_tab()
        self.create_intersection_tab()
        self.create_username_tab()
        self.create_word_tab()

    # ---------------- Unique Collector ----------------
    def create_unique_tab(self):
        self.items = set()
        tk.Label(self.unique_tab, text="Enter item:").pack(pady=5)
        self.entry_unique = tk.Entry(self.unique_tab, width=30)
        self.entry_unique.pack(pady=5)
        tk.Button(self.unique_tab, text="Add", command=self.add_unique_item).pack(pady=5)
        self.unique_display = tk.Label(self.unique_tab, text="Items: {}", font=("Arial", 12))
        self.unique_display.pack(pady=10)

    def add_unique_item(self):
        item = self.entry_unique.get().strip()
        if not item:
            return

        norm = item.lower()
        if norm in self.items:
            # give user quick feedback and clear the entry
            self.unique_display.config(text=f"Items: {', '.join(sorted(self.items))} (\"{item}\" already present)")
            self.entry_unique.delete(0, tk.END)
            return

        self.items.add(item)
        self.entry_unique.delete(0, tk.END)
        # show a stable, sorted order so the display looks consistent
        self.unique_display.config(text=f"Items: {', '.join(sorted(self.items))}")

    # ---------------- Set Operations ----------------
    def create_intersection_tab(self):
        tk.Label(self.intersection_tab, text="Set A (comma-separated):").pack()
        self.entry_a = tk.Entry(self.intersection_tab, width=40)
        self.entry_a.pack(pady=5)

        tk.Label(self.intersection_tab, text="Set B (comma-separated):").pack()
        self.entry_b = tk.Entry(self.intersection_tab, width=40)
        self.entry_b.pack(pady=5)

        tk.Button(self.intersection_tab, text="Compare", command=self.compare_sets).pack(pady=10)
        self.result_label = tk.Label(self.intersection_tab, text="", justify="left", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def compare_sets(self):
        set_a = set(map(str.strip, self.entry_a.get().split(",")))
        set_b = set(map(str.strip, self.entry_b.get().split(",")))

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

    # ---------------- Username Checker ----------------
    def create_username_tab(self):
        self.existing_users = {"alice", "bob", "charlie"}
        tk.Label(self.username_tab, text="Enter username:").pack(pady=5)
        self.entry_username = tk.Entry(self.username_tab, width=30)
        self.entry_username.pack(pady=5)
        tk.Button(self.username_tab, text="Check", command=self.check_username).pack(pady=5)
        self.username_result = tk.Label(self.username_tab, text="", font=("Arial", 12))
        self.username_result.pack(pady=10)

    def check_username(self):
        username = self.entry_username.get().strip()
        if username in self.existing_users:
            self.username_result.config(text="Username already taken!", fg="red")
        else:
            self.username_result.config(text="Username available!", fg="green")

    # ---------------- Word Frequency Filter ----------------
    def create_word_tab(self):
        tk.Label(self.word_tab, text="Paste text below:").pack()
        self.text_area = tk.Text(self.word_tab, height=10, width=50)
        self.text_area.pack(pady=5)
        tk.Button(self.word_tab, text="Filter Unique Words", command=self.filter_words).pack(pady=5)
        self.word_result = tk.Label(self.word_tab, text="", justify="left", font=("Arial", 12))
        self.word_result.pack(pady=10)

    def filter_words(self):
        text = self.text_area.get("1.0", tk.END)
        words = set(text.split())
        self.word_result.config(text=f"Unique Words:\n{', '.join(words)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SetDemoApp(root)
    root.mainloop()