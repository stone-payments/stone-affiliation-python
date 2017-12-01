# -*- coding: utf-8 -*-

"""
Pacote com processadores de criptografia
"""
import hashlib
import hmac


def encrypt(key, message):
    digester = hmac.new(bytes(key, "utf-8"),
                        bytes(message, "utf-8"),
                        hashlib.sha512)

    return digester.hexdigest()
