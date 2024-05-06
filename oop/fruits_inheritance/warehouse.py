from fruits import Fruit


def package_fruit(fruit: Fruit) -> str:
    packaging = fruit.pick()
    packaging += fruit.peel()
    packaging += "Packaged and ready to go"
    
    return packaging