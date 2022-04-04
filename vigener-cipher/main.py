import json
import string
import numpy as np

alphabet = list(string.ascii_uppercase)
alphabet_len = len(alphabet)


def encode_message(plaintext, key):
    ciphertext = ''
    for i in range(len(plaintext)):
        p = alphabet.index(plaintext[i])
        k = alphabet.index(key[i % len(key)])
        c = (p + k) % alphabet_len
        ciphertext += alphabet[c]

    return ciphertext


def decode_message(ciphertext, key):
    plaintext = ''
    for i in range(len(ciphertext)):
        p = alphabet.index(ciphertext[i])
        k = alphabet.index(key[i % len(key)])
        c = (p - k) % alphabet_len
        plaintext += alphabet[c]

    return plaintext


def bruteforce_decoding(cipher, key):
    out = ""
    cipher = cipher.upper()
    keymv = 0
    for i in range(len(cipher)):
        if cipher[i] in alphabet:
            ciphercharid = alphabet.index(cipher[i])
            keycharid = alphabet.index(key[(i - keymv) % len(key)])
            out += alphabet[(ciphercharid - keycharid) % len(alphabet)]
        else:
            keymv += 1
            out += cipher[i]

    return out


def increment_ctable(ctable, itter=0):
    if itter == len(ctable):
        ctable.append(0)
    elif ctable[itter] == len(alphabet) - 1:
        ctable[itter] = 0
        increment_ctable(ctable, itter=itter + 1)
    else:
        ctable[itter] += 1

    return ctable


def export_ctable(ctable):
    out = ""
    for i in ctable:
        out += alphabet[i]

    return out


def calc_entropy(labels, base=None):
    e = np.exp(1)
    value, counts = np.unique(labels, return_counts=True)
    norm_counts = counts / counts.sum()
    base = e if base is None else base
    return -(norm_counts * np.log(norm_counts) / np.log(base)).sum()


def bruteforce(ciphertext, max_keylength=None, min_keylength=1):
    ctable = []
    for i in range(min_keylength - 1):
        ctable.append(0)

    max_keylength = len(ciphertext) if max_keylength is None else max_keylength
    cracked = False
    cache = None
    output = []
    counter = 0

    while not cracked:
        i = increment_ctable(ctable)
        if len(i) > max_keylength:
            break
        key = export_ctable(ctable)
        out = bruteforce_decoding(ciphertext, key)
        entropy = calc_entropy(list(out))
        if cache is None or entropy < cache:
            counter += 1
            print(counter, key + ":", entropy, out)
            output.append([key, entropy, out])

    return output


print('input message to encode')
message: string = str(input())

print('''input keyword to encode message
      recommend keys with length less than 6:''')
key: string = str(input())

encoded_message = encode_message(message, key)
print(f'encoded message: {encoded_message} with keyword {key}')

print('decoding message with given key...')

decoded_message = decode_message(encoded_message, key)
print(f'decoded message: {decoded_message}')

print('decoding with bruteforce')

result = bruteforce(encoded_message, len(key))
with open('decryption.json', 'w', encoding='UTF-8') as json_file:
    data = json.dumps(result, indent=4)
    json_file.write(data)
