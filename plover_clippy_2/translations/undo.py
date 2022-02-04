# from .retro import Retro


class Undo:
    """
    basically just hides suggesting things twice due to undos
    """

    def __init__(self):
        # self._translation_stack = []
        # self.was_undo = False
        # self.retro = Retro()
        # self.cache = None
        self.cache_new = None
        self.cache_old = None
        self.blocking = True

    @staticmethod
    def isUndoStroke(new, old):
        # pretty hacky method
        # not sure if it accidentally hides other suggestions
        # update, this does not work for "TAOEU/WREUR/*/WREUR"
        return len(old) == 1 and len(new) == 0

    @staticmethod
    def equalItems(x, y):
        # equal items between two list of actions
        for i, j in zip(x, y):
            if i.__dict__.items() != j.__dict__.items():
                return False
        return True

    def filter(self, obj, clippy):
        # if self.isUndoStroke(obj.new, obj.old):
        #     self.cache = obj.old
        #     return False
        # elif self.cache and self.equalItems(self.cache, obj.new):
        #     self.cache = None
        #     return False
        # else:
        #     return True

        # limitation: only suppresses strokes for a single undo:
        # handling multiple undos would likely require more memory,
        # (maybe a tree structure of some sort?)
        # print(f"clippy.state.prev_stroke.is_correction = {clippy.state.prev_stroke.is_correction}")
        if (
                self.cache_old and
                clippy.state.prev_stroke.is_correction and
                not self.multiple_undo):
            self.multiple_undo = True
            # print(f"self.equalItems(obj.new, self.cache_old) = {self.equalItems(obj.new, self.cache_old)}")
            # print(f"self.equalItems(obj.old, self.cache_new) = {self.equalItems(obj.old, self.cache_new)}")
            return not (
                    self.equalItems(obj.new, self.cache_old)
                    and self.equalItems(obj.old, self.cache_new))
        else:
            self.multiple_undo = False
            # cache in case current stroke is an undo
            self.cache_old = obj.old
            self.cache_new = obj.new
            return True
