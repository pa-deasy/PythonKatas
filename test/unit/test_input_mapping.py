from input_mapping import DEFAULT_DELIMITER, DEFAULT_HEADER_INCLUDED, file_location_is_valid, header_included_is_valid, map_delimiter, map_header_included


def test_file_location_is_valid_when_valid_then_returns_true():
    file_location = 'test/unit/test_file.csv'
    is_valid = file_location_is_valid(file_location)
    assert is_valid is True
    
    
def test_file_location_is_valid_when_invalid_then_returns_false():
    file_location = 'test/unit/not_a_thing.csv'
    is_valid = file_location_is_valid(file_location)
    assert is_valid is False


def test_map_delimiter_when_valid_then_returned():
    delimiter = '|'
    mapped_delimiter = map_delimiter(delimiter)
    assert mapped_delimiter == delimiter


def test_map_delimiter_when_empty_then_default_returned():
    mapped_delimiter = map_delimiter('')
    assert mapped_delimiter == DEFAULT_DELIMITER


def test_header_included_is_valid_when_valid_then_returns_true():
    is_valid = header_included_is_valid('True')
    assert is_valid is True
    

def test_header_included_is_valid_when_empty_then_returns_true():
    is_valid = header_included_is_valid('')
    assert is_valid is True


def test_header_included_is_valid_when_invalid_then_returns_false():
    is_valid = header_included_is_valid('bleh')
    assert is_valid is False


def test_map_header_included_when_true_then_returns_true():
    header_included = map_header_included('True')
    assert header_included is True
    

def test_map_header_included_when_empty_then_returns_default():
    header_included = map_header_included('')
    assert header_included is DEFAULT_HEADER_INCLUDED


def test_map_header_included_when_false_then_returns_false():
    header_included = map_header_included('False')
    assert header_included is False
