from nose.tools import assert_equal
from day2 import item_score, game_score

def test_one():
    assert_equal(item_score("paper"), 2)
    assert_equal(game_score("rock","paper"), 6)


