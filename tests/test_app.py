from src.app import print_name
import  pytest
def test_sk():
    assert print_name() == "Sarale Kolitz"
