#!/usr/bin/env python

import pytest


########################################
# Fixtures
########################################

@pytest.fixture
def runner():
    from queruntine import Runner
    return Runner

@pytest.fixture
def client():
    from queruntine import Client
    return Client

@pytest.fixture
def preproc():
    from queruntine import Preprocessor
    return Preprocessor


########################################
# Tests
########################################

def test_runner_passes_payload_from_preproc_to_client(runner, client, preproc):
    a, b = 'connection_string', ['query1', 'query2']
    runner = runner(a, b)
    payload_r = runner._payload

    pre = preproc(a, b)
    pre = pre.get_payload()
    client = client(pre)
    payload_c = client._payload

    assert payload_r == payload_c

def test_runner_payload_is_output_of_preproc(runner, preproc):
    a, b = 'connection_string', ['query1', 'query2']

    runner = runner(a, b)
    preproc = preproc(a, b)

    payload_r = runner._payload
    payload_p = preproc.get_payload()

    assert payload_r == payload_p
