import tkinter as tk


class DictionaryCompareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dictionary Compare Demo")

        tk.Label(root, text="Dictionary A (key:value, comma-separated):").pack()
        self.entry_a = tk.Entry(root, width=60)
        self.entry_a.pack(pady=5)

        tk.Label(root, text="Dictionary B (key:value, comma-separated):").pack()
        self.entry_b = tk.Entry(root, width=60)
        self.entry_b.pack(pady=5)

        self.compare_button = tk.Button(root, text="Compare Dictionaries", command=self.compare)
        self.compare_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", justify="left", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def _parse_dict(self, raw_text):
        out = {}
        chunks = [part.strip() for part in raw_text.split(",") if part.strip()]
        for chunk in chunks:
            if ":" not in chunk:
                continue
            key, value = chunk.split(":", 1)
            out[key.strip()] = value.strip()
        return out

    def compare(self):
        a = self._parse_dict(self.entry_a.get())
        b = self._parse_dict(self.entry_b.get())

        keys_a = set(a.keys())
        keys_b = set(b.keys())

        only_a = {k: a[k] for k in keys_a - keys_b}
        only_b = {k: b[k] for k in keys_b - keys_a}

        shared_keys = keys_a & keys_b
        same_values = {k: a[k] for k in shared_keys if a[k] == b[k]}
        different_values = {k: (a[k], b[k]) for k in shared_keys if a[k] != b[k]}

        result_text = (
            f"Only in A: {only_a}\n"
            f"Only in B: {only_b}\n"
            f"Shared with same value: {same_values}\n"
            f"Shared with different values (A, B): {different_values}"
        )
        self.result_label.config(text=result_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = DictionaryCompareApp(root)
    root.mainloop()
