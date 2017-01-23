import string

def alphabet_position(letter):
    test_str = string.ascii_lowercase
    test_str2 = string.ascii_uppercase
    new_letter = letter.lower()
    pos = test_str.find(new_letter)

    return pos

def rotate_character(char, rot):
    test_str = string.ascii_lowercase
    test_str2 = string.ascii_uppercase

    if char not in test_str:
        if char not in test_str2:
            return char

    pos = alphabet_position(char)
    val = (pos + rot) % 26

    if char in test_str2:
        new_str = test_str2[val]
    else:
        new_str = test_str[val]

    return new_str

def encrypt(text, rot):
    rtr_str = ''
    for char in text:
        rtr_str = rtr_str + rotate_character(char, rot)

    return rtr_str
