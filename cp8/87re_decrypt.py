alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(start_text,shift_amout,chiper_direction):
    end_text=""        
    if chiper_direction == "decode":
        shift_amout*= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amout
        end_text += alphabet[new_position]
    print(f"Here {chiper_direction} result: {end_text}")

caesar(start_text = text, shift_amout = shift, chiper_dirction = direction)


# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")


# def decrypt(chiper_text, shift_amout):
#   plain_text =""
#   for letter in chiper_text:
#     position=alphabet.index(letter)
#     new_position = position - shift_amout
#     plain_text += alphabet[new_position]
#   print(f"The decrypt text is {plain_text}")

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(chiper_text=text, shift_amout= shift)