# -*- coding:utf-8 -*-
import os
import rsa


class RsaFunc:
    def __init__(self):
        pass

    # 生成秘钥并保存
    @staticmethod
    def pub_privkey(n):
        (pubkey, privkey) = rsa.newkeys(n)
        file_path = os.path.split(os.path.realpath(__file__))[0] + '\\output'
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        with open(file_path + '/public.pem', 'w+') as f:
            f.write(pubkey.save_pkcs1().decode())
        with open(file_path + '/private.pem', 'w+') as f:
            f.write(privkey.save_pkcs1().decode())
        return file_path

    # 导入公钥并加密得到密文
    def encode_rsa(self, info, n):
        file_path = self.pub_privkey(n)
        with open(file_path + '/public.pem', 'r') as f:
            pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
        crypto_text = rsa.encrypt(info.encode(), pubkey)
        return file_path, crypto_text

    # 导入私钥并解密得到明文
    @staticmethod
    def decode_rsa(file_path, crypto_text):
        with open(file_path + '/private.pem', 'r') as f:
            privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
        # 用自己的私钥对收到的密文进行解密，得到明文
        message = rsa.decrypt(crypto_text, privkey).decode()
        return message


if __name__ == '__main__':
    info_in = '张三'
    # 实例调用
    filepath, cp_text = RsaFunc().encode_rsa(info_in, 1024)
    # 类方法调用
    ex_text = RsaFunc.decode_rsa(filepath, cp_text)
    print('原始明文：', info_in, '\n加密后密文：', cp_text, '\n解密后明文：', ex_text)
