from hashlib import md5

def load_pass(password):
    password = "helloworld"
    md5(password.encode()).hexdigest()
