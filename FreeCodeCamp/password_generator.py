
import re
import secrets
import string


def generate_password(length=16,nums=1,special_chars=1,uppercase=1,lowercase=1):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols
    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
            
        constraints = [
            # class \d is a shortand for [0-9]
            # class \w is a shorthand for [a-zA-Z0-9]
            # class \W is a shorthand for [^a-zA-Z0-9]
        
            (nums, r"\d"),
            (lowercase, fr"[{symbols}]"),
            (uppercase, r"[A-Z]"),
            (special_chars, r"[a-z]")
            ]
        
        # Check Constraints
        if all(
            constraint <= len(re.findall(pattern,password))
            for constraint, pattern in constraints
        ):
            break
    return password
if __name__ == "__main__":
 
    new_password = generate_password()
    print("Generated Password:",new_password)
        
# Search() from regex
# we can do it by 2 ways 
'''
pattern = re.compile('l+')
quote = "Not all those who wander are lost."
print(pattern.search(quote))
'''
"""
pattern = ('l+')
quote = "Not all those who wander are lost."
print(re.search(pattern, quote))
"""

#findall() = it return a list with all the occurrences of the matched pattern

"""
pattern = ('l+')
quote = "Not all those who wander are lost."
print(re.findall(pattern, quote))
"""
# caret (^), placed at the beginning of the character claas, matches all the characters except those specified in the class
# . character is a wildcard that matches any character in a string
"""
pattern = r'\.'
quote = "Not all those who wander are lost."
print(re.findall(pattern, quote))
"""