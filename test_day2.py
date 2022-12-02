from nose.tools import assert_equal
from day2 import item_score, game_score, part2

#def test_one():
#    assert_equal(item_score("paper"), 2)
#    assert_equal(game_score("rock","paper"), 6)


def test_part2():
    assert_equal(part2('data/day2.example'), 12)
