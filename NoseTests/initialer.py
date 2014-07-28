def initials(name):
    name = str(name)
    if len(name) < 1:
        raise(IndexError, "Length must be over one")