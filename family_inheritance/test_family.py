from family import Child, Parent


def test_parent_when_born_then_has_expected_hair_colour_and_language():
    dad = Parent()
    
    assert dad.hair == 'brown'
    assert dad.languages == ['english']
    
    
def test_child_when_born_then_has_expected_hair_colour_and_languages():
    son = Child()
    
    assert son.hair == 'brown'
    assert son.languages == ['english', 'cantonese']
    
