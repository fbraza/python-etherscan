"""_summary_
"""

BASE_MAINNET: str = "https://api.etherscan.io/api"
BASE_GOERLI: str = "https://api-goerli.etherscan.io/api"
BASE_SEPOLIA: str = "https://api-sepolia.etherscan.io/api"


def build(params: dict, base_url: str) -> str:
    """_summary_

    Args:
        params (dict): _description_
        base_url (str): _description_

    Returns:
        str: _description_
    """
    query_params = "&".join([f"{k}={v}" for k, v in params.items()])  # type: ignore
    url = f"{base_url}?{query_params}"
    return url
