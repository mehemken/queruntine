#!/usr/bin/env python

import pytest


########################################
# Fixtures
########################################

@pytest.fixture
def postproc():
    from queruntine import Postprocessor
    return Postprocessor


########################################
# Tests
########################################

def test_Postprocessor_takes_one_arg(postproc):
    foo = postproc('')
