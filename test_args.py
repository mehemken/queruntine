import random

import pytest

from queruntine import Client
from queruntine import Postprocessor
from queruntine import Printer

@pytest.fixture
def preproc():
    from queruntine import Preprocessor
    return Preprocessor

########################################
# Args
########################################

def test_Preprocessor_takes_two_args(preproc):
    a, b = '', []
    foo = preproc(a, b)

def test_Client_accepts_dict_arg():
    a = {}
    foo = Client(a)

def test_Postprocessor_takes_one_arg():
    foo = Postprocessor('')

def test_Printer_takes_one_arg():
    foo = Printer('')

########################################
# Preprocessor
########################################

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

########################################
# Next, test that
# * The output of _jsonify is valid json
# * conn_str as bytes is in the output
#   of _to_bytes
# * the queries are in payload of jsonify
# * the queries as bytes are in the
#   output of _to_bytes
