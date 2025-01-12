from stripe.hello import hello


def test_hello():
    assert hello() == "Hello, World!"
    assert hello("David") == "Hello, David!"
