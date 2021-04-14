// SPDX-License-Identifier: MIT
pragma solidity >=0.5.0 <0.8.0;

interface ISett {
    function token() external view returns (address);

    function deposit(uint256) external;

    function depositFor(address, uint256) external;

    function depositAll() external;

    function withdraw(uint256) external;

    function withdrawAll() external;

    function earn() external;

    function claimInsurance() external; // NOTE: Only yDelegatedVault implements this

    function getPricePerFullShare() external view returns (uint256);
}
