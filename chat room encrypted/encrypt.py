"""

"""

class ENC(object):
    def __init__(self):
        self.name = "ram"


    def encrypt_message(self, message, key):
        encrypted_message = ""
        for c in message:
            encrypted_message += chr(ord(c) + key)
        return encrypted_message

    def decrypt_message(self, encrypted_message, key):
        decrypted_message = ""
        for c in encrypted_message:
            decrypted_message += chr(ord(c) - key)
        return decrypted_message