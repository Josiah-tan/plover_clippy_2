from ..sources import Sources
from .stop import Stop
from .start import Start


class Extremity:
    def __init__(self):
        self.stop_pre_sources = Sources([Stop])
        self.start_pre_sources = Sources([Start])

        self.stop_post_sources = Sources([Stop])
        self.start_post_sources = Sources([Start])

    def stopPost(self, obj, clippy):
        self.stop_post_sources.wrapColor(obj, clippy, "stop")

    def startPost(self, obj, clippy):
        print(f"self.stop_post_sources.get() = {self.stop_post_sources.get()}")
        self.start_post_sources.wrapColor(obj, clippy, "start")

    def stopPre(self, obj, clippy):
        self.stop_pre_sources.wrapColor(obj, clippy, "stop")

    def startPre(self, obj, clippy):
        self.start_pre_sources.wrapColor(obj, clippy, "start")
