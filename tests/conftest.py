import pytest
from pathlib import Path
import os

########################################
# Fixtures
########################################

@pytest.fixture
def Runner():
    from queruntine import Runner
    return Runner

@pytest.fixture
def Preprocessor():
    from queruntine import Preprocessor
    return Preprocessor

@pytest.fixture
def Client():
    from queruntine import Client
    return Client

@pytest.fixture
def ROOT_DIR():
    """
    Returns the root directory of the queruntine project
    relative to this file for use in tests. This is not available
    to the application code.

    But this smells a little funny. Maybe there is a better
    way to do this?
    """
    queruntine_root = Path(__file__).parent.parent
    return os.path.abspath(queruntine_root)

@pytest.fixture
def MTEngine(ROOT_DIR):
    import ctypes
    mtengine = os.path.join(ROOT_DIR, 'libmtengine.so')
    return ctypes.cdll.LoadLibrary(mtengine)
