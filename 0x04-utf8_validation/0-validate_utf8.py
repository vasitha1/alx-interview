def validUTF8(data):
    n = len(data)
    i = 0

    while i < n:
        byte = data[i]
        # Determine the number of bytes in this character based on the first byte
        if byte & 0b10000000 == 0:
            # 1-byte character
            length = 1
        elif byte & 0b11100000 == 0b11000000:
            # 2-byte character
            length = 2
        elif byte & 0b11110000 == 0b11100000:
            # 3-byte character
            length = 3
        elif byte & 0b11111000 == 0b11110000:
            # 4-byte character
            length = 4
        else:
            return False  # invalid leading byte

        # Check if there are enough bytes left
        if i + length > n:
            return False

        # For multi-byte characters, check the continuation bytes
        for j in range(1, length):
            if data[i + j] & 0b11000000 != 0b10000000:
                return False

        i += length

    return True