from lennoxs30api.lennox_home import lennox_home


def test_init():
    lhome = lennox_home(30)
    assert lhome.id == 30
    assert lhome.idx is None
    assert lhome.name is None
    assert lhome.json is None

