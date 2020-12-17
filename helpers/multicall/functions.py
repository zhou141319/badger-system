from enum import Enum

from dotmap import DotMap


def as_wei(value):
    return value


erc20 = DotMap(
    balanceOf="balanceOf(address)(uint256)", totalSupply="totalSupply()(uint256)"
)
sett = DotMap(
    getPricePerFullShare="getPricePerFullShare()(uint256)",
    available="available()(uint256)",
    balance="balance()(uint256)",
    controller="controller()(address)",
    strategist="strategist()(address)",
    keeper="keeper()(address)",
)
strategy = DotMap(
    balanceOfPool="balanceOfPool()(uint256)",
    balanceOfWant="balanceOfWant()(uint256)",
    balanceOf="balanceOf()(uint256)",
    isTendable="isTendable()(bool)",
    getProtectedTokens="getProtectedTokens()(address[])",
    getName="getName()(string)",
    withdrawalFee="withdrawalFee()(uint256)",
    performanceFeeGovernance="performanceFeeGovernance()(uint256)",
    performanceFeeStrategist="performanceFeeStrategist()(uint256)",
)
harvestFarm = DotMap(earned="earned()(uint256)")
rewardPool = DotMap(
        # claimable rewards
        earned="earned(address)(uint256)",
        # amount staked
        balanceOf="balanceOf(address)(uint256)",
)

func = DotMap(erc20=erc20, sett=sett, strategy=strategy, rewardPool=rewardPool,)
