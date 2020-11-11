from hashlib import sha1
from hashlib import md5
#from Crypto.Hash import SHA256
#from Crypto.Cipher import AES
#from Crypto.Cipher import DES
import binascii


def my_md5(msg):
    hl = md5()
    hl.update(msg.encode('utf-8'))
    return hl.hexdigest()


def my_sha1(msg):
    sh = sha1()
    sh.update(msg.encode('utf-8'))
    return sh.hexdigest()


def my_sha256(msg):
    sh = SHA256.new()
    sh.update(msg.encode('utf-8'))
    return sh.hexdigest()


def my_des(msg, key):
    de = DES.new(key, DES.MODE_ECB)
    mss = msg + (8 - (len(msg) % 8)) * '='
    text = de.encrypt(mss.encode())
    return binascii.b2a_hex(text).decode()


def my_aes_encrypt(msg, key, vi):
    obj = AES.new(key, AES.MODE_CBC, vi)
    txt = obj.encrypt(msg.encode())
    return binascii.b2a_hex(txt).decode()


def my_aes_decrypt(msg, key, vi):
    msg = binascii.a2b_hex(msg)
    obj = AES.new(key, AES.MODE_CBC, vi)
    return obj.decrypt(msg).decode()



