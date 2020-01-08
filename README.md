CPUchain tipbot
====

A discord Tip-bot for CPUchain, forked from [tip-sugar](https://github.com/ilmango-doge/Tip-Sugar)

## Usage

Command prefix : `//`

|Command                         |Description                                  |Example                                            |
|--------------------------------|---------------------------------------------|---------------------------------------------------|
|`//info`                        |Show information of CPUchain.                |                                                   |
|`//help`                        |Show help message.                           |                                                   |
|`//balance`                     |Show your balances.                          |                                                   |
|`//deposit`                     |Show your deposit address.                   |                                                   |
|`//tip (@mention) (amount)`     |Tip specified amount to specified user.      |`//tip @minkcrypto 3.939`                          |
|`//withdraw (address) (amount)` |Send specified amount to specified address.  |`//withdraw CPUchainNazbFd9aWN8GF4AaMSFHe1ntne 10` |
|`//withdrawal (address)`        |Send your all balances to specified address. |`//withdrawal CPUchainNazbFd9aWN8GF4AaMSFHe1ntne`  |

### Tips

withdraw-fee is 0.001 CPU by default.

Number of Confirmations is 6 blocks.

In `withdraw`, amount must be at least 0.5 CPU.

You can use CPUchain tipbot on DM.

You can donate by tip to CPUchain tipbot. (example : /tip @CPUchain tipbot 3.939)

The address changes with each deposit, but you can use the previous one. However, it is recommended to use the latest address.

## Licence

[MIT](https://github.com/cpuchain/tipbot/blob/master/LICENSE)

## Requirement

* Python 3.5.3 or higher
* [discord.py](https://github.com/Rapptz/discord.py) (rewrite)
* [python-bitcoinrpc](https://github.com/jgarzik/python-bitcoinrpc)

```
python3 -m pip install -U discord.py
```

```
python3 -m pip install python-bitcoinrpc
```

## How to run

1. Edit `config.py`

2. Edit configuration file of coind (bitcoin.conf etc.)

```
daemon=1
server=1
rpcuser={same as config.py}
rpcpassword={same as config.py}
```

3. Run `tipcpu.py`

```
python3 tipcpu.py
```
