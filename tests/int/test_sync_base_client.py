import pytest

from etherscan import url
from etherscan.client.sync_base_client import SyncBaseClient


@pytest.fixture(scope="module")
def etherscan_client():
    return SyncBaseClient(
        api_key="IZQSBAU5K6P5F957QEU1DHTAGMBH4SJQXD", base_url=url.BASE_MAINNET
    )


@pytest.mark.parametrize(
    "params,status,message,status_code",
    [
        (
            {
                "module": "account",
                "action": "balance",
                "address": "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae",
                "tag": "latest",
            },
            "1",
            "OK",
            200,
        ),
        (
            {
                "module": "fake",
                "action": "balance",
                "address": "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae",
                "tag": "latest",
            },
            "0",
            "NOTOK",
            200,
        ),
    ],
)
def test_api_call(
    etherscan_client: SyncBaseClient,
    params: dict,
    status: str,
    message: str,
    status_code: int,
):
    response = etherscan_client.api_call(params=params)
    assert response.status_code == status_code
    assert response.body.status == status
    assert response.body.message == message
