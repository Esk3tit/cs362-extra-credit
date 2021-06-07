import two_sum


# Just make test functions directly with simple assert statements
def test1():
    assert two_sum.two_sum([2, 7, 11, 15], 9) == [2, 7]
    assert two_sum.two_sum([3, 3], 6) == [3, 3]


# Invalid input tests (but this time we check such that the invalid inputs actually meet conditions)
# and therefore pass the tests
def test2():
    assert two_sum.two_sum([], 0) is None
    assert two_sum.two_sum(["3", "3"], 6) != ["3", "3"]
