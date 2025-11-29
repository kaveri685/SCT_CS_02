Below is a clean, professional,  **README.md** based on the content  for **TASK 02**.

---

```markdown
# 🖼️ Task 02 — Image Encryption Tool  
*A SkillCraft Technology Project*

---

## 📘 Overview

In this task, you will **develop a simple image encryption tool** using **pixel manipulation techniques**.  
The goal is to explore how images can be encrypted by modifying their pixel values through basic operations.

Your tool should support:

- 🔄 Swapping pixel values  
- ➕ Applying mathematical operations to each pixel (e.g., add, subtract, XOR)  
- 🔓 Ability to reverse the operation (decrypt)

---

## 🧠 What is Pixel-Based Image Encryption?

Image encryption using pixel manipulation works by modifying the RGB values of pixels.  
Each pixel in an image has values like:

```

R: 0–255
G: 0–255
B: 0–255

```

By changing these values systematically, the image becomes scrambled or encrypted.

### Common Manipulations:

| Method | Description | Reversible? |
|--------|-------------|-------------|
| Pixel Swap | Exchange positions of pixels | ✔ Yes |
| Addition/Subtraction | Add or subtract a constant key | ✔ Yes |
| XOR Operation | XOR pixel value with a key | ✔ Yes |
| Pixel Shuffling | Rearranging pixels in patterns | ✔ Yes |

---

## 🚀 Features to Implement

Your program should:

- ✔ Load an image  
- ✔ Encrypt the image using one or more operations  
- ✔ Save the encrypted output  
- ✔ Decrypt and reconstruct the original image  
- ✔ Allow the user to choose encryption method  

---

## 📂 Suggested File Structure

```

📦 Image-Encryption-Tool
┣ 📜 image_encrypt.py
┣ 📜 README.md
┗ 📂 samples
┣ original.png
┗ encrypted.png

````

---

## 💻 Sample Python Code (Basic Pixel Manipulation)

Below is an example using **Pillow (PIL)**.

### 🔹 Example: XOR-based Encryption

```python
from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print("Image encrypted successfully!")


def decrypt_image(input_path, output_path, key):
    # XORing again with the same key decrypts it
    encrypt_image(input_path, output_path, key)


# Example Usage
encrypt_image("original.png", "encrypted.png", key=25)
decrypt_image("encrypted.png", "decrypted.png", key=25)
````

---

## 📝 Other Operations You Can Implement

### 🔹 1. Pixel Swapping

Swap positions of (i, j) with (width-i-1, height-j-1).

### 🔹 2. Add/Subtract Key

```
new_pixel = (old_pixel + key) % 256
```

### 🔹 3. Shuffle Rows/Columns

Randomize pixel order with a seed.

---

## 📌 Example Output

| Original                          | Encrypted                           |
| --------------------------------- | ----------------------------------- |
| ![original](samples/original.png) | ![encrypted](samples/encrypted.png) |

*(Images are optional for your project)*

---

## 🛠️ How to Run

### 1️⃣ Install dependencies

```
pip install pillow
```

### 2️⃣ Run the script

```
python image_encrypt.py
```

### 3️⃣ Provide:

* Input image path
* Encryption key
* Encryption method

---

## 🎯 Future Improvements

* Add a GUI using **Tkinter**
* Add multiple encryption layers
* Add grayscale mode
* Implement block-based scrambling

---

## 📜 License

This project is created for educational purposes under **SkillCraft Technology**.

---

## 👨‍💻 Author

**SkillCraft Technology**



Just tell me!
