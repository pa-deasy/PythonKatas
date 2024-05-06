import pytest

from radio_selection import select_stations


@pytest.fixture
def stations():
    stations = {}
    stations['kone'] = set(['id', 'nv', 'ut'])
    stations['ktwo'] = set(['wa', 'id', 'mt'])
    stations['kthree'] = set(['or', 'nv', 'ca'])
    stations['kfour'] = set(['nv', 'ut'])
    stations['kfive'] = set(['ca', 'az'])
    
    return stations


def test_select_stations_when_necessary_stations_exist_then_as_expected(stations):
    states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
    expected = set(['ktwo', 'kthree', 'kone', 'kfive'])
    
    actual = select_stations(stations, states_needed)
    
    assert actual == expected
    