from trees_and_graphs.trees_and_graphs_examples import Node, check_route_exists


def test_check_route_exists_when_route_exists_then_returns_true():
    node_7 = Node(name='node 7', children=[])
    node_6 = Node(name='node 6', children=[])
    node_5 = Node(name='node 5', children=[node_7])
    node_4 = Node(name='node 4', children=[node_5, node_6])
    node_3 = Node(name='node 3', children=[node_4, node_5])
    node_2 = Node(name='node 2', children=[node_3])
    node_1 = Node(name='node 1', children=[node_2, node_3])
    node_5.children.append(node_3)
    node_3.children.append(node_1)
    
    does_exist = check_route_exists(node_2, node_6)
    
    assert does_exist is True
    
    
def test_check_route_exists_when_route_does_not_exist_then_returns_false():
    node_7 = Node(name='node 7', children=[])
    node_6 = Node(name='node 6', children=[])
    node_5 = Node(name='node 5', children=[node_7])
    node_4 = Node(name='node 4', children=[])
    node_3 = Node(name='node 3', children=[node_4])
    node_2 = Node(name='node 2', children=[node_3])
    node_1 = Node(name='node 1', children=[node_2, node_3])
    node_7.children.append(node_6)
    node_5.children.append(node_3)
    node_3.children.append(node_1)
    
    
    does_exist = check_route_exists(node_1, node_7)
    
    assert does_exist is False