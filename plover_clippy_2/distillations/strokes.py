class Strokes:
    """
    stroke suggestion filter
    max: the maximum number of suggestions allowed
    multi_max: the maximum number of suggestions allowed for each multistroke
    """

    def __init__(self, max=3, multi_max=3):
        assert max >= 1
        self.max = max
        assert multi_max >= 1
        self.multi_max = multi_max

    def distill_multi_max(self, obj, clippy):
        suggestions = clippy.state.phrase["suggestions"]
        _suggestions = []
        count = 0
        number_strokes = 0
        for suggestion in suggestions:
            len_suggestion = len(suggestion)
            if len_suggestion > number_strokes:
                _suggestions.append(suggestion)
                number_strokes = len_suggestion
                count = 1
            elif len_suggestion == number_strokes and count < self.multi_max:
                _suggestions.append(suggestion)
                count += 1
        clippy.state.phrase["suggestions"] = _suggestions
        return True

    def distill_max(self, obj, clippy):
        suggestions = clippy.state.phrase["suggestions"]
        _suggestions = suggestions[:min(self.max, len(suggestions))]
        clippy.state.phrase["suggestions"] = _suggestions
        return True

    def distill(self, obj, clippy):
        if not self.distill_multi_max(obj, clippy):
            return False
        if not self.distill_max(obj, clippy):
            return False
        return True
