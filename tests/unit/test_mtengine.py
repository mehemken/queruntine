########################################
# Tests for the Multi Thread Engine
########################################


def test_mtengine_returns(MTEngine):
    response = MTEngine.exec_queries()
    assert response


def test_mtengine_accepts_values(MTEngine):
    dummy_bytes = b'foobarbaz'
    response = MTEngine.exec_queries(dummy_bytes)
    assert response
