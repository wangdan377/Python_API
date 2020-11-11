import allure
import time
import base64
import sys
import hashlib
import hmac
import struct
class BaseAction:
    @allure.step("生成谷歌验证码")
    def google_code(self, secret_key):
        key = base64.b32decode(secret_key)
        msg = struct.pack(">Q", int(time.time()) // 30)
        code = hmac.new(key, msg, hashlib.sha1).digest()

        # 版本判断
        if sys.version_info > (2, 7):
            o = code[19] & 15
        else:
            o = ord(code[19]) & 15
        code = str((struct.unpack(">I", code[o:o + 4])[0] & 0x7fffffff) % 1000000)

        # 如果第一位是0，则不会显示，判断若是5位码，就在第一位补上0
        if len(code) == 5:
            code = '0' + code
        return code