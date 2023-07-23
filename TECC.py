import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def create_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            pass

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get("1.0", tk.END))

def save_as_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get("1.0", tk.END))

def close_file():
    if messagebox.askyesno("Close", "Do you want to close the file? Any unsaved changes will be lost."):
        text.delete("1.0", tk.END)

def about():
    messagebox.showinfo("About", "Simple Text Editor\nVersion 2.0")

def exit_editor():
    if messagebox.askokcancel("Exit", "Do you want to exit the text editor?"):
        root.destroy()

def cut_text():
    text.event_generate("<<Cut>>")

def copy_text():
    text.event_generate("<<Copy>>")

def paste_text():
    text.event_generate("<<Paste>>")

def select_all_text():
    text.tag_add("sel", "1.0", tk.END)

root = tk.Tk()
root.title("Simple Text Editor")

text = scrolledtext.ScrolledText(root, wrap="word")
text.pack(expand=True, fill="both")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=create_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Close", command=close_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)

edit_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all_text)

help_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

root.protocol("WM_DELETE_WINDOW", exit_editor)
root.mainloop()
