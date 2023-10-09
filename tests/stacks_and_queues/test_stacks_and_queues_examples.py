from stacks_and_queues.stacks_and_queues_examples import MultiStack


def test_multistack_when_operated_on_then_behaves_as_expected():
    stack = MultiStack(stack_count=3, total_size=10)
    
    assert stack.is_empty(1) is True
    assert stack.is_empty(2) is True
    assert stack.is_empty(3) is True
    stack.pop(1)
    stack.pop(2)
    stack.pop(3)
    
    stack.push(stack_number=1, value=10)
    assert stack.peek(stack_number=1) == 10
    stack.push(stack_number=2, value=20)
    assert stack.peek(stack_number=2) == 20
    stack.push(stack_number=3, value=30)
    assert stack.peek(stack_number=3) == 30
    
    assert stack.is_full(1) is False
    assert stack.is_full(2) is False
    assert stack.is_full(3) is False
    
    stack.push(stack_number=2, value=21)
    stack.push(stack_number=2, value=22)
    stack.push(stack_number=2, value=23)
    assert stack.peek(stack_number=2) == 22
    
    assert stack.is_full(2) is True
    assert stack.pop(2) is 22
    assert stack.peek(2) == 21
    stack.push(stack_number=2, value=23)
    assert stack.peek(2) == 23
    