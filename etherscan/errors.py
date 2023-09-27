"""Errors that can be raised by this SDK"""

from etherscan.response import EtherscanResponse


class EtherscanClientError(Exception):
    """Base error class for Etherscan errors"""


class EtherscanRequestError(EtherscanClientError):
    def __init__(self, message: str, response: EtherscanResponse):
        msg: str = f"""
        message : {message}\n
        the server responded with :\n
        status  : {response.body.status}\n
        message : {response.body.message}\n
        result  : {response.body.result}\n
        """
        super(EtherscanClientError, self).__init__(msg)


class EtherscanApiError(EtherscanClientError):
    def __init__(self, message: str, response: EtherscanResponse):
        msg: str = f"""
        message : {message}\n
        the server responded with :\n
        code : {response.status_code}\n
        status  : {response.body.status}\n
        message : {response.body.message}\n
        result  : {response.body.result}\n
        """
        super(EtherscanClientError, self).__init__(msg)
