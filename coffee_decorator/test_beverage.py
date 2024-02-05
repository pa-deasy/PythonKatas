from beverage import DarkRoast, HomeBlend, Milk, Mocha, Size


def test_beverage_when_small_home_blend_with_two_milk_then_correct_cost_and_description():
    beverage = Milk(Milk(HomeBlend(Size.SMALL)))
    
    assert beverage.cost() == 2.7
    assert beverage.get_description() == 'Home Blend, Milk, Milk'
    
    
def test_beverage_when_large_dark_roast_mocha_then_correct_cost_and_description():
    beverage = Mocha(DarkRoast(Size.LARGE))
    
    assert beverage.cost() == 5.4
    assert beverage.get_description() == 'Dark Roast, Mocha'