# queruntine

Python asks **Ru**st to **que**ry a database concurre**nt**ly.

## UNDER CONSTRUCTION

This may take a few weeks.

## Prototype API

```
from queruntine import Runner

conn_str = 'mongodb://localhost:27017'
queries = ['rust_basics.guesses.find({})']

runner = Runner(conn_str, queries)

runner.run()
```
