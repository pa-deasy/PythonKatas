from trees_and_graphs.trees_and_graphs_examples import Node, TreeNode, check_route_exists, create_bst_from_sorted_list, create_linked_lists_from_tree


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
    
    
def test_create_bst_from_sorted_list_when_created_then_bst_ordered_as_expected():
    sorted_numbers = [1, 3, 7, 8, 12, 18, 55, 70, 80]
    
    bst = create_bst_from_sorted_list(sorted_numbers)
    
    assert bst.value == 12
    assert bst.left.value == 7
    assert bst.left.left.value == 3
    assert bst.left.left.left.value == 1
    assert bst.left.right.value == 8
    assert bst.right.value == 70
    assert bst.right.left.value == 55
    assert bst.right.left.left.value == 18
    assert bst.right.right.value == 80
         
#                       12
#               7                   70       
#           3       8           55      80
#       1                   18

def test_create_linked_lists_from_tree_when_created_then_lists_as_expected():
    root_12 = TreeNode(value=12, left=None, right=None)
    node_7 = TreeNode(value=7, left=None, right=None)
    node_3 = TreeNode(value=3, left=None, right=None)
    node_1 = TreeNode(value=1, left=None, right=None)
    node_8 = TreeNode(value=8, left=None, right=None)
    node_70 = TreeNode(value=70, left=None, right=None)
    node_55 = TreeNode(value=55, left=None, right=None)
    node_18 = TreeNode(value=18, left=None, right=None)
    node_80 = TreeNode(value=80, left=None, right=None)
    
    root_12.left = node_7
    root_12.left.left = node_3
    root_12.left.left.left = node_1
    root_12.left.right = node_8
    root_12.right = node_70
    root_12.right.left = node_55
    root_12.right.left.left = node_18
    root_12.right.right = node_80
    
    linked_lists = create_linked_lists_from_tree(root_12)
    
    assert len(linked_lists) == 4
    assert linked_lists[0].head.value == 12
    assert linked_lists[0].head.next is None
    assert linked_lists[1].head.value == 70
    assert linked_lists[1].head.next.value == 7
    assert linked_lists[1].head.next.next is None
    assert linked_lists[2].head.value == 80
    assert linked_lists[2].head.next.value == 55
    assert linked_lists[2].head.next.next.value == 8
    assert linked_lists[2].head.next.next.next.value == 3
    assert linked_lists[2].head.next.next.next.next is None
    assert linked_lists[3].head.value == 18
    assert linked_lists[3].head.next.value == 1
    assert linked_lists[3].head.next.next is None
