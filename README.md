# queruntine

Python asks **Ru**st to **que**ry a database concurre**nt**ly.

## UNDER CONSTRUCTION

This may take a few weeks.

## Prototype API

```
from queruntine import Runner

runner = Runner()

runner.connection_string = 'foo'
runner.queries = ['fee', 'fi', 'foe', 'fum']

runner.run()
```
