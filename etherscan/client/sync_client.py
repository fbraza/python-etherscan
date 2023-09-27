"""_summary_"""

from etherscan import actions
from etherscan.client.sync_base_client import SyncBaseClient


class Client(SyncBaseClient):
    LOGS = actions.Logs()
    STATS = actions.Stats()
    PROXY = actions.Proxy()
    TOKENS = actions.Tokens()
    BLOCKS = actions.Blocks()
    ACCOUNTS = actions.Accounts()
    CONTRACTS = actions.Contracts()
    GASTRACKER = actions.GasTracker()
    TRANSACTIONS = actions.Transactions()

    def get_eth_balance_by_adress(self, address: str, tag: str, **kwargs):
        kwargs.update({"address": address, "tag": tag})
        return self.api_call(params=kwargs)
