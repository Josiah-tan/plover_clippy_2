class Sources:
    def __init__(self, cls_available):
        self._cls_available = cls_available
        self._str_available = self.str(self._cls_available)
        self._sources = []

    def str(self, sources):
        res = []
        for source in sources:
            res.append(source.__name__)
        return res

    def get(self):
        return self._sources

    def set(self, *val):
        self._sources = ()
        for source in val:
            args = ()
            kwargs = {}
            if type(source) == str:
                source = self._cls_available[self._str_available.index(source)]
            elif hasattr(source, "__iter__"):
                assert len(source) <= 3
                for item in source:
                    if type(item) == str:
                        _source = self._cls_available[
                                self._str_available.index(item)]
                    elif isinstance(item, dict):
                        kwargs = item
                    else:
                        args = item
                source = _source
            if callable(source):
                self._sources += (source(*args, **kwargs),)
            else:
                self._sources += (source,)

    def append(self, *val):
        sources = self.get()
        self.set(*val)
        self._sources = sources + self.get()

    def prepend(self, *val):
        sources = self.get()
        self.set(*val)
        self._sources = self.get() + sources

    def wrapColor(self, obj, clippy, string):
        for source in self.get():
            if hasattr(source, "preprocess"):
                source.preprocess(obj, clippy)
            if hasattr(source, "addColor"):
                source.addColor(obj, clippy)
            if hasattr(source, string):
                # source.format(obj, clippy)
                getattr(source, string)(obj, clippy)
            if hasattr(source, "extraColor"):
                source.extraColor(obj, clippy)
            if source.output:
                clippy.actions.add(source.output)


# i = Sources()
# i.set("Retro")
# i.get()
# i.append("Org")
# i.prepend("Undo", "FingerSpelling")
# i.get()
# i.append("Tkfps")
# i.get()
