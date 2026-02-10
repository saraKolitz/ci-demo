from src.app import print_name
import  pytest
def test_returns_string():
    result = print_name()
    assert isinstance(result, str)
def test_sk():
    assert print_name() == "Sarale Kolitz"
