import pytest

from boxes import Box, search_for_key


@pytest.fixture
def sample_boxes_with_key():
    green_box = Box(has_key=True, description='green box', contained_boxes=[])
    blue_box = Box(has_key=False, description='blue box', contained_boxes=[])
    red_box = Box(has_key=False, description='red box', contained_boxes=[])
    
    white_box = Box(has_key=False, description='white box', contained_boxes=[green_box, blue_box, red_box])
    black_box = Box(has_key=False, description='black box', contained_boxes=[])
    
    purple_box = Box(has_key=False, description='purple box', contained_boxes=[white_box, black_box])
    gold_box = Box(has_key=False, description='gold box', contained_boxes=[])
    
    brown_box = Box(has_key=False, description='brown box', contained_boxes=[purple_box, gold_box])
    
    return brown_box


@pytest.fixture
def sample_boxes_with_no_key():
    green_box = Box(has_key=False, description='green box', contained_boxes=[])
    blue_box = Box(has_key=False, description='blue box', contained_boxes=[])
    red_box = Box(has_key=False, description='red box', contained_boxes=[])
    
    white_box = Box(has_key=False, description='white box', contained_boxes=[green_box, blue_box, red_box])
    black_box = Box(has_key=False, description='black box', contained_boxes=[white_box])
    
    return black_box


def test_search_for_key_when_key_exists_then_finds_key(sample_boxes_with_key):
    box_with_key = search_for_key(sample_boxes_with_key)
    
    assert box_with_key is not None
    assert box_with_key.description == 'green box'
    

def test_search_for_key_when_no_key_exists_then_returns_none(sample_boxes_with_no_key):
    no_key = search_for_key(sample_boxes_with_no_key)
    
    assert no_key is None
    