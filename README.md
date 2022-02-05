# ETH miner hashrate alarm/monitoring

## Needs to have your spesific ETH_ADRESS and email in config

### nanominer.py for hashrate warning
```python
ETH = "ETH_ADRESS"
```

### ehtermine.py for hashrate warning 
Expect up to 10min delay, still way 'better' then ethermine's alarm system

Note 
* That if we can't send email it will crash, add inn retry on send email
* Datetime is now for every print, make a function in the future

```python
ETH = "ETH_ADRESS"
```

### Rename config 
Rename config.default.yaml to config.yaml and enter information in config, NB pwd are in cleartxt, so use a disposable email adress to send from 

``` shell
mail:
  to: "TEST@example.com"
  from: "test@example.com"
  pwd: "pwd"
  smtp: "smtp.xxxx.com"
```
