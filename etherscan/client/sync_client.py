"""_summary_"""

from etherscan import actions, modules
from etherscan.client.sync_base_client import SyncBaseClient
from etherscan.response import EtherscanResponse


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

    def get_eth_balance_by_address(
        self, address: str, tag: str, **kwargs
    ) -> EtherscanResponse:
        module, action = modules.ACCOUNT, self.ACCOUNTS.balance
        kwargs.update(
            {"module": module, "action": action, "address": address, "tag": tag}
        )
        return self.api_call(module=module, action=action, params=kwargs)

    def get_eth_balance_from_multiple_address(
        self, address: list[str], tag: str, **kwargs
    ) -> EtherscanResponse:
        """_summary_

        Args:
            address (list[str]): _description_
            tag (str): _description_

        Returns:
            _type_: _description_
        """
        module, action = modules.ACCOUNT, self.ACCOUNTS.balance_multi
        kwargs.update(
            {
                "module": module,
                "action": action,
                "address": ",".join(address),
                "tag": tag,
            }
        )
        return self.api_call(module=module, action=action, params=kwargs)

    def list_transaction_by_address(
        self,
        address: str,
        startblock: int,
        endblock: int,
        page: int,
        offset: int,
        sort: str,
        **kwargs
    ) -> EtherscanResponse:
        """_summary_

        Args:
            address (str): _description_
            startblock (int): _description_
            endblock (int): _description_
            page (int): _description_
            offset (int): _description_
            sort (str): _description_

        Returns:
            EtherscanResponse: _description_
        """
        if sort not in ["asc", "desc"]:
            sort = "desc"

        module, action = modules.ACCOUNT, self.ACCOUNTS.tx_list
        kwargs.update(
            {
                "module": module,
                "action": action,
                "address": address,
                "startblock": startblock,
                "endblock": endblock,
                "page": page,
                "offset": offset,
                "sort": sort,
            }
        )
        return self.api_call(module=module, action=action, params=kwargs)

    def list_internal_transaction_by_address(
        self,
        address: str,
        startblock: int,
        endblock: int,
        page: int,
        offset: int,
        sort: str,
        **kwargs
    ) -> EtherscanResponse:
        """_summary_

        Args:
            address (str): _description_
            startblock (int): _description_
            endblock (int): _description_
            page (int): _description_
            offset (int): _description_
            sort (str): _description_

        Returns:
            EtherscanResponse: _description_
        """
        if sort not in ["asc", "desc"]:
            sort = "desc"

        module, action = modules.ACCOUNT, self.ACCOUNTS.tx_list_internal
        kwargs.update(
            {
                "module": module,
                "action": action,
                "address": address,
                "startblock": startblock,
                "endblock": endblock,
                "page": page,
                "offset": offset,
                "sort": sort,
            }
        )
        return self.api_call(module=module, action=action, params=kwargs)
