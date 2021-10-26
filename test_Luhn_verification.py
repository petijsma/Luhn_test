import pytest
from Luhn_verification import luhn

def test_luhn():
    assert luhn(49927398716)
    assert luhn(49927398717)


