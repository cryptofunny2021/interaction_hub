# Interaction Hub


**قرارداد مرکزی اکوسیستم SocialFi**

**Contract Address:**  
`0xF4f25C67D8aaa24A71E85C9cCF61c5c1a8F2f8b1`

## 🚀 قابلیت جدید (v0.2.3)
- حالا مستقیم به **Reputation Scoring** و **Dynamic Token** متصل است.
- هر بار که `record_interaction()` صدا زده شود:
  - ۱۰ امتیاز Reputation اضافه می‌شود.
  - ۵ توکن پاداش Mint می‌شود.

## نحوه استفاده
```python
from genlayer import *

hub = gl.contract("0xF4f25C67D8aaa24A71E85C9cCF61c5c1a8F2f8b1")
hub.record_interaction()   #
تعامل ثبت + پاداش
# =====
A GenLayer smart contract for recording user interactions.

## Features

* Record interactions
* Count interaction activity
* Retrieve interaction totals

## Files

* contract.py

## Network

GenLayer Testnet

## Author

cryptofunny2021

## Main Ecosystem Repository

https://github.com/cryptofunny2021/genlayer-socialfi-ecosystem

## Related Contracts

This contract is part of a larger GenLayer ecosystem.

### Ecosystem Repositories

* Reputation Scoring
  https://github.com/cryptofunny2021/reputation_scoring

* Dynamic Token
  https://github.com/cryptofunny2021/dynamic_token

* Dispute Resolution
  https://github.com/cryptofunny2021/dispute_resolution

* Interaction Hub
  https://github.com/cryptofunny2021/interaction_hub

* Task Marketplace
  https://github.com/cryptofunny2021/task_marketplace
