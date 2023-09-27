import pytest

from etherscan import url
from etherscan.client import sync_client


@pytest.fixture(scope="module")
def etherscan_client():
    return sync_client.Client(
        api_key="IZQSBAU5K6P5F957QEU1DHTAGMBH4SJQXD", base_url=url.BASE_MAINNET
    )


def test_get_eth_balance_by_adress(etherscan_client: sync_client.Client):
    response = etherscan_client.get_eth_balance_by_adress(
        address="0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae", tag="latest"
    )
    assert response.status_code == 200
