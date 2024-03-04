# Open a file in write mode ('w')
with open('passage.txt', 'w') as file:
    # Prompt the user to input a passage of text
    passage = input("Enter your passage: ")
    
    # Write the passage to the file
    file.write(passage)

print("Passage has been written to passage.txt")
