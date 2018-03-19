#!/usr/bin/env python

import pytest


########################################
# Fixtures
########################################

@pytest.fixture
def printer():
    from queruntine import Printer
    return Printer


########################################
# Tests
########################################

def test_Printer_takes_one_arg(printer):
    foo = printer('')
