// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openZeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    constructor(uint256 initialSupply) public ERC20 ("simpToken", "smpT") {
    // constructor(uint256 initialSupply, string memory _name, string memory _symbol) public ERC20(_name, _symbol) {
        _mint(msg.sender, initialSupply);
    }

    // function sendo() {
    //     msg.sender.send(1 ether/ 2);
    // }
}
