#!/usr/bin/env python

import pytest
import random
import json


########################################
# Fixtures
########################################

@pytest.fixture
def preproc():
    from queruntine import Preprocessor
    return Preprocessor

########################################
# Tests
########################################

def test_Preprocessor_takes_two_args(preproc):
    a, b = '', []
    foo = preproc(a, b)

def test_get_payload_returns_bytes(preproc):
    preproc = preproc('', [])
    payload = preproc.get_payload()
    assert type(payload) == bytes

def test_jsonify_returns_str(preproc):
    preproc = preproc('', [])
    foo = preproc._jsonify()
    assert type(foo) == str

def test_to_bytes_returns_bytes(preproc):
    preproc = preproc('', [])
    foo = preproc._to_bytes()
    assert type(foo) == bytes

def test_conn_str_in_jsonify_payload(preproc):
    conn_str, b = 'foo', []
    preproc = preproc(conn_str, b)
    payload = preproc._jsonify()
    assert conn_str in payload

def test_random_conn_str_in_jsonify_payload(preproc):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    rand_letters = [random.choice(letters) for _ in range(15)]
    conn_str = ''.join(rand_letters)
    preproc = preproc(conn_str, [])
    payload = preproc._jsonify()
    assert conn_str in payload

def test_jsonify_returns_valid_json(preproc):
    a, b = 'a', []
    preproc = preproc(a, b)
    payload = preproc._jsonify()
    loaded = json.loads(payload)
    assert type(loaded) == dict

def test_single_query_input_in_jsonify_output(preproc):
    query = ['db.foo.find({})']
    preproc = preproc('a', query)
    payload = preproc._jsonify()
    assert query[0] in payload

def test_to_bytes_is_same_as_jsoinfy_output(preproc):
    a, b = 'feefifoefum', ['foo', 'bar', 'baz']
    preproc = preproc(a, b)
    payload_str = preproc._jsonify()
    payload_bytes = preproc._to_bytes()
    assert json.loads(payload_str) == json.loads(payload_bytes)

def test_get_payload_equals_output_of_to_bytes(preproc):
    a, b = 'feefifoefum', ['foo', 'bar', 'baz']
    preproc = preproc(a, b)
    payload = preproc.get_payload()
    p_bytes = preproc._to_bytes()
    assert payload == p_bytes
