import string

available_characters = list(string.ascii_letters) + [" "]

base_char_int_mapping = {}
base_int_char_mapping = {}
i = 0
for character in available_characters:
    base_char_int_mapping[character] = i
    base_int_char_mapping[i] = character
    i += 1

max_char_value = i-1

offset = 0
encoder = {}
decoder = {}
for key_char in available_characters:
    key_encoder_lookup = {}
    key_decoder_lookup = {}
    for plain_text_char in available_characters:
        offset_char_int_value = base_char_int_mapping[plain_text_char] + offset
        if offset_char_int_value > max_char_value:
            offset_char_int_value = offset_char_int_value - max_char_value - 1
        offset_character_mapping = base_int_char_mapping[offset_char_int_value]
        key_encoder_lookup[plain_text_char] = offset_character_mapping
        key_decoder_lookup[offset_character_mapping] = plain_text_char
    encoder[key_char] = key_encoder_lookup
    decoder[key_char] = key_decoder_lookup
    offset += 1


def encode_message(message, key, encoder):
    message = message.replace("\n", " ")
    encoded_message = []
    key_index = 0
    key_as_list = [key_character if key_character in encoder.keys() else "_"
                   for key_character in list(key)]
    for character in message:
        if key_index > len(key_as_list) - 1:
            key_index = 0
        key_character = key_as_list[key_index]
        if character not in encoder.keys():
            encoded_message.append("_")
        else:
            encoded_message.append(encoder[key_character][character])
        key_index += 1

    return "".join(encoded_message)


def decode_message(message, key, decoder):
    message = message.replace("\n", " ")
    decoded_message = []
    key_index = 0
    key_as_list = [
        key_character if key_character in decoder.keys() else "_"
        for key_character in list(key)
    ]

    for character in message:
        if key_index > len(key_as_list) - 1:
            key_index = 0
        key_character = key_as_list[key_index]
        if character not in decoder.keys():
            decoded_message.append("_")
        else:
            decoded_message.append(decoder[key_character][character])
        key_index += 1

    return "".join(decoded_message)


print('input message to encode')
message: string = str(input())

print('input keyword to encode message')
key: string = str(input())

encoded_message = encode_message(message, key, encoder)

print(f'encoded message: {encoded_message} with keyword {key}')

print('decoding message with prepared table...')

decoded_message = decode_message(encoded_message, key, decoder)
print(f'decoded message: {decoded_message}')
