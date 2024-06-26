def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    while True:
        choice = input("Type 'encrypt' to encrypt, 'decrypt' to decrypt, or 'exit' to quit: ").lower()
        if choice == 'exit':
            break
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please type 'encrypt', 'decrypt', or 'exit'.")
            continue

        message = input("Enter your message: ")
        try:
            shift = int(input("Enter shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue

        if choice == 'encrypt':
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'decrypt':
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
