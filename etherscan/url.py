import urllib

BASE_MAINNET: str = "https://api.etherscan.io/api"
BASE_GOERLI: str = "https://api-goerli.etherscan.io/api"
BASE_SEPOLIA: str = "https://api-sepolia.etherscan.io/api"


def build(params: dict, base_url: str) -> str:
    query_params = urllib.parse.urlencode(params)  # type: ignore
    url = f"{base_url}?{query_params}"
    return url
