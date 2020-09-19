from hashlib import sha1

def load_pass(password):
    password = "helloworld"
    sha1(password.encode()).hexdigest()
