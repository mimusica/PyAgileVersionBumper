__version__ = "0.0.1"
__author__ = "Christophe@Langenberg.be"


def __contributors__():
    with open("./CONTRIBUTORS.txt") as c:
        contributors = c.readlines()

    return contributors

