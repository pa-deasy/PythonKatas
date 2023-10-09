from stacks_and_queues.stacks_and_queues_examples import MinStack, MultiStack, MyQueue, SetOfStacks, Stack, sort_stack


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
    
    
def test_minstack_when_operated_on_then_behaves_as_expected():
    stack = MinStack()
    
    stack.push(5)
    assert stack.min() == 5
    stack.push(6)
    assert stack.min() == 5
    stack.push(3)
    assert stack.min() == 3
    stack.push(7)
    assert stack.min() == 3
    assert stack.pop() == 7
    assert stack.pop() == 3
    assert stack.min() == 5


def test_setofstacks_when_operated_on_then_behaves_as_expected():
    stack = SetOfStacks(2)
    
    assert stack.is_full(0) is False
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    assert stack.peek() == 3
    assert stack.pop() == 3
    assert stack.peek() == 2
    
    stack.push(4)
    stack.push(5)
    assert stack.pop_at(0) == 2
    stack.push(6)
    stack.push(7)
    
    assert stack.peek() == 7
    
    
def test_myqueue_when_operated_on_then_behaves_as_expected():
    queue = MyQueue()
    
    queue.enqueue(1)
    assert queue.peek() == 1
    queue.enqueue(2)
    assert queue.peek() == 1
    queue.enqueue(3)
    assert queue.peek() == 1
    queue.enqueue(4)
    assert queue.peek() == 1
    
    assert queue.dequeue() == 1
    assert queue.peek() == 2
    
    
def test_sort_stack_when_operated_on_then_behaves_as_expected():
    stack = Stack()
    stack.push(3)
    stack.push(5)
    stack.push(2)
    stack.push(4)
    stack.push(1)
    
    sorted_stack = sort_stack(stack)
    
    assert sorted_stack.pop() == 1
    assert sorted_stack.pop() == 2
    assert sorted_stack.pop() == 3
    assert sorted_stack.pop() == 4
    assert sorted_stack.pop() == 5
    assert sorted_stack.is_empty() is True