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
    for letter in text:
        if letter.lower() in letters:
            number = ord(letter.lower()) - 96
            encrypted_number = (number + key) % 26
            encrypted_text += letters[encrypted_number-1]
        else:
            encrypted_text += " "

    return encrypted_text


def decrypt(encripted, key):
    """
    Decrypts an encrypted message using the same key used for encryptation
    """
    return encrypt(encrypted, -key)


def break_cypher(encrypted_message):
    """
    Takesin an encrypted message and transfors it into its original state
    """
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
        The received encypted message was: 
        {encrypted}
        Using one a key of {most_likely_key}, the original message may be: 
        {original_message}
        The following keys will generate the same result:
        {potential_keys}
        '''))
    return original_message


def was_broken():
    """
    Devise a method for the computer to determine if code was broken with minimal human guidance.
    """
    if message == break_cypher(encrypted):
        return True
    else:
        return False


if __name__ == "__main__":
    
    english_dict = english_words_lower_set
    key = 152
    message = "a mi me gusta andar el pelo suelto but not for long"
    
    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)

    print('Encrypted: ', encrypted)
    print('Decrypted: ', decrypted)

    break_cypher(encrypted)
    print(was_broken())

    