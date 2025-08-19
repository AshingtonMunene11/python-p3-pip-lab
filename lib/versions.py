import sys
import requests
import pytest
#nothing to add, again nothing else to add today

def python_version():
    return sys.version_info

def requests_version():
    return requests.__version__

def pytest_version():
    return pytest.__version__
