from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt, decrypt, break_cypher, was_broken

def test_version():
    assert __version__ == '0.1.0'


def test_encrypt_exists():
    encrypt


def test_decrypt_exists():
    decrypt


def test_break_cypher_exists():
    break_cypher


def test_was_broken_exists():
    was_broken


# encrypt a string with a given shift
def test_encrypt():
    message = 'abcd'
    key = 1
    encrypted = encrypt(message, key)
    assert encrypted == 'bcde'


def test_wrap_26():
    message = 'xyza'
    key = 2
    encrypted = encrypt(message, key)
    assert encrypted == 'zabc'


def test_wrap_26_backwards():
    message = 'abcd'
    key = -2
    encrypted = encrypt(message, key)
    assert encrypted == 'yzab'


# decrypt a previously encrypted string with the same shift
def test_encrypt_phrase():
    message = 'hello my name is chuck'
    key = 152
    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)
    assert encrypted == 'dahhk iu jwia eo ydqyg'
    assert message == decrypted


# encryption should handle upper and lower case letters
def test_handle_upper_case():
    message = 'Hello my name is Chuck'
    key = 152
    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)
    assert encrypted == 'dahhk iu jwia eo ydqyg'
    assert decrypted == 'hello my name is chuck'


# encryption should allow non-alpha characters but ignore them, including white space
def test_non_alpha_characters():
    message = 'Hello! My name is Chuck. I am 97 years old. And you?'
    key = 152
    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)
    assert encrypted == 'dahhk  iu jwia eo ydqyg  e wi    uawno khz  wjz ukq '
    assert decrypted == 'hello  my name is chuck  i am    years old  and you '


# decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
def test_brake_cypher():
    message = 'hs vzr sgd adrs ne shldr  hs vzr sgd vnqrs ne shldr '
    decrypted = break_cypher(message)
    assert decrypted[0] == 'it was the best of times  it was the worst of times '