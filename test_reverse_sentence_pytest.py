import reverse_sentence


# Just make test functions directly with simple assert statements
def test1():
    assert reverse_sentence.rev_sen("Testing in pytest") == "pytest in Testing"
    assert reverse_sentence.rev_sen("This is for extra credit") == "credit extra for is This"


# Invalid input tests (results in failure)
def test2():
    assert reverse_sentence.rev_sen(123) != "321"
    assert reverse_sentence.rev_sen(123.456) != "456.123"
