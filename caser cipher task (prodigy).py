def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Welcome to the Caesar Cipher Program!")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").strip().upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice! Please choose 'E' for encryption or 'D' for decryption.")
        return
    
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'E':
        result = encrypt(message, shift)
        print(f"Encrypted Message: {result}")
    elif choice == 'D':
        result = decrypt(message, shift)
        print(f"Decrypted Message: {result}")

if __name__ == "__main__":
    main()
