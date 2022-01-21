// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

interface GuestListAPI {
    function authorized(address guest, uint256 amount)
        external
        view
        returns (bool);
}
