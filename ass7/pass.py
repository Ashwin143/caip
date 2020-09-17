'''from cryptography.fernet import Fernet
key = b'' # Use one of the methods to get a key (it must be the same when decrypting)
input_file = 'test.txt'
output_file = 'test.encrypted'

with open(input_file, 'rb') as f:
    data = f.read()  # Read the bytes of the input file

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted) '''



'''
# print(key)
# b'B8XBLJDiroM3N2nCBuUlzPL06AmfV4XkPJ5OKsPZbC4='
# cipher = Fernet(key)
# password = "ACESBS35".encode('utf-8')
# token = cipher.encrypt(password)
# print(token)
# b'gAAAAABe_TUP82q1zMR9SZw1LpawRLHjg' 
# cipher = Fernet(key)
# mypassword = cipher.decrypt(token).decode('utf-8')
# print(mypassword)

cipher = Fernet(key)
# password = "ACESBS35".encode('utf-8')

# token = cipher.encrypt(password)
# print(token)
# b'gAAAAABe_TUP82q1zMR9SZw1LpawRLHjg' 
# cipher = Fernet(key)

mypassword = cipher.decrypt(token).decode('utf-8')
print(mypassword)'''



# import base64
# from cryptography.fernet import Fernet
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# password_provided = "ACESBS35"  # This is input in the form of a string
# password = password_provided.encode()  # Convert to type bytes
# salt = b'salt_'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes

# key=b'gZWoLcYsup587B2dWMNgYKgNiWvFA4oc7ZHX3eYIZo4='
# token=b'gAAAAABfR4OiiGwz4za-Dymg7XEI7f9OLzoT68VfY5Mqu95UR0fBd-tnb_7z3uieK_FantPP5mGqagwyKgHfKoVT49B7LKdFgQ=='
# kdf = PBKDF2HMAC(
#     algorithm=hashes.SHA256(),
#     length=32,
#     salt=salt,
#     iterations=100000,
#     backend=default_backend()
# )
# key = base64.urlsafe_b64encode(kdf.derive(password)) 



# token = Fernet(key).encrypt(password)
# print(token)

# mypassword = Fernet(key).decrypt(token).decode('utf-8')
# print(mypassword)




