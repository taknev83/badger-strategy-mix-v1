from brownie import *

from config import (
    BADGER_DEV_MULTISIG,
    WANT,
    LP_COMPONENT,
    REWARD_TOKEN,
    PROTECTED_TOKENS,
    FEES,
)
from dotmap import DotMap


def main():
    return mockSwap()


def mockSwap():
    deployer = accounts[0]
    router = Contract.from_explorer("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D")
    router.swapExactETHForTokens(
        0,  ## Mint out
        ["0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", WANT],
        deployer,
        9999999999999999,
        {"from": deployer, "value": 5000000000000000000},
    )
