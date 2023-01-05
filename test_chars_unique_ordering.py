import pytest

from chars_unique_ordering import remove_duplicate_chars_and_order


def test_remove_duplicate_chars_and_order_when_calculated_then_as_expected():
    input = 'abuukscpccf'
    expected = 'abcfkpsu'
    
    actual = remove_duplicate_chars_and_order(input)
    
    assert actual == expected
