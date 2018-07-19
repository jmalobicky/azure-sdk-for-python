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


class AzureStorageInfoValue(Model):
    """Azure Files or Blob Storage access information value for dictionary
    storage.

    :param type: Type of storage. Possible values include: 'AzureFiles',
     'AzureBlob'
    :type type: str or ~azure.mgmt.web.models.AzureStorageType
    :param account_name: Name of the storage account.
    :type account_name: str
    :param share_name: Name of the file share (container name, for Blob
     storage).
    :type share_name: str
    :param access_key: Access key for the storage account.
    :type access_key: str
    :param mount_path: Path to mount the storage within the site's runtime
     environment.
    :type mount_path: str
    :param state: State of the storage account. Possible values include: 'Ok',
     'InvalidCredentials', 'InvalidShare'
    :type state: str or ~azure.mgmt.web.models.AzureStorageState
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'AzureStorageType'},
        'account_name': {'key': 'accountName', 'type': 'str'},
        'share_name': {'key': 'shareName', 'type': 'str'},
        'access_key': {'key': 'accessKey', 'type': 'str'},
        'mount_path': {'key': 'mountPath', 'type': 'str'},
        'state': {'key': 'state', 'type': 'AzureStorageState'},
    }

    def __init__(self, *, type=None, account_name: str=None, share_name: str=None, access_key: str=None, mount_path: str=None, state=None, **kwargs) -> None:
        super(AzureStorageInfoValue, self).__init__(**kwargs)
        self.type = type
        self.account_name = account_name
        self.share_name = share_name
        self.access_key = access_key
        self.mount_path = mount_path
        self.state = state
