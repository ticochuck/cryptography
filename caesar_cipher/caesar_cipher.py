import string
import textwrap
from english_words import english_words_lower_set

def encrypt(text, key):
    """
    Shifts plain text using a given key
    
    Args:
        text: plain text phrase
        key: interger
    """
    encrypted_text = ""
    letters = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    for letter in text:
        if letter.lower() in letters or letter in uppercase:
            number = ord(letter.lower()) - 96
            encrypted_number = (number + key) % 26
            encrypted_text += letters[encrypted_number-1]
        else:
            encrypted_text += " "

    return encrypted_text


def decrypt(encrypted, key):
    """
    Decrypts an encrypted message using the same key used for encryptation
    """
    return encrypt(encrypted, -key)


def break_cypher(encrypted_message):
    """
    Takesin an encrypted message and transfors it into its original state
    """
    english_dict = english_words_lower_set
    percent, highest_percent, most_likely_key = 0, 0, 0
    original_message = ""
    potential_keys = []

    for key in range(27):
        new_decrypted = decrypt(encrypted_message, key)
        
        count = 0
        words = new_decrypted.split()
        for word in words:
            if word in english_dict:
                count +=1
        
        percent = (count / len(words)) * 100
        
        if percent > highest_percent:
            highest_percent = percent
            original_message = new_decrypted
            most_likely_key = key
    
    for n in range(-10,10+1):
        potential_keys.append(most_likely_key + 26*(n*2))
    
    print(textwrap.dedent(f'''
        The received encrypted message was: 
        {encrypted_message}
        Using one a key of {most_likely_key}, the original message may be: 
        {original_message}
        Any of the following keys will generate the same result:
        {potential_keys}
        '''))
    return original_message, highest_percent


def was_broken():
    """
    Devise a method for the computer to determine if code was broken with minimal human guidance.
    """
    confidence = break_cypher(encrypted)
    
    if confidence[1] > 80.0:
        print(f'The code was cracked with a {round(confidence[1],2)}% confidence level.')
        return True
    else:
        print(f'{round(confidence[1],2)}% confidence level, tells me that the code was not cracked.')
        return False


if __name__ == "__main__":
    key = 152
    #message = "hello! my name is Chuck. Was this message cracked yes or not?"
    message = 'Hello! My name is Chuck. I am 97 years old. And you?'
    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)

    print('Original: ', message)
    print('Encrypted: ', encrypted)
    print('Decrypted: ', decrypted)

    was_broken()

    