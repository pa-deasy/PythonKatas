import pytest

from dict_bfs import find_closest_mango_seller

@pytest.fixture
def friends_graph():
    friends: dict[str, list[str]] = {}
    friends['me'] = ['alice', 'bob', 'claire']
    friends['bob'] = ['anuj', 'peggy']
    friends['alice'] = ['peggy']
    friends['claire'] = ['thom', 'jonny']
    friends['anuj'] = []
    friends['peggy'] = []
    friends['thom'] = []
    friends['jonny'] = []
    
    return friends


@pytest.fixture
def friends_graph_without_seller():
    friends: dict[str, list[str]] = {}
    friends['me'] = ['alice', 'bob', 'claire']
    friends['bob'] = ['anuj', 'peggy']
    friends['alice'] = ['peggy']
    friends['claire'] = ['tho', 'jonny']
    friends['anuj'] = []
    friends['peggy'] = []
    friends['tho'] = []
    friends['jonny'] = []
    
    return friends


def test_find_closest_mango_seller_when_exists_returns_closest(friends_graph):
    mango_seller = find_closest_mango_seller(friends_graph)
    
    assert mango_seller == 'thom'
    
    
def test_find_closest_mango_seller_when_none_exists_returns_not_found(friends_graph_without_seller):
    no_seller = find_closest_mango_seller(friends_graph_without_seller)
    
    assert no_seller == 'no mango sellers'