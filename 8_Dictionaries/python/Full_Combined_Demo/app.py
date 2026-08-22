import tkinter as tk
from tkinter import ttk


class DictionaryDemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dictionary Data Structure Demo")
        self.root.geometry("720x460")

        notebook = ttk.Notebook(root)
        notebook.pack(expand=True, fill="both")

        self.collector_tab = ttk.Frame(notebook)
        self.compare_tab = ttk.Frame(notebook)
        self.username_tab = ttk.Frame(notebook)
        self.word_tab = ttk.Frame(notebook)

        notebook.add(self.collector_tab, text="Key/Value Collector")
        notebook.add(self.compare_tab, text="Dictionary Compare")
        notebook.add(self.username_tab, text="Username Directory")
        notebook.add(self.word_tab, text="Word Frequency")

        self.create_collector_tab()
        self.create_compare_tab()
        self.create_username_tab()
        self.create_word_tab()

    def create_collector_tab(self):
        self.items = {}

        tk.Label(self.collector_tab, text="Key:").pack(pady=3)
        self.collector_key = tk.Entry(self.collector_tab, width=35)
        self.collector_key.pack(pady=3)

        tk.Label(self.collector_tab, text="Value:").pack(pady=3)
        self.collector_value = tk.Entry(self.collector_tab, width=35)
        self.collector_value.pack(pady=3)

        tk.Button(self.collector_tab, text="Add / Update", command=self.add_collector_item).pack(pady=6)
        self.collector_display = tk.Label(self.collector_tab, text="Items: {}", font=("Arial", 12))
        self.collector_display.pack(pady=10)

    def add_collector_item(self):
        key = self.collector_key.get().strip()
        value = self.collector_value.get().strip()
        if not key:
            return

        self.items[key] = value
        self.collector_key.delete(0, tk.END)
        self.collector_value.delete(0, tk.END)
        pretty = ", ".join(f"{k}: {self.items[k]}" for k in sorted(self.items))
        self.collector_display.config(text=f"Items: {{{pretty}}}")

    def create_compare_tab(self):
        tk.Label(self.compare_tab, text="Dictionary A (key:value, comma-separated):").pack()
        self.entry_a = tk.Entry(self.compare_tab, width=65)
        self.entry_a.pack(pady=5)

        tk.Label(self.compare_tab, text="Dictionary B (key:value, comma-separated):").pack()
        self.entry_b = tk.Entry(self.compare_tab, width=65)
        self.entry_b.pack(pady=5)

        tk.Button(self.compare_tab, text="Compare", command=self.compare_dicts).pack(pady=10)
        self.compare_result = tk.Label(self.compare_tab, text="", justify="left", font=("Arial", 12))
        self.compare_result.pack(pady=10)

    def _parse_dict(self, raw_text):
        out = {}
        chunks = [part.strip() for part in raw_text.split(",") if part.strip()]
        for chunk in chunks:
            if ":" not in chunk:
                continue
            key, value = chunk.split(":", 1)
            out[key.strip()] = value.strip()
        return out

    def compare_dicts(self):
        a = self._parse_dict(self.entry_a.get())
        b = self._parse_dict(self.entry_b.get())

        keys_a = set(a.keys())
        keys_b = set(b.keys())

        only_a = {k: a[k] for k in keys_a - keys_b}
        only_b = {k: b[k] for k in keys_b - keys_a}
        shared = keys_a & keys_b
        same_values = {k: a[k] for k in shared if a[k] == b[k]}
        different_values = {k: (a[k], b[k]) for k in shared if a[k] != b[k]}

        self.compare_result.config(
            text=(
                f"Only in A: {only_a}\n"
                f"Only in B: {only_b}\n"
                f"Shared with same value: {same_values}\n"
                f"Shared with different values (A, B): {different_values}"
            )
        )

    def create_username_tab(self):
        self.users = {
            "alice": {"active": True, "role": "admin"},
            "bob": {"active": True, "role": "editor"},
            "charlie": {"active": False, "role": "viewer"},
        }

        tk.Label(self.username_tab, text="Enter username:").pack(pady=5)
        self.username_entry = tk.Entry(self.username_tab, width=30)
        self.username_entry.pack(pady=5)
        tk.Button(self.username_tab, text="Check", command=self.check_username).pack(pady=5)

        self.username_result = tk.Label(self.username_tab, text="", font=("Arial", 12))
        self.username_result.pack(pady=10)

    def check_username(self):
        username = self.username_entry.get().strip().lower()
        if username in self.users:
            info = self.users[username]
            status = "active" if info["active"] else "inactive"
            self.username_result.config(
                text=f"User exists: role={info['role']}, status={status}",
                fg="green",
            )
        else:
            self.username_result.config(text="Username not found", fg="red")

    def create_word_tab(self):
        tk.Label(self.word_tab, text="Paste text below:").pack()
        self.text_area = tk.Text(self.word_tab, height=10, width=60)
        self.text_area.pack(pady=5)
        tk.Button(self.word_tab, text="Count Words", command=self.count_words).pack(pady=5)
        self.word_result = tk.Label(self.word_tab, text="", justify="left", font=("Arial", 12))
        self.word_result.pack(pady=10)

    def count_words(self):
        text = self.text_area.get("1.0", tk.END).strip().lower()
        counts = {}
        for word in text.split():
            counts[word] = counts.get(word, 0) + 1

        if not counts:
            self.word_result.config(text="No words found")
            return

        ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
        lines = [f"{word}: {count}" for word, count in ordered[:20]]
        self.word_result.config(text="Word Frequency:\n" + "\n".join(lines))


if __name__ == "__main__":
    root = tk.Tk()
    app = DictionaryDemoApp(root)
    root.mainloop()
