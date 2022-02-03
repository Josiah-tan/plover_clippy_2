from .retro import Retro


class FingerSpelling:
    def __init__(self):
        # self._translation_stack = []
        self.was_finger_spelling = False
        self.retro = Retro()

    @staticmethod
    def isFingerSpelling(translation):
        return any(action.glue for action in translation.formatting)

    def filter(self, obj, clippy):
        translation_stack = clippy.engine.translator_state.translations
        if self.isFingerSpelling(translation_stack[-1]):
            # self._translation_stack.append(translation_stack[-1])
            self.was_finger_spelling = True
            return False
        else:
            return True

    def available(self, clippy):
        if self.was_finger_spelling:
            self.was_finger_spelling = False
            # return len(self._translation_stack) > 0
            return len(clippy.engine.translator_state.translations) >= 2
            # return True
        return False

    def getTranslationStack(self, clippy):
        translation_stack = clippy.engine.translator_state.translations
        start = end = len(translation_stack) - 1
        while start >= 1:
            if self.isFingerSpelling(translation_stack[start-1]):
                start -= 1
            else:
                break
        res = []
        for i in range(start, end):
            res.append(translation_stack[i])
        return res

        # translation_stack = self._translation_stack
        # self._translation_stack = []
        # return translation_stack

    def generator(self, obj, clippy):
        if self.available(clippy):
            phrase = self.getTranslationStack(clippy)
            english = self.retro.getEnglish(phrase)
            stroked = self.retro.getStroked(phrase)
            suggestions = self.retro.getSuggestions(clippy, english, stroked)
            if suggestions:
                yield {"english": english,
                       "stroked": stroked,
                       "suggestions": suggestions}
