class Defaults:
    @staticmethod
    def initPre(obj, clippy):
        return obj.org.defaultPre(clippy)

    @staticmethod
    def init(clippy):
        clippy.state.output_file_name = "clippy_2.org"
        clippy.state.efficiency_symbol = "*"
        clippy.state.max_pad_efficiency = 5
        clippy.state.max_pad_english = 15
        clippy.state.justify = "left"
        clippy.state.last_num_translations = 10

        clippy.state.colors = {
                # for formatting
                "suggestions": "neutral_aqua",
                "stroked": "neutral_purple",
                "english": "neutral_orange",
                "efficiency_symbol": lambda efficiency_symbol: [
                    "bright_green", "bright_purple", "bright_blue",
                    "bright_orange", "bright_red"
                    ][min(len(efficiency_symbol.strip())-1, 4)],
                "source": "gray",
                # "*": "gray", # not implemented
                # ">": "gray",
                # for extremities
                "START": "bright_green",
                "STOP": "bright_red",
                "date": "neutral_aqua",
                # "-": "bright_blue",
                }

        clippy.extremity.start_pre_sources.set(
                ["Start", {
                    "colorscheme": "gruvbox",
                    "mode": "defaultPre"}])

        clippy.extremity.stop_pre_sources.set(
                ["Stop", {
                    "colorscheme": "gruvbox",
                    "mode": "defaultPre"}])

    @staticmethod
    def initPost(obj, clippy):
        pass
        # return obj.org.defaultPost(clippy)

    @staticmethod
    def start(clippy):
        clippy.translations.sources.set(
                "Undo", "FingerSpelling", "Retro", "Tkfps")

        # for testing purposes
        # clippy.translations.sources.set("FingerSpelling")
        # clippy.translations.sources.append("Retro", "Tkfps")
        # clippy.translations.sources.prepend("Undo")

        clippy.distillations.sources.set(
                ["Repeat", {"num": 1}],
                ["Strokes", {"max": 3, "multi_max": 3}])

        clippy.formatting.sources.set(
                ["Org", {
                    "colorscheme": "gruvbox",
                    "mode": "defaultSuggest"}])

    @staticmethod
    def startPre(obj, clippy):
        # return obj.org.defaultPre(clippy)
        return clippy.extremity.startPre(obj, clippy)

    @staticmethod
    def startPost(obj, clippy):
        # return obj.org.defaultPost(clippy)
        return clippy.extremity.startPost(obj, clippy)

    @staticmethod
    def stopPre(obj, clippy):
        # return obj.org.defaultPre(clippy)
        return clippy.extremity.stopPre(obj, clippy)

    @staticmethod
    def stopPost(obj, clippy):
        # return obj.org.defaultPost(clippy)
        return clippy.extremity.stopPost(obj, clippy)

    @staticmethod
    def onTranslatePre(obj, clippy):
        return clippy.translations.org.defaultPre(obj, clippy)

    @staticmethod
    def onTranslateSuggest(obj, clippy):
        # return clippy.formatting.org.defaultSuggest(obj, clippy)
        return clippy.formatting.suggest(obj, clippy)

    @staticmethod
    def onTranslatePost(obj, clippy):
        return clippy.translations.org.defaultPost(obj, clippy)

    @staticmethod
    def onTranslateFilter(obj, clippy):
        # return clippy.translations.retro.filter(obj, clippy)
        return clippy.translations.filter(obj, clippy)

    @staticmethod
    def onTranslateDistill(obj, clippy):
        return clippy.distillations.distill(obj, clippy)

    @staticmethod
    def onTranslateGenerator(obj, clippy):
        # yield from clippy.translations.retro.generator(obj, clippy)
        yield from clippy.translations.generator(obj, clippy)

    @staticmethod
    def onStrokedPre(obj, clippy):
        return obj.org.defaultPre(obj, clippy)

    @staticmethod
    def onStrokedPost(obj, clippy):
        return obj.org.defaultPost(obj, clippy)
