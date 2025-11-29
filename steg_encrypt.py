import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

# --- Encryption functions (same as before, simplified) ---
def encrypt_add(arr, key):
    return (arr + key) % 256

def decrypt_add(arr, key):
    return (arr - key) % 256

def encrypt_xor(arr, key):
    return arr ^ key

def decrypt_xor(arr, key):
    return arr ^ key

# --- GUI logic ---
class ImageCipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Image Cipher")
        self.image = None
        self.img_array = None

        # Buttons
        tk.Button(root, text="Open Image", command=self.open_image).pack(pady=5)
        tk.Button(root, text="Encrypt (Add)", command=self.encrypt_add).pack(pady=5)
        tk.Button(root, text="Decrypt (Add)", command=self.decrypt_add).pack(pady=5)
        tk.Button(root, text="Encrypt (XOR)", command=self.encrypt_xor).pack(pady=5)
        tk.Button(root, text="Decrypt (XOR)", command=self.decrypt_xor).pack(pady=5)
        tk.Button(root, text="Save Image", command=self.save_image).pack(pady=5)

        # Canvas for preview
        self.canvas = tk.Label(root)
        self.canvas.pack()

        # Key entry
        tk.Label(root, text="Key (integer):").pack()
        self.key_entry = tk.Entry(root)
        self.key_entry.insert(0, "42")
        self.key_entry.pack()

    def open_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.bmp")])
        if not path:
            return
        img = Image.open(path).convert("RGB")
        self.img_array = np.array(img)
        self.display_image(img)

    def display_image(self, img):
        img_tk = ImageTk.PhotoImage(img)
        self.canvas.configure(image=img_tk)
        self.canvas.image = img_tk

    def get_key(self):
        try:
            return int(self.key_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Key must be an integer")
            return None

    def encrypt_add(self):
        key = self.get_key()
        if key is None or self.img_array is None: return
        self.img_array = encrypt_add(self.img_array, key)
        self.display_image(Image.fromarray(self.img_array.astype('uint8')))

    def decrypt_add(self):
        key = self.get_key()
        if key is None or self.img_array is None: return
        self.img_array = decrypt_add(self.img_array, key)
        self.display_image(Image.fromarray(self.img_array.astype('uint8')))

    def encrypt_xor(self):
        key = self.get_key()
        if key is None or self.img_array is None: return
        self.img_array = encrypt_xor(self.img_array, key)
        self.display_image(Image.fromarray(self.img_array.astype('uint8')))

    def decrypt_xor(self):
        key = self.get_key()
        if key is None or self.img_array is None: return
        self.img_array = decrypt_xor(self.img_array, key)
        self.display_image(Image.fromarray(self.img_array.astype('uint8')))

    def save_image(self):
        if self.img_array is None:
            messagebox.showerror("Error", "No image to save")
            return
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            Image.fromarray(self.img_array.astype('uint8')).save(path)
            messagebox.showinfo("Saved", f"Image saved to {path}")

# --- Run GUI ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCipherGUI(root)
    root.mainloop()