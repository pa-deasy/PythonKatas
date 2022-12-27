from voting import VotingStation
import pytest


@pytest.fixture
def sample_voting_station():
    return VotingStation(voters={})

def test_cast_vote_when_has_not_voted_then_votes(sample_voting_station):
    assert sample_voting_station.cast_vote('Patrick') == 'Patrick just voted'
    assert sample_voting_station.cast_vote('Nicole') == 'Nicole just voted'
    

def test_cast_vote_when_has_voted_then_does_not_vote(sample_voting_station):
    assert sample_voting_station.cast_vote('Patrick') == 'Patrick just voted'
    assert sample_voting_station.cast_vote('Patrick') == 'Patrick already voted'