import os
import argparse
import pdb

def decode(shift, cipher):
    decoded = ''
    for char in cipher:
        if char.isalpha():
            is_upper = char.isupper()
            ascii_offset = ord('A') if is_upper else ord('a')
            shifted_char = chr(((ord(char) - ascii_offset - shift) % 26) + ascii_offset)
            decoded += shifted_char
        else:
            decoded += char
    return decoded

def cipher_decrypt(args, cipher=None):
    words = {}
    word = ''

    # read in the file
    with open('en-US.dic', 'r', encoding='utf-8') as file:
        text = file.readlines()
        
    # add words to dictionary for efficient lookup
    for word in text:
        word = word.strip()
        words[word] = True

    # pdb.set_trace()

    if cipher is not None:
        scores = {i: 0 for i in range(0, 26)}
        tokens = cipher.strip().split()
        #iterate through words by inverse shift values
        for i in range(0, 26):
            for word in tokens:
                decoded = decode(i, word)
                if decoded.lower() in words:
                    scores[i] += 1

        shift = 26 - max(scores, key=scores.get)
        # make sure that it returns zero in the case that there is no shift.
        if shift == 26:
            shift = 0
        return (shift), decode(26 - shift, cipher)
    else:
        if not args.filepath:
            filepath = input('Enter filepath of ciphertext file: ')
        else:
            filepath = args.filepath
        
        with open(filepath, 'r') as file:
            cipher = file.readlines()
    
        if os.path.exists('output.txt'):
            os.remove('output.txt')
        # iterate through the lines in a file
        for msg in cipher:    
            # a dict for scoring shift values 
            scores = {i: 0 for i in range(0, 26)}
            tokens = msg.strip().split()
            #iterate through words by inverse shift values
            for i in range(0, 26):
                for word in tokens:
                    decoded = decode(i, word)
                    if decoded.lower() in words:
                        scores[i] += 1

            shift = 26 - max(scores, key=scores.get)
            with open('output.txt', 'a') as file:
                file.write(f'{shift};{decode(26 - shift, msg)}\n')

            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This is a Caesar cipher decryption program. \
                                                  Given a ciphertext file, it should automatically detect and \
                                                  output the correct shift value and plaintext')
    
    parser.add_argument("-f", "--filepath", action="store", const=None, type=str, nargs="?")
    parser.add_argument("-l", "--line", action="store", const=None, type=str, nargs="?")

    args = parser.parse_args()
    if args.line:
        cipher_decrypt(None, args.line)
    else:
        cipher_decrypt(args)    
