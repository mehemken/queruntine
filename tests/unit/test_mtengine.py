import pytest


########################################
# Tests for the Multi Thread Engine
########################################


@pytest.mark.skip(reason='Triggers a coredump')
def test_mtengine_returns(MTEngine):
    response = MTEngine.exec_queries()
    assert response


def test_mtengine_accepts_values(MTEngine):
    dummy_bytes = b'foobarbaz'
    response = MTEngine.exec_queries(dummy_bytes)
    assert response
