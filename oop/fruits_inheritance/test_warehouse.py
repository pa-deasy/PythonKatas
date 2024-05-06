import pytest

from fruits import Apple, Bananna, Kiwi
from warehouse import package_fruit

@pytest.fixture
def sample_kiwi():
    return Kiwi(colour="green")


@pytest.fixture
def sample_apple():
    return Apple(colour="red")


@pytest.fixture
def sample_bananna():
    return Bananna(colour="yellow")


def test_packaging_when_kiwi_then_packaged(sample_kiwi):
    expected = "Picked a green fruitPeeled off a green skinPackaged and ready to go"
    actual = package_fruit(sample_kiwi)
    
    assert actual == expected
    
    
def test_packaging_when_apple_then_packaged(sample_apple):
    expected = "Picked a shiny red applePeeled the shiny red skin off an applePackaged and ready to go"
    actual = package_fruit(sample_apple)
    
    assert actual == expected
    

def test_packaging_when_bananna_then_packaged(sample_bananna):
    expected = "Picked a curvy yellow banannaPeeled the curvy yellow skin off a banannaPackaged and ready to go"
    actual = package_fruit(sample_bananna)
    
    assert actual == expected