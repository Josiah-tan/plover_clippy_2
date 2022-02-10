# from util import getOrgDate
from ..config import Config
from ..default import Defaults


class OnTranslate:
    def __init__(self, old, new):
        self.old = old
        self.new = new

    def pre(self, clippy):
        if hasattr(Config, "onTranslatePre"):
            Config.onTranslatePre(self, clippy)
        else:
            Defaults.onTranslatePre(self, clippy)

    def filter(self, clippy):
        if hasattr(Config, "onTranslateFilter"):
            return Config.onTranslateFilter(self, clippy)
        else:
            return Defaults.onTranslateFilter(self, clippy)

    def suggest(self, clippy):
        if hasattr(Config, "onTranslateSuggest"):
            Config.onTranslateSuggest(self, clippy)
        else:
            Defaults.onTranslateSuggest(self, clippy)

    def distill(self, clippy):
        if hasattr(Config, "onTranslateDistill"):
            return Config.onTranslateDistill(self, clippy)
        else:
            return Defaults.onTranslateDistill(self, clippy)

    def post(self, clippy):
        if hasattr(Config, "onTranslatePost"):
            Config.onTranslatePost(self, clippy)
        else:
            Defaults.onTranslatePost(self, clippy)

    def generator(self, clippy):
        if hasattr(Config, "onTranslateGenerator"):
            yield from Config.onTranslateGenerator(self, clippy)
        else:
            yield from Defaults.onTranslateGenerator(self, clippy)
