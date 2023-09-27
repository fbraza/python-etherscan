"""_summary_"""


import logging

import requests

from etherscan import url
from etherscan.response import EtherscanResponse, EtherscanResult


class SyncBaseClient:
    """_summary_"""

    def __init__(
        self,
        api_key: str,
        base_url: str,
        headers: None | dict = None,
        timeout: int = 30,
        logger: None | logging.Logger = None,
    ):
        """_summary_

        Args:
            api_key (str): _description_
            base_url (str): _description_
            headers (None | dict, optional): _description_. Defaults to None.
            logger (None | logging.Logger, optional): _description_. Defaults to None.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = headers or {}
        self.timeout = timeout
        # add the user agent in headers
        self.logger = logger if logger is not None else logging.getLogger(__name__)

    def api_call(
        self,
        params: dict,
        headers: None | dict = None,
    ) -> EtherscanResponse:
        headers = headers or {}
        headers.update(self.headers)
        params["apikey"] = self.api_key
        api_url: str = url.build(params=params, base_url=self.base_url)
        etherscan_response = self._send_request_and_parse_response(
            api_url=api_url, headers=headers
        )
        return etherscan_response

    def _send_request_and_parse_response(
        self,
        api_url: str,
        headers: dict,
    ) -> EtherscanResponse:
        etherscan_response = requests.get(
            url=api_url, headers=headers, timeout=self.timeout
        )
        return EtherscanResponse(
            request_url=etherscan_response.url,
            http_method=etherscan_response.request.method,
            status_code=etherscan_response.status_code,
            response_headers=etherscan_response.headers,
            etherscan_body=EtherscanResult.model_validate_json(
                etherscan_response.json()
            ),
        ).validate()
