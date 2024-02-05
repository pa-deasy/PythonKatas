import pytest

from fruits import Apple, Bananna, Kiwi


@pytest.fixture
def sample_kiwi():
    return Kiwi("green")


@pytest.fixture
def sample_apple():
    return Apple("red")


@pytest.fixture
def sample_bananna():
    return Bananna("yellow")


def test_kiwi_when_created_then_expected(sample_kiwi):
    assert sample_kiwi.pick() == "Picked a green fruit"
    assert sample_kiwi.peel() == "Peeled off a green skin"
    
    
def test_apple_when_created_then_expected(sample_apple):
    assert sample_apple.pick() =="Picked a shiny red apple"
    assert sample_apple.peel() == "Peeled the shiny red skin off an apple"
    

def test_bananna_when_created_then_expected(sample_bananna):
    assert sample_bananna.pick() =="Picked a curvy yellow bananna"
    assert sample_bananna.peel() == "Peeled the curvy yellow skin off a bananna"