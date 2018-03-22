#!/usr/bin/env python

import os
import ctypes


########################################
# Tests
########################################

def test_Client_accepts_dict_arg(Client):
    a = {}
    client = Client(a)

def test_Runner_exposes_dylib_location(Runner, ROOT_DIR):
    runner = Runner('', [])
    mtengine_file = os.path.join(ROOT_DIR, 'libmtengine.so')
    assert runner._mtengine_path == mtengine_file

def test_Client_gets_response_from_mtengine(Client, Runner):
    runner = Runner()

    a = {}
    client = Client(a)

    mtengine = runner._mtengine_path
    response = client.get_response(mtengine)
    assert response


def test_Client_decodes_message_to_string(Client, Preprocessor, Runner):
    runner = Runner()
    mtengine = runner._mtengine_path

    a, b = 'conn_str', ['queries']
    preproc = Preprocessor(a, b)
    payload = preproc.get_payload()

    client = Client(payload)
    response = client.get_response(mtengine)
    assert payload == response


# What to test next
# * Sends to Rust
# * Receives from Rust
