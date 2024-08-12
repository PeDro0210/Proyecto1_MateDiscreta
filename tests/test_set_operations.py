import setOperation as op

def test_union():
    print(op.union({"z":"_", "e":"_"}, {"a":"_", "b":"_", "e":"_"}).keys())
    assert op.union({"z":"_", "e":"_"}, {"a":"_", "b":"_", "e":"_"}).keys() == {"a", "b", "e", "z"}

def test_complement():
    assert op.complement({"z":"_","e":"_"}).keys() ==  set(list("abcdfghijklmnopqrstvwxy0123456789"))

def test_intersection():
    assert op.intersection({"z":"_", "e":"_"}, {"a":"_", "b":"_", "e":"_"}).keys() == {"e"}

def test_difference():
    assert op.difference({"z":"_", "e":"_"}, {"a":"_", "b":"_", "e":"_"}).keys() == {"z"}


def test_difference():
    assert op.simetricDifference({"z":"_", "e":"_"}, {"a":"_", "b":"_", "e":"_"}).keys() == {"z", "a", "b"}


