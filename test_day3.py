from day3 import part1, value, score, linescore
from nose.tools import assert_equal

def test_sample():
    assert_equal(part1('data/day3.sample'), 157)
#
#
#def test_score():
#    assert_equal(score('a','a'), 1)
#
#def test_value():
#    assert_equal(value('a'), 1)
#    assert_equal(value('A'), 27)

def test_linescore():
    assert_equal(linescore('vJrwpWtwJgWrhcsFMMfFFhFp'), 16)
