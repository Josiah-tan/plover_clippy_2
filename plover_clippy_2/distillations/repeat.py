from ..algos.queue import IterableQueue


class Repeat:
    """
    keeps track of last num suggestions,
    ensures that these suggestions are not repeated
    """

    def __init__(self, num=1):
        self.queue = IterableQueue(num)
        self.num = num

    def distill(self, obj, clippy):
        english = clippy.state.phrase["english"]
        if self.queue.empty():
            self.queue.put(english)
            return True

        if english in self.queue.iterable():
            return False

        if self.queue.full():
            self.queue.remove()

        self.queue.put(english)
        return True
