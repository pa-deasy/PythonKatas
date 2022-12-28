import pytest

from node_bfs import Person, find_closest_mango_seller

@pytest.fixture
def friends_graph():
    jonny = Person(name='jonny', is_mango_seller=False, friends=[])
    thom = Person(name='thom', is_mango_seller=True, friends=[])
    peggy = Person(name='peggy', is_mango_seller=False, friends=[])
    anuj = Person(name='anuj', is_mango_seller=False, friends=[])
    claire = Person(name='claire', is_mango_seller=False, friends=[thom, jonny])
    alice = Person(name='alice', is_mango_seller=False, friends=[peggy])
    bob = Person(name='bob', is_mango_seller=False, friends=[anuj, peggy])
    me = Person(name='me', is_mango_seller=False, friends=[alice, bob, claire])
    
    return me


@pytest.fixture
def friends_graph_without_seller():
    jonny = Person(name='jonny', is_mango_seller=False, friends=[])
    thom = Person(name='thom', is_mango_seller=False, friends=[])
    peggy = Person(name='peggy', is_mango_seller=False, friends=[])
    anuj = Person(name='anuj', is_mango_seller=False, friends=[])
    claire = Person(name='claire', is_mango_seller=False, friends=[thom, jonny])
    alice = Person(name='alice', is_mango_seller=False, friends=[peggy])
    bob = Person(name='bob', is_mango_seller=False, friends=[anuj, peggy])
    me = Person(name='me', is_mango_seller=False, friends=[alice, bob, claire])
    
    return me


def test_find_closest_mango_seller_when_exists_returns_closest(friends_graph):
    mango_seller = find_closest_mango_seller(friends_graph)
    
    assert mango_seller == 'thom'
    
    
def test_find_closest_mango_seller_when_none_exists_returns_not_found(friends_graph_without_seller):
    no_seller = find_closest_mango_seller(friends_graph_without_seller)
    
    assert no_seller == 'no mango sellers'