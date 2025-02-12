import tkinter as tk
from tkinter import messagebox
import pyshorteners
import webbrowser

def shorten_url():
    link = url_entry.get()
    if not link:
        messagebox.showerror("Error", "Please enter a URL")
        return
    
    s = pyshorteners.Shortener()
    choice = shortener_var.get()
    
    try:
        if choice == "tinyurl":
            shorturl = s.tinyurl.short(link)
        elif choice == "is.gd":
            shorturl = s.isgd.short(link)
        else:
            messagebox.showerror("Error", "Please select a shortener")
            return
        
        result_label.config(text=f"Shortened URL: {shorturl}", fg="blue", cursor="hand2")
        result_label.bind("<Button-1>", lambda e: webbrowser.open_new(shorturl))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("URL Shortener")

# URL entry
tk.Label(root, text="Enter the URL to shorten:", font=("Helvetica", 12)).pack(pady=5)
url_entry = tk.Entry(root, width=50, font=("Helvetica", 12))
url_entry.pack(pady=5)

# Shortener options
shortener_var = tk.StringVar(value="tinyurl")
tk.Radiobutton(root, text="tinyurl", variable=shortener_var, value="tinyurl", font=("Helvetica", 12)).pack(anchor=tk.W)
tk.Radiobutton(root, text="is.gd", variable=shortener_var, value="is.gd", font=("Helvetica", 12)).pack(anchor=tk.W)

# Shorten button
tk.Button(root, text="Shorten URL", command=shorten_url, font=("Helvetica", 12)).pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=5)

# Run the application
root.mainloop()
