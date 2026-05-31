import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from src.analyzer import StudentResultAnalyzer


class ResultAnalyzerGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Analyzer")
        self.root.geometry("1000x600")
        self.root.configure(bg="#1e1e1e")

        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background="#2d2d2d",
            foreground="white",
            fieldbackground="#2d2d2d",
            rowheight=25
        )

        style.configure(
            "Treeview.Heading",
            background="#3a3a3a",
            foreground="white",
            font=("Segoe UI", 10, "bold")
        )

        style.configure(
            "Dark.TButton",
            background="#0078D7",
            foreground="white",
            font=("Segoe UI", 10)
        )

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="📊 Student Result Analyzer",
            bg="#1e1e1e",
            fg="white",
            font=("Segoe UI", 18, "bold")
        )
        title.pack(pady=15)

        btn_frame = tk.Frame(self.root, bg="#1e1e1e")
        btn_frame.pack()

        ttk.Button(
            btn_frame,
            text="Load CSV",
            command=self.load_csv,
            style="Dark.TButton"
        ).pack(side=tk.LEFT, padx=10)

        ttk.Button(
            btn_frame,
            text="Analyze",
            command=self.analyze,
            style="Dark.TButton"
        ).pack(side=tk.LEFT, padx=10)

        self.stats_label = tk.Label(
            self.root,
            text="",
            bg="#1e1e1e",
            fg="#00ff99",
            font=("Segoe UI", 11)
        )
        self.stats_label.pack(pady=10)

        self.tree = ttk.Treeview(self.root)
        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

        self.file_path = None

    def load_csv(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")]
        )

        if self.file_path:
            messagebox.showinfo(
                "Success",
                "CSV Loaded Successfully"
            )

    def analyze(self):

        if not self.file_path:
            messagebox.showerror(
                "Error",
                "Please load a CSV file first"
            )
            return

        analyzer = StudentResultAnalyzer(self.file_path)
        df = analyzer.process()

        self.tree.delete(*self.tree.get_children())

        self.tree["columns"] = list(df.columns)
        self.tree["show"] = "headings"

        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        for _, row in df.iterrows():
            self.tree.insert(
                "",
                tk.END,
                values=list(row)
            )

        stats = analyzer.class_statistics()

        self.stats_label.config(
            text=f"Average: {stats['Average Score']:.2f}%   |   "
                 f"Highest: {stats['Highest Score']:.2f}%   |   "
                 f"Lowest: {stats['Lowest Score']:.2f}%"
        )