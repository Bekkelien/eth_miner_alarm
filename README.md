# ETH miner hasrate alarm/monitoring

Only tested for api from nanominer, sends a email over mail.py (custom) when eth hasrate are lower the set limit

### Needs to have your spesific ETH_ADRESS

```python
nanominer_api = "https://api.nanopool.org/v1/eth/reportedhashrate/ETH_ADRESS"
```

### Bug (Time formate is off se example)
```shell
Last reported hashrate: 471.558 Time: 13:29:2
```
