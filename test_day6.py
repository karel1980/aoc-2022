from day6 import findMarkerPosition, findMarkerPosition2
from nose.tools import assert_equal


def test_examples():
    assert_equal(findMarkerPosition('bvwbjplbgvbhsrlpgdmjqwftvncz'), 5)
    assert_equal(findMarkerPosition('nppdvjthqldpwncqszvftbrmjlhg'), 6)
    assert_equal(findMarkerPosition('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'), 10)
    assert_equal(findMarkerPosition('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'), 11)


def test_examples():
    assert_equal(findMarkerPosition2('mjqjpqmgbljsphdztnvjfqwrcgsmlb'), 19)
    assert_equal(findMarkerPosition2('bvwbjplbgvbhsrlpgdmjqwftvncz'), 23)
    assert_equal(findMarkerPosition2('nppdvjthqldpwncqszvftbrmjlhg'), 23)
    assert_equal(findMarkerPosition2('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'), 29)
    assert_equal(findMarkerPosition2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'), 26)
