import hashlib
import yaml

def load_pass(password):
    password = b"helloworld"
    hashlib.md5(password).hexdigest()
    hashlib.sha1(password).hexdigest()
    yaml.load(password)
