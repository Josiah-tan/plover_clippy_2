from collections.abc import Iterable
import os.path
from plover.oslayer.config import CONFIG_DIR


class Preprocess:
    def __init__(self):
        self.fname = os.path.join(CONFIG_DIR, 'clippy_2_cfg.py')
        self.mod = {}

    def sourceConfig(self):
        if os.path.isfile(self.fname):
            with open(self.fname, encoding='utf-8') as fp:
                source = fp.read()
            exec(source, self.mod)

    def isSingleInstance(self):
        config = self.mod.get('config')
        return (config is not None and
                not isinstance(config, Iterable))

    def handleSingleInstance(self):
        return [self.mod.get('config')]

    def isIterable(self):
        config = self.mod.get('config')
        return config is not None and isinstance(
                config, Iterable)

    def handleIterable(self):
        lis = []
        for c in self.mod.get('config'):
            if callable(c):
                lis.append(c())
            else:
                lis.append(c)
        return lis

    def isSingleClass(self):
        return self.mod.get('Config') is not None

    def handleSingleClass(self):
        return [self.mod.get('Config')()]

    def handleJustFunctions(self):
        class Config:
            pass
        for key, value in self.mod.items():
            if key == "__builtins__":
                continue
            else:
                setattr(Config, key, staticmethod(value))
        return [Config()]

    def getConfig(self):
        if self.isSingleInstance():
            return self.handleSingleInstance()
        elif self.isIterable():
            return self.handleIterable()
        elif self.isSingleClass():
            return self.handleSingleClass()
        else:
            return self.handleJustFunctions()


if __name__ == "__main__":
    preprocess = Preprocess()

    class Config:
        pass
    preprocess.mod = {"config": Config()}
    print(preprocess.getConfig())

    preprocess.mod = {"config": (Config(), Config(), Config())}
    print(preprocess.getConfig())
    preprocess.mod = {"config": [Config(), Config(), Config()]}
    print(preprocess.getConfig())

    preprocess.mod = {"Config": Config}
    print(preprocess.getConfig())

    preprocess.mod = {"function1": (lambda x: x), "function2": (lambda y: y)}
    print(preprocess.getConfig())

else:
    preprocess = Preprocess()
    preprocess.sourceConfig()
    config = preprocess.getConfig()
