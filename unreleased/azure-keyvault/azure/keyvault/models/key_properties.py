# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class KeyProperties(Model):
    """Properties of the key pair backing a certificate.

    :param exportable: Indicates if the private key can be exported.
    :type exportable: bool
    :param key_type: The key type.
    :type key_type: str
    :param key_size: The key size in bytes. e.g. 2048.
    :type key_size: int
    :param reuse_key: Indicates if the same key pair will be used on
     certificate renewal.
    :type reuse_key: bool
    """ 

    _attribute_map = {
        'exportable': {'key': 'exportable', 'type': 'bool'},
        'key_type': {'key': 'kty', 'type': 'str'},
        'key_size': {'key': 'key_size', 'type': 'int'},
        'reuse_key': {'key': 'reuse_key', 'type': 'bool'},
    }

    def __init__(self, exportable=None, key_type=None, key_size=None, reuse_key=None):
        self.exportable = exportable
        self.key_type = key_type
        self.key_size = key_size
        self.reuse_key = reuse_key
