import pytest

from pythonic_list import HikeTrailCollection

def test_for_in():

    trail = HikeTrailCollection(("Rattlesnake","Koko Head","Enchantment"))

    trails_list = []

    for trail in trail:
        trails_list.append(trail)

    assert trails_list == ["Rattlesnake","Koko Head","Enchantment"]


# @pytest.mark.skip("pending")
def test_list_comprehension():

    trails = HikeTrailCollection(("Rattlesnake","Koko Head","Enchantment"))

    cap_trails = [trail.upper() for trail in trails]

    assert cap_trails == ["RATTLESNAKE", "KOKO HEAD", "ENCHANTMENT"]

# @pytest.mark.skip("pending")
def test_list_cast():

    trail_list = ["Rattlesnake","Koko Head","Enchantment"]

    trails = HikeTrailCollection(trail_list)

    assert list(trails) == trail_list


# @pytest.mark.skip("pending")
def test_range():

    num_range = range(1,20+1)

    nums = HikeTrailCollection(num_range)

    assert len(nums) == 20



# @pytest.mark.skip("pending")
def test_filter():

    nums = HikeTrailCollection(range(1,21))

    odds = [num for num in nums if num % 2]

    assert odds == [1,3,5,7,9,11,13,15,17,19]


# @pytest.mark.skip("pending")
def test_next():

    trails = HikeTrailCollection(["Rattlesnake","Koko Head","Enchantment"])

    iterator = iter(trails)

    assert next(iterator) == "Rattlesnake"
    assert next(iterator) == "Koko Head"
    assert next(iterator) == "Enchantment"


# @pytest.mark.skip("pending")
def test_stop_iteration():

    trails = HikeTrailCollection(["Rattlesnake","Koko Head","Enchantment"])

    iterator = iter(trails)

    with pytest.raises(StopIteration):
        while True:
            trail = next(iterator)

# @pytest.mark.skip("pending")
def test_str():
    trails = HikeTrailCollection(["Rattlesnake","Koko Head","Enchantment"])
    assert str(trails) == "[ Rattlesnake ] -> [ Koko Head ] -> [ Enchantment ] -> None"

# dunder method tests

# @pytest.mark.skip("pending")
def test_equals():

    lla = HikeTrailCollection(["Rattlesnake","Koko Head","Enchantment"])
    llb = HikeTrailCollection(["Rattlesnake","Koko Head","Enchantment"])

    assert lla == llb

# @pytest.mark.skip("pending")
def test_get_item():

    trails = HikeTrailCollection(["apple","banana","cucumber"])

    assert trails[0] == "apple"

# @pytest.mark.skip("pending")
def test_get_item_out_of_range():

    trails = HikeTrailCollection(["apple","banana","cucumber"])

    with pytest.raises(IndexError):
        trails[100]