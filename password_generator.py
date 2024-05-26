import random
import string

def generate_password(length=12):# ამ ფუნქციას გადაეცემა პარამეტრი length რომელიც არის სიმბოლოების რაოდენობას
    """
    This function generates a random password of specified length.
    :param length: Length of the password to be generated.
    :return: Randomly generated password.
    """
    # Define the set of characters to be used in the password
    password_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(password_characters) for i in range(length))
    # Return the generated password
    return password

# Dictionary mapping password levels to the number of characters
level = {
        'a': 8,
        'b': 10,      
        'c': 12, 
        'd': 14, 
        'e': 16, 
        'f': 18, 
        'g': 20, 
        'h': 22
}
# Dictionary mapping password levels to hacking likelihood
level_text = {
             'a': 'hack 100%',
             'b': 'hack 85%',
             'c': 'hack 70%',
             'd': 'hack 55%',
             'e': 'hack 40%',
             'f': 'kack 25%',
             'g': 'hack 10%',
             'h': 'hack 0%'
}

print("password level: A < B < C < D < E < F< G < H") # Prompt the user with password levels and their security ratings
pass_level = input("Enter password level: ").lower() # Get the user's chosen password level and convert it to lowercase
password = generate_password(level[pass_level]) # Generate a password based on the chosen level's character count
# Display the result, including the security rating and the generated password
print(f"""
                            {level_text[pass_level]}
----------------------------|--------      
generated password: {password}
------------------------------------
""")
