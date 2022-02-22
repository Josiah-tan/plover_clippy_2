# from util import getOrgDate
# from ..config import config
from ..default import Defaults


class OnTranslate:
    def __init__(self, config, old, new):
        self.config = config
        self.old = old
        self.new = new

    def pre(self, clippy):
        if hasattr(self.config, "onTranslatePre"):
            self.config.onTranslatePre(self, clippy)
        else:
            Defaults.onTranslatePre(self, clippy)

    def filter(self, clippy):
        if hasattr(self.config, "onTranslateFilter"):
            return self.config.onTranslateFilter(self, clippy)
        else:
            return Defaults.onTranslateFilter(self, clippy)

    def suggest(self, clippy):
        if hasattr(self.config, "onTranslateSuggest"):
            self.config.onTranslateSuggest(self, clippy)
        else:
            Defaults.onTranslateSuggest(self, clippy)

    def distill(self, clippy):
        if hasattr(self.config, "onTranslateDistill"):
            return self.config.onTranslateDistill(self, clippy)
        else:
            return Defaults.onTranslateDistill(self, clippy)

    def post(self, clippy):
        if hasattr(self.config, "onTranslatePost"):
            self.config.onTranslatePost(self, clippy)
        else:
            Defaults.onTranslatePost(self, clippy)

    def generator(self, clippy):
        if hasattr(self.config, "onTranslateGenerator"):
            yield from self.config.onTranslateGenerator(self, clippy)
        else:
            yield from Defaults.onTranslateGenerator(self, clippy)
