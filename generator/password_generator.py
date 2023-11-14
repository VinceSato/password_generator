from random import sample

def password_generator():

    password_length = int(input("Thank you for using our password generator!\n Please pick the desired password length:\n"))
    password_lower = "abcdefghijklmnopqrstuvwxyz"
    password_upper = password_lower.upper()
    numbers = "0123456789"
    password_special = "!@#$%^&*()?"

    print(f"Understood. Your password has a length of {password_length} digits!")
    print('Our standard password generator contains lower and uppercase letters, as well as numbers.\nWould you like to include special characters? Type "yes" or "y" to accept.')

    has_special = input()

    password_chars = password_lower + password_upper + numbers
    if has_special.lower() in ("yes", "y"):
        password_chars += password_special
        print("Alright. Special characters enabled.")

    try:
        print("Your brand new password is: " + "".join(sample(password_chars,k = password_length)))
    except:
        raise ValueError("Something went wrong. Perhaps your desired length is higher than 73?")
    
    print("Enjoy!")

    print("Bye!")



   
