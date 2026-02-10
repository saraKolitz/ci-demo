from src.app import print_name
import  pytest
def test_returns_string():
    res = print_name()
    assert isinstance(res, str)
def test_sk():
    assert print_name() == "Sarale Kolitz"
