import hashlib
password = "thembi123"
hash_object = hashlib.sha256(password.encode())
print(hash_object.hexdigest())