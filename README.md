# dbt-devnull
A do-nothing dbt adapter plugin.

Following commands should be succesul if configuration is correct withou any database connection
- dbt debug
- dbt docs generate

## Install
```
pip install dbt-devnull
```

## Configuration
A sample profile configuration
```
test:
  target: test
  outputs:
    test:
      type: devnull
      schema: test
      database: test
      username: user
      password: password
      host: localhost
      threads: 1
```

