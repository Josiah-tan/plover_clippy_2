def tails(ls):
    for i in reversed(range(len(ls))):
        yield ls[i:]
