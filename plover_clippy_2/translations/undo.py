# from .retro import Retro


class Undo:
    """
    basically just hides suggesting things twice due to undos
    """

    def __init__(self):
        # self._translation_stack = []
        self.was_undo = False
        # self.retro = Retro()
        self.cache = None

    @staticmethod
    def isUndoStroke(new, old):
        # pretty hacky method
        # not sure if it accidentally other suggestions
        return len(old) == 1 and len(new) == 0

    @staticmethod
    def equalItems(x, y):
        for i, j in zip(x, y):
            if i.__dict__.items() != j.__dict__.items():
                return False
        return True

    def filter(self, obj, clippy):
        if self.isUndoStroke(obj.new, obj.old):
            self.cache = obj.old
            return False
        elif self.cache and self.equalItems(self.cache, obj.new):
            self.cache = None
            return False
        else:
            return True
