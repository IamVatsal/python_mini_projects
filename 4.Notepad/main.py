import tkinter as tk
from tkinter import Widget, filedialog
from tkinter import Tk, Text, Button, Frame

from sympy import false, true


class SimpleNotepad:
    open_file: bool = false
    file_path: str = None
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("Vatsal's Simple Notepad")
        # self.root.geometry("600x400")

        # Text Widget
        self.text_area = Text(self.root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH)


        # Frame for Buttons
        self.frame = Frame(self.root)
        self.frame.pack()

        # Save Buttons
        self.save_button = Button(self.frame, text="Save", command=self.save_file)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        # save as Button
        self.save_as_button = Button(self.frame, text="Save As", command=self.save_file_as)
        self.save_as_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Load Button
        self.save_button = Button(self.frame, text="Load", command=self.load_file)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)


    def save_file_as(self) -> None:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                  filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))

        self.open_file = true
        self.file_path = file_path


    def save_file(self) -> None:
        if self.open_file:
            file_path = self.file_path
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                      filetypes=[("Text files", "*.txt")])
        
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
        
        
        print(f"File saved successfully! {file_path}")

    def load_file(self) -> None:
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

        self.open_file = true
        self.file_path = file_path
        
        print(f"File loaded successfully! {file_path}")

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root: Tk = Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()

if __name__ == "__main__":
    main()