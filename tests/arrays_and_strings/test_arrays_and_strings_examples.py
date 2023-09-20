from arrays_and_strings.arrays_and_strings_examples import urlify


def test_urlify_when_converted_then_matches_expected():
    input = ['M', 'r', ' ', 'J', 'o', 'h', 'n', ' ',  'S', 'm', 'i', 't', 'h', ' ', ' ', ' ']
    true_length = 13
    expected = ['M', 'r', '%', '2', '0', 'J', 'o', 'h', 'n', '%', '2', '0', 'S', 'm', 'i', 't', 'h']
    
    actual = urlify(input, true_length)
    
    assert actual == expected