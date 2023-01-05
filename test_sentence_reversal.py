import pytest

from sentence_reversal import reverse_sentence


def test_reverse_sentence_when_reversed_then_as_expected():
    sentence = 'My name is Khan'
    expected = 'Khan is name My'
    
    actual = reverse_sentence(sentence)
    
    assert actual == expected
