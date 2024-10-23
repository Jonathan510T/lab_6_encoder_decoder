# encoder_decoder.py
# Author: Jonathan Tang

def encode(password):
    encoded = ""
    for char in password:
        encoded += str((int(char) + 3) % 10)
    return encoded


def main():
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == '2':
            print("Decode option not yet implemented!")
        elif option == '3':
            break
        else:
            print("Invalid option! Please try again.")


if __name__ == "__main__":
    main()