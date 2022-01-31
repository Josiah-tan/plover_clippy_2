class Defaults:
    @staticmethod
    def initPre(obj, clippy):
        return obj.orgDefaultPre(clippy)

    @staticmethod
    def init(clippy):
        clippy.state.output_file_name = "clippy_2.org"
        clippy.state.efficiency_symbol = "*"
        clippy.state.max_pad_efficiency = 5
        clippy.state.max_pad_english = 15

    @staticmethod
    def initPost(obj, clippy):
        pass
        # return obj.orgDefaultPost(clippy)

    @staticmethod
    def startPre(obj, clippy):
        return obj.orgDefaultPre(clippy)

    @staticmethod
    def startPost(obj, clippy):
        return obj.orgDefaultPost(clippy)

    @staticmethod
    def stopPre(obj, clippy):
        return obj.orgDefaultPre(clippy)

    @staticmethod
    def stopPost(obj, clippy):
        return obj.orgDefaultPost(clippy)

    @staticmethod
    def onTranslatePre(obj, clippy):
        return obj.orgDefaultPre(clippy)

    @staticmethod
    def onTranslateCall(obj, clippy):
        return obj.orgDefaultCall(clippy)

    @staticmethod
    def onTranslatePost(obj, clippy):
        return obj.orgDefaultPost(clippy)
