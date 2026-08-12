import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
class NarrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Narration Tool")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.selected_file = None
        main = tk.Frame(root, bg="#181818")
        main.pack(fill="both", expand=True)
        title = tk.Label(main, text="Narration Tool", font=("Arial", 24, "bold"), fg="white", bg="#181818")
        title.pack(pady=(30, 25))
        select_button = tk.Button(main, text="Select File", command=self.select_file, font=("Arial", 12, "bold"), bg="#333333", fg="white", activebackground="#444444", activeforeground="white", relief="flat", padx=25, pady=10, cursor="hand2")
        select_button.pack()
        self.file_label = tk.Label(main, text="No file selected", font=("Arial", 10), fg="#aaaaaa", bg="#181818")
        self.file_label.pack(pady=(10, 25))
        options_frame = tk.Frame(main, bg="#181818")
        options_frame.pack()
        self.generate_var = tk.BooleanVar(value=False)
        self.song_var = tk.BooleanVar(value=False)
        self.generate_circle = tk.Checkbutton(options_frame, text="Generate Narration", variable=self.generate_var, font=("Arial", 13), fg="white", bg="#181818", activebackground="#181818", activeforeground="white", selectcolor="#181818", cursor="hand2")
        self.generate_circle.pack(anchor="w", pady=8)
        self.song_circle = tk.Checkbutton(options_frame, text="Add Song to Narration", variable=self.song_var, font=("Arial", 13), fg="white", bg="#181818", activebackground="#181818", activeforeground="white", selectcolor="#181818", cursor="hand2")
        self.song_circle.pack(anchor="w", pady=8)
        run_button = tk.Button(main, text="RUN", command=self.run, font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", activebackground="#45a049", activeforeground="white", relief="flat", padx=50, pady=12, cursor="hand2")
        run_button.pack(pady=30)
    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Video files", "*.mp4 *.mov *.avi *.mkv *.webm"), ("Audio files", "*.mp3 *.wav *.m4a *.aac"), ("All files", "*.*")])
        if file_path:
            self.selected_file = file_path
            filename = Path(file_path).name
            self.file_label.config(text=f"Selected: {filename}", fg="#4CAF50")
    def run(self):
        if not self.selected_file:
            messagebox.showwarning("No File", "Please select a file first.")
            return
        if not self.generate_var.get() and not self.song_var.get():
            messagebox.showwarning("No Option", "Please select at least one option.")
            return
        generate_narration = self.generate_var.get()
        add_song = self.song_var.get()
        print("RUNNING")
        print("File:", self.selected_file)
        print("Generate narration:", generate_narration)
        print("Add song:", add_song)
        if generate_narration:
            print("Generating narration...")
        if add_song:
            print("Adding song...")
        messagebox.showinfo("Complete", "The selected operations have been started.")
if __name__ == "__main__":
    root = tk.Tk()
    app = NarrationApp(root)
    root.mainloop()