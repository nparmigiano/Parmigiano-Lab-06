


def encode_password(password):
    """
    This function takes in an 8-digit password as a string and returns the encoded password,
    with each digit being shifted up by 3 numbers.
    """
    encoded_password = ""
    for char in password:
        if not char.isdigit():
            raise ValueError("Password must contain only integers")
        encoded_password += str((int(char) + 3) % 10)
    if len(encoded_password) != 8:
        raise ValueError("Encoded password should be 8 digits long")
    return encoded_password


def decode_password(password):
    """
    This function takes in an encoded password as a string and returns the original password,
    with each digit being shifted down by 3 numbers.
    """
    decoded_password = ""
    for char in password:
        if not char.isdigit():
            raise ValueError("Encoded password must contain only integers")
        decoded_password += str((int(char) - 3) % 10)
    if len(decoded_password) != 8:
        raise ValueError("Decoded password should be 8 digits long")
    return decoded_password


while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    choice = input("Please enter an option: ")

    if choice == "1":
        password = input("Please enter your 8-digit password to encode: ")
        try:
            encoded_password = encode_password(password)
        except ValueError as e:
            print(e)
        else:
            print("Your password has been encoded and stored as: ", encoded_password)

    elif choice == "2":
        encoded_password = input("Please enter your password to decode: ")
        try:
            decoded_password = decode_password(encoded_password)
        except ValueError as e:
            print(e)
        else:
            print("Your password has been decoded and is: ", decoded_password)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice, please try again.")
