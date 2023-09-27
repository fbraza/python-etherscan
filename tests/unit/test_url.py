import pytest

from etherscan import url


@pytest.mark.parametrize(
    "params,base_url,expected_url",
    [
        (
            {
                "module": "account",
                "action": "balance",
                "address": "0xde0b2",
                "tag": "latest",
                "apikey": "4cb697bae",
            },
            url.BASE_MAINNET,
            "https://api.etherscan.io/api?module=account&action=balance&address=0xde0b2&tag=latest&apikey=4cb697bae",
        ),
        (
            {
                "action": "balance",
                "module": "account",
                "tag": "latest",
                "address": "0xde0b2",
                "apikey": "4cb697bae",
            },
            url.BASE_GOERLI,
            "https://api-goerli.etherscan.io/api?action=balance&module=account&tag=latest&address=0xde0b2&apikey=4cb697bae",
        ),
        (
            {
                "action": "balance",
                "module": "account",
                "tag": "latest",
                "address": "0xde0b2",
                "apikey": "4cb697bae",
            },
            url.BASE_SEPOLIA,
            "https://api-sepolia.etherscan.io/api?action=balance&module=account&tag=latest&address=0xde0b2&apikey=4cb697bae",
        ),
    ],
)
def test_build_url(params, base_url, expected_url):
    _url = url.build(params, base_url)
    assert _url == expected_url
