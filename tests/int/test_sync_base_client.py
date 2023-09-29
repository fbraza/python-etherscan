import pytest

from etherscan_client.api import url
from etherscan_client.api.sync_base_client import SyncBaseClient


@pytest.fixture(scope="module")
def etherscan_client():
    return SyncBaseClient(
        api_key="IZQSBAU5K6P5F957QEU1DHTAGMBH4SJQXD", base_url=url.BASE_MAINNET
    )


@pytest.mark.parametrize(
    "module,action,params,status,message,status_code",
    [
        (
            "account",
            "balance",
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
            "block",
            "getblockreward",
            {
                "module": "block",
                "action": "getblockreward",
                "blockno": "2165403",
            },
            "1",
            "OK",
            200,
        ),
    ],
)
def test_api_call(
    etherscan_client: SyncBaseClient,
    module: str,
    action: str,
    params: dict,
    status: str,
    message: str,
    status_code: int,
):
    response = etherscan_client.api_call(module=module, action=action, params=params)
    assert response.status_code == status_code
    assert response.body.status == status
    assert response.body.message == message
    assert response.module == module
    assert response.action == action
