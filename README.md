# ETH miner hashrate alarm/monitoring

### Configuration
Rename config.default.yaml to config.yaml and enter information in config, NB pwd are in cleartxt, so use a disposable email adress to send from 

``` shell
mail:
  to: "test@example.com"
  from: "test@example.com"
  pwd: "pwd"

eth:
  nanominer: "xxxx"
  ethermine: "xxxx"
```

### nanominer.py for hashrate warning

### ehtermine.py for hashrate warning 
Expect up to 10min delay, still way 'better' then ethermine's alarm system

Note:
- [x] That if we can't send email it will crash, add inn retry on send email
- [ ] Datetime is now for every print, make a function in the future


