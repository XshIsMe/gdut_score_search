#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import binascii
from Crypto.Cipher import AES


def pad(text):
    """
    填充函数，使被加密数据的字节码长度是block_size的整数倍
    """
    count = len(text)
    add = AES.block_size - (count % AES.block_size)
    entext = text + (chr(add) * add)
    return entext.encode('UTF-8')


def aes(verifycode, password):
    key = (verifycode.zfill(4)[:4]*4).encode('UTF-8')
    srcs = password
    mode = AES.MODE_ECB

    encrypted = AES.new(key, mode)
    password = encrypted.encrypt(pad(srcs))

    password = binascii.b2a_hex(password)
    return password.decode()
