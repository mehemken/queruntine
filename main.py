#!/usr/bin/env python

# How should the API look?

from queruntine import Runner

runner = Runner()

runner.connection_string = 'foo'
runner.queries = ['fee', 'fi', 'foe', 'fum']

runner.run()
