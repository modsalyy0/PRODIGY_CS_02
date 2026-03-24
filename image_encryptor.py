from PIL import Image
def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256,
                            (g + key) % 256,
                            (b + key) % 256)
    img.save("encrypted.png")
    print("Encrypted image saved as encrypted.png")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256,
                            (g - key) % 256,
                            (b - key) % 256)
    img.save("decrypted.png")
    print("Decrypted image saved as decrypted.png")

choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
path = input("Enter image path: ")
key = int(input("Enter key value: "))
if choice == 'e':
    encrypt_image(path, key)
elif choice == 'd':
    decrypt_image(path, key)
else:
    print("Invalid choice!")