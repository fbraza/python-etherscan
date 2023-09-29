import pytest

from etherscan_client import sync_client
from etherscan_client.api import url


@pytest.fixture(scope="module")
def etherscan_client():
    return sync_client.Client(
        api_key="IZQSBAU5K6P5F957QEU1DHTAGMBH4SJQXD", base_url=url.BASE_MAINNET
    )


def test_get_eth_balance_by_address(etherscan_client: sync_client.Client):
    etherscan_response = etherscan_client.get_eth_balance_by_address(
        address="0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae", tag="latest"
    )
    assert etherscan_response.status_code == 200
    assert etherscan_response.body.status == "1"
    assert etherscan_response.body.message == "OK"


def test_get_eth_balance_from_multiple_address(etherscan_client: sync_client.Client):
    address = [
        "0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a",
        "0x63a9975ba31b0b9626b34300f7f627147df1f526",
        "0x198ef1ec325a96cc354c7266a038be8b5c558f67",
    ]
    etherscan_response = etherscan_client.get_eth_balance_from_multiple_address(
        address=address, tag="latest"
    )
    assert etherscan_response.status_code == 200
    assert etherscan_response.body.status == "1"
    assert etherscan_response.body.message == "OK"


def test_list_transaction_by_address(etherscan_client: sync_client.Client):
    etherscan_response = etherscan_client.list_transaction_by_address(
        address="0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a",
        startblock=0,
        endblock=99999999,
        page=2,
        offset=10,
        sort="asc",
    )
    assert etherscan_response.status_code == 200
    assert etherscan_response.body.status == "1"
    assert etherscan_response.body.message == "OK"


def test_list_internal_transaction_by_address(etherscan_client: sync_client.Client):
    etherscan_response = etherscan_client.list_internal_transaction_by_address(
        address="0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a",
        startblock=0,
        endblock=99999999,
        page=1,
        offset=10,
        sort="asc",
    )
    assert etherscan_response.status_code == 200
    assert etherscan_response.body.status == "1"
    assert etherscan_response.body.message == "OK"
