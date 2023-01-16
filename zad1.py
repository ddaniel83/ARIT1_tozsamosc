import base64


def encryption(string):
    print(f'String before encoding: {string}')
    encoded_string = string.encode('ascii')

    encoded_bytes = base64.b64encode(encoded_string)
    base64_string = encoded_bytes.decode("ascii")
    print(f'Encoded string: {base64_string}')

    decoded_string_bytes = base64.b64decode(base64_string)
    decoded_string = decoded_string_bytes.decode('ascii')
    print(f'Decoded string: {decoded_string}')


encryption('Test')
