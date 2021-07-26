# ETH miner hasrate alarm/monitoring

Only tested for api from nanominer, sends a email over mail.py (custom) when eth hasrate are lower the set limit

### Needs to have your spesific ETH_ADRESS

```python
nanominer_api = "https://api.nanopool.org/v1/eth/reportedhashrate/ETH_ADRESS"
```

### Rename config 
Rename config.default.yaml to config.yaml and enter information in config, NB pwd are i cleartxt, so use a disposable email adress to send from 

``` shell
mail:
  to: "TEST@example.com"
  from: "test@example.com"
  pwd: "pwd"
  smtp: "smtp.xxxx.com"
```
