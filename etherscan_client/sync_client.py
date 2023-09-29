"""_summary_"""

from etherscan_client.api import actions, modules
from etherscan_client.api.response import EtherscanResponse
from etherscan_client.api.sync_base_client import SyncBaseClient


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
        """Returns the Ether balance in Wei of a given address.

        Args:
            address (str): _description_
            tag (str): _description_

        Returns:
            EtherscanResponse: _description_
        """
        module, action = modules.ACCOUNT, self.ACCOUNTS.balance
        kwargs.update(
            {"module": module, "action": action, "address": address, "tag": tag}
        )
        return self.api_call(module=module, action=action, params=kwargs)

    def get_eth_balance_from_multiple_address(
        self, address: list[str], tag: str, **kwargs
    ) -> EtherscanResponse:
        """Returns the balance of the accounts in Wei from a list of addresses.

        Args:
            address (list[str]): _description_
            tag (str): _description_

        Returns:
           EtherscanResponse
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
        """Returns the list of transactions performed by an address, with optional pagination.

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
        """Returns the list of internal transactions performed by an address, with optional pagination.

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

    def list_internal_transaction_by_hash_transaction(
        self, transaction_hash: str, **kwargs
    ) -> EtherscanResponse:
        """Returns the list of internal transactions performed within a transaction.

        Args:
            transaction_hash (str): _description_

        Returns:
            EtherscanResponse: _description_
        """
        module, action = modules.ACCOUNT, self.ACCOUNTS.tx_list_internal
        kwargs.update({"transaction_hash": transaction_hash})
        return self.api_call(module=module, action=action, params=kwargs)

    def list_internal_transaction_by_block_range(
        self,
        address: str,
        startblock: int,
        endblock: int,
        page: int,
        offset: int,
        sort: str,
        **kwargs
    ) -> EtherscanResponse:
        """Returns the list of internal transactions performed within a block range, with optional pagination.

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
