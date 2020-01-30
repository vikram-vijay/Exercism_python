def commands(number):
    secret_handshake = {1: "wink", 2: "double blink", 4: "close your eyes", 8: "jump"}
    handshake = [secret_handshake[i] for i in secret_handshake.keys() if bool(i & number)]
    if not (number // 16) % 2:
        return handshake
    return handshake[::-1]
