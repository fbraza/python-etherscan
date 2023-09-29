import pydantic
from requests.structures import CaseInsensitiveDict


class EtherscanResult(pydantic.BaseModel):
    status: str
    message: str
    result: str | list | dict


class EtherscanResponse:
    def __init__(
        self,
        request_url: str,
        http_method: str | None,
        status_code: int,
        response_headers: CaseInsensitiveDict[str],
        etherscan_body: EtherscanResult,
        etherscan_module: str,
        etherscan_action: str,
    ):
        """_summary_

        Args:
            request_url (str): _description_
            http_method (str | None): _description_
            status_code (int): _description_
            response_headers (CaseInsensitiveDict[str]): _description_
            etherscan_body (EtherscanResult): _description_
            etherscan_module (str): _description_
            etherscan_action (str): _description_
        """
        self.url = request_url
        self.method = http_method
        self.status_code = status_code
        self.headers = response_headers
        self.body = etherscan_body
        self.module = etherscan_module
        self.action = etherscan_action

    def validate(self):
        if self.status_code == 200 and (
            self.body.status == "1" and self.body.message == "OK"
        ):
            return self
        elif self.status_code == 200 and (
            self.body.status == "0" or self.body.message == "NOTOK"
        ):
            msg = f"Incorrect Request for (module: {self.module}) & (action: {self.action})"
            raise EtherscanRequestError(message=msg, response=self)
        else:
            msg = (
                f"Etherscan Error for (module: {self.module}) & (action: {self.action})"
            )
            raise EtherscanApiError(message=msg, response=self)


class EtherscanClientError(Exception):
    """Base error class for Etherscan errors"""


class EtherscanRequestError(EtherscanClientError):
    def __init__(self, message: str, response: EtherscanResponse):
        msg: str = f"""
        message : {message}\n
        the server responded with :
        status  : {response.body.status}
        message : {response.body.message}
        result  : {response.body.result}
        url     : {response.url}
        """
        super(EtherscanClientError, self).__init__(msg)


class EtherscanApiError(EtherscanClientError):
    def __init__(self, message: str, response: EtherscanResponse):
        msg: str = f"""
        message : {message}\n
        the server responded with :
        code    : {response.status_code}
        status  : {response.body.status}
        message : {response.body.message}
        result  : {response.body.result}
        url     : {response.url}
        """
        super(EtherscanClientError, self).__init__(msg)
