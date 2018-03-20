#!/usr/bin/env python

import pytest
import random
import json


########################################
# Preprocessor
########################################

def test_Preprocessor_takes_two_args(Preprocessor):
    a, b = '', []
    foo = Preprocessor(a, b)

def test_get_payload_returns_bytes(Preprocessor):
    preproc = Preprocessor('', [])
    payload = preproc.get_payload()
    assert type(payload) == bytes

def test_jsonify_returns_str(Preprocessor):
    preproc = Preprocessor('', [])
    foo = preproc._jsonify()
    assert type(foo) == str

def test_to_bytes_returns_bytes(Preprocessor):
    preproc = Preprocessor('', [])
    foo = preproc._to_bytes()
    assert type(foo) == bytes

def test_conn_str_in_jsonify_payload(Preprocessor):
    conn_str, b = 'foo', []
    preproc = Preprocessor(conn_str, b)
    payload = preproc._jsonify()
    assert conn_str in payload

def test_random_conn_str_in_jsonify_payload(Preprocessor):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    rand_letters = [random.choice(letters) for _ in range(15)]
    conn_str = ''.join(rand_letters)
    preproc = Preprocessor(conn_str, [])
    payload = preproc._jsonify()
    assert conn_str in payload

def test_jsonify_returns_valid_json(Preprocessor):
    a, b = 'a', []
    preproc = Preprocessor(a, b)
    payload = preproc._jsonify()
    loaded = json.loads(payload)
    assert type(loaded) == dict

def test_single_query_input_in_jsonify_output(Preprocessor):
    query = ['db.foo.find({})']
    preproc = Preprocessor('a', query)
    payload = preproc._jsonify()
    assert query[0] in payload

def test_to_bytes_is_same_as_jsoinfy_output(Preprocessor):
    a, b = 'feefifoefum', ['foo', 'bar', 'baz']
    preproc = Preprocessor(a, b)
    payload_str = preproc._jsonify()
    payload_bytes = preproc._to_bytes()
    assert json.loads(payload_str) == json.loads(payload_bytes)

def test_get_payload_equals_output_of_to_bytes(Preprocessor):
    a, b = 'feefifoefum', ['foo', 'bar', 'baz']
    preproc = Preprocessor(a, b)
    payload = preproc.get_payload()
    p_bytes = preproc._to_bytes()
    assert payload == p_bytes
