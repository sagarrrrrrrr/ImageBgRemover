import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk
from rembg import remove
import os

class BackgroundRemoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Background Remover")
        self.root.geometry("500x500")
        self.root.config(bg="#f0f0f0")

        self.label = tk.Label(root, text="Drag & Drop an Image Here", width=50, height=10, bg="#e0e0e0")
        self.label.pack(pady=20)
        self.label.drop_target_register(DND_FILES)
        self.label.dnd_bind('<<Drop>>', self.drop)

        self.image_preview = tk.Label(root, bg="#f0f0f0")
        self.image_preview.pack(pady=10)

        self.remove_button = tk.Button(root, text="Remove Background", command=self.remove_background)
        self.remove_button.pack(pady=10)

        self.file_path = None

    def drop(self, event):
        self.file_path = event.data.strip("{}")  # Handle paths with spaces
        if os.path.isfile(self.file_path):
            self.show_image(self.file_path)

    def show_image(self, path):
        img = Image.open(path)
        img.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(img)
        self.image_preview.configure(image=photo)
        self.image_preview.image = photo

    def remove_background(self):
        if not self.file_path:
            messagebox.showerror("Error", "No image selected!")
            return

        try:
            with Image.open(self.file_path) as img:
                output = remove(img)

                file_ext = os.path.splitext(self.file_path)[1].lower()
                if file_ext in [".jpg", ".jpeg"]:
                    output = output.convert("RGB")

                save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                         filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")],
                                                         title="Save Image As")
                if save_path:
                    output.save(save_path)
                    messagebox.showinfo("Success", f"Image saved to:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove background:\n{e}")

if __name__ == "__main__":
    try:
        from tkinterdnd2 import TkinterDnD
    except ImportError:
        print("Please install tkinterdnd2: pip install tkinterdnd2")
        exit()

    root = TkinterDnD.Tk()
    app = BackgroundRemoverApp(root)
    root.mainloop()

