#!/usr/bin/env python

import pytest


########################################
# Fixtures
########################################

@pytest.fixture
def client():
    from queruntine import Client
    return Client


########################################
# Tests
########################################

def test_Client_accepts_dict_arg(client):
    a = {}
    foo = client(a)


# What to test next
# * Does not accept empty dict
# * Does not return empty dict
# * Sends to Rust
# * Receives from Rust
