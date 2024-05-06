import pytest

from object_oriented_design.hash_table import Hasher


@pytest.fixture
def hasher():
    return Hasher(5)


def test_get_index_for_key_when_calculated_repeatedly_when_index_is_consistent(hasher):
    assert hasher.get_index_for_key('meep') == 4
    assert hasher.get_index_for_key('meep') == 4
    

def test_put_when_put_multiple_times_then_creates_or_updates_key(hasher):
    hasher.put('meep', 11)
    assert hasher.array[4].value == 11
    hasher.put('moop', 12)
    assert hasher.array[4].value == 12
    assert hasher.array[4].next.value == 11
    hasher.put('moop', 13)
    assert hasher.array[4].value == 13
    assert hasher.array[4].next.value == 11
    
    
def test_remove_when_removed_various_keys_then_array_values_as_expected(hasher):
    hasher.put('meep', 11)
    hasher.put('moop', 12)
    hasher.put('maap', 13)
    hasher.put('mup', 1)
    
    assert hasher.array[4].value == 13
    assert hasher.array[4].next.value == 12
    assert hasher.array[4].next.next.value == 11
    hasher.remove('moop')
    assert hasher.array[4].value == 13
    assert hasher.array[4].next.value == 11
    assert hasher.array[4].next.next is None
    
    assert hasher.array[3].value == 1
    hasher.remove('mup')
    assert hasher.array[3] is None
    
    
def test_get_when_retrieved_then_value_as_expected(hasher):
    hasher.put('meep', 11)
    hasher.put('moop', 12)
    hasher.put('mup', 1)
    
    assert hasher.get('meep') == 11
    assert hasher.get('moop') == 12
    assert hasher.get('mup') == 1
    assert hasher.get('maap') is None