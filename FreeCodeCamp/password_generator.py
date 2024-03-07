
import re
import secrets
import string


def generate_password(length,nums,special_chars,uppercase,lowercase):
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
            (nums, r"[0-9]"),
            (lowercase, r"[a-z]"),
            (uppercase, r"[A-Z]"),
            (special_chars, r"")
            ]
    
# new_password = generate_password(8)
# print(new_password)
        
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
pattern = r'\.'
quote = "Not all those who wander are lost."
print(re.findall(pattern, quote))