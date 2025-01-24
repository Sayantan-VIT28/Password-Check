import re
import random
import string

def generate_random_password(length=12):
    if length < 8:
        return "Password length must be at least 8 characters."
    
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation  
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]
    
    all_chars = upper + lower + digits + special
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[{}]'.format(re.escape(string.punctuation)), password))
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    if score == 5:
        feedback = "Strong password."
    elif score >= 3:
        feedback = "Moderate password. Consider adding more complexity."
    else:
        feedback = "Weak password. Consider making it longer and adding uppercase letters, numbers, and special characters."
    
    return {
        "Length criteria met": length_criteria,
        "Uppercase criteria met": uppercase_criteria,
        "Lowercase criteria met": lowercase_criteria,
        "Number criteria met": number_criteria,
        "Special character criteria met": special_char_criteria,
        "Strength score": score,
        "Feedback": feedback
    }

def main():
    print("Welcome to the Password Complexity Checker!")
    while True:
        print("\nMenu:")
        print("1. Check Password Strength")
        print("2. Generate Random Password")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            password = input("Enter a password to check its strength: ")
            result = check_password_strength(password)
            print("\nPassword Strength Analysis:")
            for key, value in result.items():
                print(f"{key}: {value}")
        elif choice == "2":
            length = int(input("Enter the desired password length (minimum 8): "))
            random_password = generate_random_password(length)
            print(f"Generated Password: {random_password}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
