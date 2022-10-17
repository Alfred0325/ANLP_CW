# ANLP_CW
This is for ANLP CW
~~~
// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;


contract Bank {
    mapping(address => uint256) balance; // check the amount of coins deposited for the calling account, mapping from an account address to a value
    address[] public customers; //the account addresses, which is an array of addresses

    //stores the arguments passed in Deposit transaction logs, the customer is the account address, the message here is a string stored in memory
    event Deposit(address customer, string message); 
    event Withdrawal(address customer); //stores the arguments passed in Withdrawal transaction logs

    function deposit(string memory message) public payable { // this function deposit a specified value of coins, the message here is a string stored in memory
        require(msg.value > 10); // msg.value the value to be deposited. This line is to check the value to be deposited is larger than 10 wei
        balance[msg.sender] += msg.value - 10; // msg.sender is to access the calling account. This line is to deduct 10 wei for a base fee for every time deposit

        customers.push(msg.sender);

        emit Deposit(msg.sender, message); // call Deposit event
    }

    function withdraw() public { // this function withdraw the money deposited 
        uint256 b = balance[msg.sender]; // get the amount of coins deposited for the calling account
        balance[msg.sender] = 0; // for security, set the balance of this calling account to be 0
        payable(msg.sender).transfer(b); // transfer the amount of deposited coins back to the calling account

        emit Withdrawal(msg.sender);// call Withdrawal event
    }

    function getBalance() public view returns (uint256) {// this function is to return the amount of coins deposited form the calling account
        return balance[msg.sender];
    }
    
    function empty() public { // this function is to transfer all the balance to the contract's owner
        require(msg.sender == customers[0]);
        
        payable(msg.sender).transfer(address(this).balance);
    }
}
~~~
