__author__ = 'polina'

def encode_morze(text, text_morse=''):
    morse_code = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    " " : "__"}
    text = text.upper()
    for i in text:
        if i not in morse_code.keys() :
            continue
        text_morse+=morse_code[i]+'__'
    res = text_morse.replace('.', '^_').replace('-', '^^^_').rstrip('_')
    return res



encode_morze('In a hole in the round there lived a hobbit')


# proposet version
# def encode_morze(text):
#     morze = {
#         "A" : ".-",
#         "B" : "-...",
#         "C" : "-.-.",
#         "D" : "-..",
#         "E" : ".",
#         "F" : "..-.",
#         "G" : "--.",
#         "H" : "....",
#         "I" : "..",
#         "J" : ".---",
#         "K" : "-.-",
#         "L" : ".-..",
#         "M" : "--",
#         "N" : "-.",
#         "O" : "---",
#         "P" : ".--.",
#         "Q" : "--.-",
#         "R" : ".-.",
#         "S" : "...",
#         "T" : "-",
#         "U" : "..-",
#         "V" : "...-",
#         "W" : ".--",
#         "X" : "-..-",
#         "Y" : "-.--",
#         "Z" : "--..",
#     }
#     encoded = ''
#     for i in text:
#         to_add = ''
#         if i == ' ':
#             to_add = '____'
#         elif i.upper() in morze.keys():
#             to_add = morze[i.upper()].replace('.','^_').replace('-','^^^_') + '__'
#         encoded = encoded + to_add
#     if len(encoded):
#         while encoded[-1] == '_':
#             encoded = encoded[:-1]
#     return encoded