from setOperation import union

def test_union():
    assert union({"z":"_", "e":"_"}, {"a":"_", "b":"_", "e":"_"}) == {"a", "b", "e", "z"}
