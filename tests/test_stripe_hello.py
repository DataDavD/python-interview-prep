from stripe.hello import hello

import logging


def test_hello():
    # create logger
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
    log.info("test logger")
    assert hello() == "Hello, World!"
    assert hello("David") == "Hello, David!"
