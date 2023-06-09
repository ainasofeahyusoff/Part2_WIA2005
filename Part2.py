def crack_safe(correct_combination):
    found = False
    
    for i in range(1000):
        combination = str(i).zfill(3)
        print (combination)
        if combination == correct_combination:
            found = True
            break
    
    if found:
        print("Safe cracked! The combination is:", correct_combination)
    else:
        print("Failed to crack the safe. Combination not found.")

# Receive input from the user for the correct combination
correct_combination = input("Enter the correct combination (3 digits): ")

# Call the crack_safe function to attempt cracking the safe
crack_safe(correct_combination)
