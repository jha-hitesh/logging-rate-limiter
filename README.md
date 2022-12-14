# logging-rate-limiter

a simple logging filter which can be used to limit the amount of logs getting out from a system.
It uses token bucket algorithm internally.


#### Installation

- from pypi
```
pip install logging_rate_limiter
```

#### Usage
- check [example](tests/test_logging.py) for a complete example
- the filter is available as
```
from logging_rate_limiter.utils import RateLimitingFilter
```
- on a basic level this filter can be added to a logger or a logging handler
- this filter takes multiple optional keywords with key as log_level and value as a dict with 3 keys
```
"DEBUG": {
    "tokens_per_sec": 1,
    "starting_tokens": 1, # optional, default=0
    "max_tokens_balance": 1 # optional, default=infinity
}
```
- `tokens_per_sec`: the number of tokens(logs) which will be available for a given log level
- `starting_tokens`: the number of tokens already available at the start of the logging initialisation
- `max_tokens_balance`: the maximum number of tokens that can be accumulated if the logs for a particular level are not being requested as much as the `tokens_per_sec` allowed. kind of limited burst balance.
- besides providing this config for particular log levels, you can supply a `default` key with this config.
- if a `default` is supplied and there is no config supplied for a requested log level then this requested log level will be checked against this default config. useful for scenario where you want an overall rate shared across multiple log levels.
- besides this an optional `result_callback` can be supplied which will be called everytime a log record goes through filter function
- the `result_callback` must accept 2 params `result` which is a boolean telling whether the log record was filtered or not and `record` the original log record.

#### Pytest

- pytest tests/

#### License

- this project is licensed under [MIT License](LICENSE)