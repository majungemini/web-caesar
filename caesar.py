def alphabet_position(letter):
    list1 = 'abcdefghijklmnopqrstuvwxyz'
    list2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in list1:
        for idx in range(len(list1)):
            if letter == list1[idx]:
                position_letter = idx
    else:
        for idx in range(len(list2)):
            if letter == list2[idx]:
                position_letter = idx
    return position_letter

def rotate_character(char, rot):
    list1 = 'abcdefghijklmnopqrstuvwxyz'
    list2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    list3 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if char not in list3:
        return char
    else:
        char_posi = alphabet_position(char)
        rot_posi = char_posi + rot

        if char in list1:
            if rot_posi < 26:
                new_char = list1[rot_posi]
            else:
                new_char = list1[rot_posi % 26]
        elif char in list2:
            if rot_posi < 26:
                new_char = list2[rot_posi]
            else:
                new_char = list2[rot_posi % 26]
        return new_char

def encrypt(text,rot):
    new_text = ""
    for letter in text:
        new_text = new_text + rotate_character(letter,rot)
    return new_text
