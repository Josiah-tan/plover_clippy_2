# from util import getOrgDate
from ..config import config
from ..default import Defaults


class OnTranslate:
    def __init__(self, old, new):
        self.old = old
        self.new = new

    def pre(self, clippy):
        if hasattr(config, "onTranslatePre"):
            config.onTranslatePre(self, clippy)
        else:
            Defaults.onTranslatePre(self, clippy)

    def filter(self, clippy):
        if hasattr(config, "onTranslateFilter"):
            return config.onTranslateFilter(self, clippy)
        else:
            return Defaults.onTranslateFilter(self, clippy)

    def suggest(self, clippy):
        if hasattr(config, "onTranslateSuggest"):
            config.onTranslateSuggest(self, clippy)
        else:
            Defaults.onTranslateSuggest(self, clippy)

    def distill(self, clippy):
        if hasattr(config, "onTranslateDistill"):
            return config.onTranslateDistill(self, clippy)
        else:
            return Defaults.onTranslateDistill(self, clippy)

    def post(self, clippy):
        if hasattr(config, "onTranslatePost"):
            config.onTranslatePost(self, clippy)
        else:
            Defaults.onTranslatePost(self, clippy)

    def generator(self, clippy):
        if hasattr(config, "onTranslateGenerator"):
            yield from config.onTranslateGenerator(self, clippy)
        else:
            yield from Defaults.onTranslateGenerator(self, clippy)
