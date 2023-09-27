import pydantic
from requests.structures import CaseInsensitiveDict

from etherscan import errors


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
    ):
        self.url = request_url
        self.method = http_method
        self.status_code = status_code
        self.headers = response_headers
        self.body = etherscan_body

    def validate(self):
        if self.status_code == 200 and (
            self.body.status == "1" and self.body.message == "OK"
        ):
            return self
        elif self.status_code == 200 and (
            self.body.status == "0" or self.body.message == "NOTOK"
        ):
            msg = "Incorrect Request "
            raise errors.EtherscanApiError(message=msg, response=self)
        else:
            msg = f"Etherscan API Error for (url: {self.url})"
            raise errors.EtherscanApiError(message=msg, response=self)
