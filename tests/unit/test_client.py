#!/usr/bin/env python

import pytest
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
    assert type(response) == bytes


# What to test next
# * Does not accept empty dict
# * Does not return empty dict
# * Sends to Rust
# * Receives from Rust
