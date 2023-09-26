from enum import Enum


class Modules(Enum):
    account: str = "account"
    contract: str = "contract"
    transaction: str = "transaction"
    block: str = "block"
    logs: str = "logs"
    proxy: str = "proxy"
    token: str = "token"
    gastracker: str = "gastracker"
    stats: str = "stats"


class Accounts(Enum):
    balance: str = "balance"
    balance_multi: str = "balancemulti"
    tx_list: str = "txlist"
    tx_list_internal: str = "txlistinternal"
    token_tx: str = "tokentx"
    token_nft_tx: str = "tokennfttx"
    token_1155_tx: str = "token1155tx"
    get_mined_blocks: str = "getminedblocks"
    txs_Beacon_Withdrawal: str = "txsBeaconWithdrawal"
    balance_history: str = "balancehistory"
    token_balance: str = "tokenbalance"
    token_balance_history: str = "tokenbalancehistory"
    address_token_balance: str = "addresstokenbalance"
    address_token_nft_balance: str = "addresstokennftbalance"
    address_token_nft_inventory: str = "addresstokennftinventory"


class Contracts(Enum):
    get_abi: str = "getabi"
    get_source_code: str = "getsourcecode"
    get_contract_creation: str = "getcontractcreation"


class Transactions(Enum):
    get_status: str = "getstatus"
    get_tx_receipt_status: str = "gettxreceiptstatus"


class Blocks(Enum):
    get_block_reward: str = "getblockreward"
    get_block_countdown: str = "getblockcountdown"
    get_block_no_by_time: str = "getblocknobytime"


class Logs(Enum):
    get_logs: str = "getLogs"


class Proxy(Enum):
    eth_block_number: str = "eth_blockNumber"
    eth_get_block_by_number: str = "eth_getBlockByNumber"
    eth_get_uncle_by_block_number_and_index: str = "eth_getUncleByBlockNumberAndIndex"
    eth_get_block_transaction_count_by_number: str = (
        "eth_getBlockTransactionCountByNumber"
    )
    eth_get_transaction_by_hash: str = "eth_getTransactionByHash"
    eth_get_transaction_by_block_number_and_index: str = (
        "eth_getTransactionByBlockNumberAndIndex"
    )
    eth_get_transaction_count: str = "eth_getTransactionCount"
    eth_send_raw_transaction: str = "eth_sendRawTransaction"
    eth_get_transaction_receipt: str = "eth_getTransactionReceipt"
    eth_call: str = "eth_call"
    eth_get_code: str = "eth_getCode"
    eth_gas_price: str = "eth_gasPrice"
    eth_estimate_gas: str = "eth_estimateGas"
    # experimental action
    eth_get_storage_at: str = "eth_getStorageAt"


class Tokens(Enum):
    pass


class GasTracker(Enum):
    gasestimate: str = "gasestimate"
    gasoracle: str = "gasoracle"


class Stats(Enum):
    pass
