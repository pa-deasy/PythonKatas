from pokemon import PokemonFactory, Type


def test_choose_when_water_chosen_then_selected_outputs_the_expected_message():
     pokemon = PokemonFactory.choose(Type.WATER)
     
     assert pokemon.selected() == 'Select Squirtle a water type Pokemon that is sure to make a splash'
     
    
def test_choose_when_fire_chosen_then_selected_outputs_the_expected_message():
     pokemon = PokemonFactory.choose(Type.FIRE)
     
     assert pokemon.selected() == 'Selected Charmander a fire type Pokemon with a sparky personality'
     

def test_choose_when_grass_chosen_then_selected_outputs_the_expected_message():
     pokemon = PokemonFactory.choose(Type.GRASS)
     
     assert pokemon.selected() == 'Selected Bulbasaur a grass type Pokemeon that is cool as a breeze'
