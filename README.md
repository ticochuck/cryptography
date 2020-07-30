# Cryptography

[Link to Latest PR](https://github.com/ticochuck/cryptography/pull/1)

## Description
- Devise a method to encrypt a message that can then be decrypted when supplied with the corresponding key.

## Feature Tasks and Requirements
- Create an encrypt function that takes in a plain text phrase and a numeric shift.
The phrase will then be shifted that many letters.
    - E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘acb’, 10) would return ‘klm’
shifts that exceed 26 should wrap around
    - E.g. encrypt(‘abc’,27) would return ‘bcd’

- Create a decrypt method that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form as long as correct key is supplied.

- Break the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.

- Devise a method for the computer to determine if code was broken with minimal human guidance.


## Implementation Notes

- In order to accomplish a certain task you’ll need access to a corpus of English words.
- A search on something like python list of english words should get you going.


## User Acceptance Tests

- encrypt a string with a given shift
- decrypt a previously encrypted string with the same shift
- encryption should handle upper and lower case letters
- encryption should allow non-alpha characters but ignore them, including white space
- decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.


## References

[Letters to Numbers](https://www.kite.com/python/answers/how-to-convert-letters-to-numbers-in-python)

[English Words](https://pypi.org/project/english-words/)


## Lab18 - Cryptography

[Canvas Assignment](https://canvas.instructure.com/courses/2045906/assignments/15161041)

## Author

[Chuck Li Villalobos](https://github.com/ticochuck)
