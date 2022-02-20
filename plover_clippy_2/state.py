import os.path
from plover.oslayer.config import CONFIG_DIR
from io import IOBase


class State:
    def __init__(self):
        self._output_file_name = None
        self._efficiency_symbol = None
        self._max_pad_efficiency = None
        self._max_pad_english = None
        self._f = None
        self._justify = None

        self.phrase = None
        # self.gruvbox_colors = None
        self.colors = None

    @property
    def output_file_name(self):
        return self._output_file_name

    @output_file_name.setter
    def output_file_name(self, val):
        assert type(val) == str and val != ""
        val = os.path.join(CONFIG_DIR, val)
        self._output_file_name = val

    @property
    def efficiency_symbol(self):
        return self._efficiency_symbol

    @efficiency_symbol.setter
    def efficiency_symbol(self, val):
        assert type(val) == str and val != ""
        self._efficiency_symbol = val

    @property
    def max_pad_efficiency(self):
        return self._max_pad_efficiency

    @max_pad_efficiency.setter
    def max_pad_efficiency(self, val):
        assert type(val) == int and val > 0
        self._max_pad_efficiency = val

    @property
    def max_pad_english(self):
        return self._max_pad_english

    @max_pad_english.setter
    def max_pad_english(self, val):
        assert type(val) == int and val > 0
        self._max_pad_english = val

    @property
    def f(self):
        if self._f is None or self._f.closed:
            self.f = open(self.output_file_name, "a")
        return self._f

    @f.setter
    def f(self, val):
        assert isinstance(val, IOBase)
        self._f = val

    @property
    def justify(self):
        return self._justify

    @justify.setter
    def justify(self, val):
        if type(val) == str:
            if val in "left":
                val = str.ljust
            elif val in "right":
                val = str.rjust
        self._justify = val
