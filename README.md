# ETH miner hasrate/workers alarm/monitoring

## Needs to have your spesific ETH_ADRESS and email in config

### nanominer.py for hashrate warning
```python
ETH = "ETH_ADRESS"
```

### ehtermine.py for active workers warning

Note that if we can't send email it will crash, add inn retry on send email

```python
WORKERS = 4
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
