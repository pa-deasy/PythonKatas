import pytest

from flight_path_generator import flight_path_from


def test_flight_path_from_when_path_exists_then_is_returned():
    flights = {'YYZ':'DCA', 'YVR':'YYZ', 'DCA':'JFK'}
    expected = 'YVR -> YYZ -> DCA -> JFK'
    
    actual = flight_path_from(flights)
    
    assert actual == expected
    
    
def test_flight_path_from_when_no_clear_path_exists_then_error_returned():
    flights = {'YYZ':'DCA', 'YVR':'YYZ', 'DCA':'JFK', 'DUB':'LND'}
    
    with pytest.raises(Exception):
        flight_path_from(flights)
