import hashlib
import yaml

def load_pass(password):
    password = b"helloworld"
    hashlib.md5(password).hexdigest()
    yaml.load(password)
