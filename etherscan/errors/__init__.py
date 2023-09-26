"""Errors that can be raised by this SDK"""


class EtherscanClientError(Exception):
    """Base error class for Etherscan errors"""


class EtherscanModuleError(EtherscanClientError):
    def __init__(self, module: str):
        msg: str = f"Module {module: str} does not exist"
        super(EtherscanClientError, self).__init__(msg)


class EtherscanActionsError(EtherscanClientError):
    def __init__(self, module: str, action: str):
        msg: str = f"Action '{action}' not found in module {module}"
        super(EtherscanClientError, self).__init__(msg)


class EtherscanApiError(EtherscanClientError):
    def __init__(self, message, response):
        msg: str = f"{message} : the server responded with : {response}"
        self.response = response
        super(EtherscanClientError, self).__init__(msg)
