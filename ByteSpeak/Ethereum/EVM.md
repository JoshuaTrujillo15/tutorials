# Ethereum Virtual Machine

To understand the Ethereum protocol,
you will need to understand the basics of blockchain,
distributed computing, and cryptography.

---

## The Cryptography

Cryptography is a niche field of mathematics, but it is becoming invaluable in
the age of information.
Blockchains, as mentioned later, rely on some strong cryptographic primitives,
or core algorithms.
Only algorithms specifically applicable to the Ethereum protocol will be
mentioned in this document.

### Cryptographic Hash Functions

Cryptographic hash functions serve as checksums that are extremely difficult to
forge.
These functions take an arbitrary amount of data as in input, and the output a
deterministic, fixed length 'hash digest'.
Cryptographic Hash Functions are **one-way**, meaning the digest can not be used
to calculate the input without brute force.

**Important cryptographic hash function properties include:**

- deterministic, the same input MUST create the same digest

- quick to calculate the digest

- infeasible to create two identical digests from different inputs

- infeasible to reverse the function (without brute force)

- a small input change should completely change the output

**Common Examples Include:**

SHA256 is an industry standard, it is used by the Bitcoin Protocol, HTTPS, and
others.
It belongs to the Secure Hashing Algorithm (SHA) family of hash functions,
specifically, the SHA-2 family.

Keccak256 is used by the Ethereum protocol.
It is also in the SHA family, specifically SHA-3.

Both take an input of any length and output a digest of 256 bits, or 32 bytes.

256 bits yields `(2^256)`, or `(1.16 * 10^77)` different possilble digests. 

For scale, the estimated number of protons in the observable universe is:

`(1.57 * 10^80)`.

### Digital Signatures

Digital signatures are mathematical schemes used to ensure data authenticity, to
authenticate a user, and to protect against copying/forging new signatures.

The scheme most often uses a **trapdoor-function**, or a number easy to
calculate one way, but infeasible to calculate another way.

This relies on a public and private key pair.

The private key, is further referred to as secret key for unambiguous notation
like this:`(sK, pK)`.

The public key is derived from the secret key via the trapdoor function.
Common schemes include some variation of Modular Exponentiation.

An analogy for modular exponentiation is how 12 hour clocks work.

    If a 12 hour clock reads '2:00',
    this could mean either 2:00 or 14:00.

    Imagine if there were 48 hours in a day.
    A 12 hour clock reading '2:00' could
    mean 2:00, 14:00, 26:00, or 38:00!

    Exponentiation means the 'hour', or secret key
    is raised to the power of a massive number. 

    Modulo means we confine that massive number to a
    finite field, similar to how a 12 hour clock
    is a finite field containing 24 possible hours.

This is all a bit simplified, but this is the concept that lets a user derive
a public key from a private key.

To sign a message, the message's data is hashed, and the signature is
generated on the hash with the private key. Remember that changing the message
will change the hash digest, rendering the digital signature invalid.

To verify a signature, the validator only needs the derived public key, the
message hash, and the signature.

---

## Blockchain Basics

Blockchain is not a new technology, the concept is that new blocks should
include a checksum of the previous block's data so that if any previous block is
ever changed, the checksum would change on each subsequent block or become
invalid.

For cryptocurrency blockchains, strong cryptographic primitives are used to
ensure it is computationally infeasible to ever spoof, change, or forge a 
transaction history.

Here is a simplified JSON representation of a block:

```javascript

blockchain: {[

    // ...

    {
        previousBlocksHash: '0x0123456789ABCDEF',

        transaction: {
            senderAddress: '0x0123456789ABCDEF',
            recipientAddress: '0xFEDCBA9876543210',
            amount: 100,
            timestamp: '1621190194'
        },

        signatureData: {
            transactionSignature: '0xFEDCBA9876543210',
            transactionHash: '0x0123456789ABCDEF'
        },
    },

    // ...

]}

```

This represents the cryptographic hash of the previous block in the chain:
```javascript
previousBlocksHash: '0x0123456789ABCDEF'
```

This represents the transaction. It includes the public keys of both the sender
and the recipient.

User balances are determined by how many coins are sent to and received by their
public keys.
```javascript
transaction: {
    senderAddress: '0x0123456789ABCDEF',
    recipientAddress: '0xFEDCBA9876543210',
    amount: 100,
    timestamp: '1621190194'
},
```

This represents the digital signature, consisting of the transaction hash and
the signature provided by the sender.
```javascript
signatureData: {
    transactionSignature: '0xFEDCBA9876543210',
    transactionHash: '0x0123456789ABCDEF'
}
```

### Consensus

Consensus is needed to ensure every single miner and node has the same exact
transaction history.

These schemes deserve hours of study each to fully grasp, so this document won't
be detailing them. Just know that these ensure the transaction history and order
is agreed upon and easily verified.

Here are 

- Proof of Work
- Proof of Stake
- Proof of Elapsed Time
- Proof of (Time and) Space

Ethereum currently uses Proof of Work, but Ethereum 2.0 intends to move to Proof
of Stake by the end of 2021.

---

## The Ethereum Virtual Machine

The Ethereum Virtual Machine, or EVM, represents a global computer consisting of
every miner on the Ethereum network.

In the Bitcoin protocol, each new block updates the current balances of all
users on the network.

In the Ethereum protocol, each new block updates a global 'state', consisting of
the balances of all users on the network AND the state of smart contracts.

This is where the Ethereum protocol really stands out.

A transaction on the Ethereum network can be one of two types, one is a simple
transfer of 'Ether' from one account to another and the other is a smart
contract.

### Ether

When people refer to 'Ethereum', most often they are referring to 'Ether', or
the native currency of the Ethereum network.

Ether is used for many low-level transactions, smart contract deployments,
transaction fees, and other things.

### Smart Contract Overview

Smart contracts are special instructions for the EVM to execute when the block
containing it is mined. 

---

## Smart Contracts

Smart Contracts have proven to be incredibly useful for the development of the
cryptocurrency ecosystem.
These can be used to create 'tokens' which are enforcable with the security and
finality of the Ethereum blockchain.

### Languages

There are a few languages used to write smart contracts, the most popular is
Solidity. However, Solidity code cannot be sent as instructions to the EVM as
is.
The Solidity code is compiled to bytecode, which is sent to the network to be 
used as instructions in the block.

### Fungible Tokens

Fungible tokens, or tokens that are each equivalent in value, function as
'sub-currencies' in the Ethereum network.

Popular examples include:
- Tether (USDT)
- Uniswap (UNI)
- Basic Attention Token (BAT)

Other cryptocurrencies can be 'wrapped' and exchanged on the Ethereum network,
meaning anything from Bitcoin to US Dollars can be exchanged via the network.

### Non-Fungible Tokens (NFT's)

Non-Fungible Tokens, or NTF's, are unique tokens, not necessarily equivalent in
value.

Popular NFT uses include:
- digital art
- real estate deeds
- game items

The NFT community is still very young and shows a lot of potential for many use
cases.

---

