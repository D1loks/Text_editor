from tkinter import messagebox, filedialog


def save_file(textbox):
    text = textbox.get("1.0", "end")  # Get text from the CTkTextbox
    if not text.strip():
        messagebox.showerror("Error", "Text box is empty!")
        return "Text box is empty!"
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text)


def open_file(textbox):
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            textbox.delete("1.0", "end")
            textbox.insert("1.0", content)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found")
