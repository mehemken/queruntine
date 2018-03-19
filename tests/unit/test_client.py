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
