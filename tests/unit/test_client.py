#!/usr/bin/env python

import os
import ctypes
import pytest


########################################
# Tests
########################################


def test_client_knows_dylib_location(Client, ROOT_DIR):
    client = Client()
    mtengine_file = os.path.join(ROOT_DIR, 'libmtengine.so')
    assert client._mtengine_path == mtengine_file


@pytest.mark.ffi
def test_Client_gets_response_from_mtengine(Client):
    client = Client()
    payload = b"{'foo':'bar'}"

    response = client.get_response(payload)
    assert response


@pytest.mark.ffi
def test_client_decodes_message_to_string(Client, Preprocessor):
    client = Client()
    payload = b"{'foo':'bar'}"

    response = client.get_response(payload)
    assert response


# What to test next
# * Sends to Rust
# * Receives from Rust
