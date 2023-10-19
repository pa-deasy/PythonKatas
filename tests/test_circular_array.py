from object_oriented_design.circular_array import CircularArray


def test_convert_when_converted_then_index_is_correct():
    ca = CircularArray([1, 2, 3, 4, 5])
    
    assert ca.convert(0) == 0
    assert ca.convert(2) == 2
    
    
def test_rotate_when_rotated_then_covert_works_as_expected():
    ca = CircularArray([1, 2, 3, 4, 5])
    
    assert ca.convert(2) == 2
    ca.rotate(2)
    assert ca.convert(2) == 4
    ca.rotate(9)
    assert ca.convert(2) == 3
    
    
def test_get_when_rotated_then_returns_expected_int():
    ca = CircularArray([10, 20, 30, 40, 50])
    
    assert ca.get(2) == 30
    ca.rotate(7)
    assert ca.get(2) == 50
    
    
def test_append_when_appended_then_item_is_inserted_at_the_rotated_end():
    ca = CircularArray([10, 20, 30, 40, 50])
    
    ca.append(60)
    assert ca.get(5) == 60
    ca.rotate(3)
    assert ca.get(2) == 60
    # [10, 20, 30, 40, 50, 60]
    assert ca.get(5) == 30
    ca.append(70)
    assert ca.get(5) == 30
    assert ca.get(6) == 70