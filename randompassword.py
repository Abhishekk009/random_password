import random
import string


def generate_password(length: int = 6) -> str:
    """
    Generate a random password of the given length.
    The password will contain uppercase, lowercase letters, and digits.

    :param length: Desired password length (minimum 6)
    :return: Randomly generated password
    """
    if length < 6:
        raise ValueError("Password length must be at least 6 characters.")

    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length: "))
        generated_password = generate_password(password_length)
        print("Generated password:", generated_password)
    except ValueError as err:
        # Handles non-integer input and length < 6 cases
        print(err)
