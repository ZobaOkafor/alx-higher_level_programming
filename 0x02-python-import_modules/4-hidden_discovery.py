#!/usr/bin/python3

"""Prints all the names in hidden_4.pyc"""


if __name__ == "__main__":
    import hidden_4

    hidden_names = hidden_4
    noms = dir(hidden_names)

    for nom in noms:
        if nom[:2] != "__":
            print(nom)
