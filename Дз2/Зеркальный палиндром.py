s = input()
def is_palindrome(s):
    return s == s[::-1]


def is_mirror(s):
    mirror_chars = {
        '0': '0', '1': '1', '2': ' ', '3': ' ', '4': ' ',
        '5': ' ', '6': '9', '7': ' ', '8': '8', '9': '6',
        'A': 'A', 'b': ' ', 'd': ' ', 'E': 'E', 'H': 'H',
        'I': 'I', 'M': 'M', 'O': 'O', 'p': ' ', 'q': ' ',
        'T': 'T', 'U': 'U', 'v': 'v', 'W': 'W', 'X': 'X',
        'Y': 'Y', 'Z': ' '
    }

    mirrored_string = ""

    for char in reversed(s):
        if char not in mirror_chars or mirror_chars[char] == ' ':
            return False
        mirrored_string += mirror_chars[char]

    return mirrored_string == s


def is_mirror_palindrome(s):
    return is_palindrome(s) and is_mirror(s)

print(is_mirror_palindrome(s))