// SPDX-License-Identifier: AGPL-3.0-only
pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

import "deps/@uma/core/contracts/financial-templates/expiring-multiparty/Liquidatable.sol";

/**
 * @title Expiring Multi Party.
 * @notice Convenient wrapper for Liquidatable.
 */
contract ExpiringMultiParty is Liquidatable {
    /**
     * @notice Constructs the ExpiringMultiParty contract.
     * @param params struct to define input parameters for construction of Liquidatable. Some params
     * are fed directly into the PricelessPositionManager's constructor within the inheritance tree.
     */
    constructor(ConstructorParams memory params)
        public
        Liquidatable(params)
    // Note: since there is no logic here, there is no need to add a re-entrancy guard.
    {

    }
}
