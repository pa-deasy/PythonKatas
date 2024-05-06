import pytest


from weighted_graph import quickest_path


@pytest.fixture
def travel_graph():
    graph = {}
    
    graph['start'] = {}
    graph['start']['a'] = 6
    graph['start']['b'] = 2
    
    graph['a'] = {}
    graph['a']['fin'] = 1

    graph['b'] = {}
    graph['b']['a'] = 3
    graph['b']['fin'] = 5
    
    graph['fin'] = {}
    
    return graph


def test_quickest_path_when_travel_path_exists_then_gets_quickest(travel_graph):
    quickest = quickest_path(travel_graph)
    
    assert quickest == 'start -> b -> a -> fin'
    
    
@pytest.fixture
def trading_graph():
    graph = {}
    
    graph['start'] = {}
    graph['start']['lp'] = 5
    graph['start']['poster'] = 0
    
    graph['lp'] = {}
    graph['lp']['guitar'] = 15
    graph['lp']['drum'] = 20
    
    graph['poster'] = {}
    graph['poster']['guitar'] = 30
    graph['poster']['drum'] = 35
    
    graph['guitar'] = {}
    graph['guitar']['fin'] = 20
    
    graph['drum'] = {}
    graph['drum']['fin'] = 10
    
    graph['fin'] = {}
    
    return graph


def test_quickest_path_when_trading_path_exists_then_gets_quickest(trading_graph):
    quickest = quickest_path(trading_graph)
    
    assert quickest == 'start -> lp -> drum -> fin'
