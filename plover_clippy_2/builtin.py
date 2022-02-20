from .state import State
from .default import Defaults
from .actions import Actions
from .translations import Translations
from .distillations import Distillations
from .formatting import Formatting
from .extremity import Extremity

from .hooks.initialize import Initialize
from .hooks.start import Start
from .hooks.stop import Stop
from .hooks.translate import OnTranslate
from .hooks.stroke import OnStroked

from plover.engine import StenoEngine
# from plover.translation import Translation


class Clippy:
    def __init__(self, engine: StenoEngine) -> None:
        super().__init__()

        hook = Initialize()
        hook.pre(self)

        self.engine: StenoEngine = engine
        self.state = State()
        self.actions = Actions(self.state)
        self.translations = Translations()
        self.distillations = Distillations()
        self.formatting = Formatting()
        self.extremity = Extremity()

        Defaults.init(self)

        hook.post(self)

    def start(self) -> None:
        hook = Start()
        hook.pre(self)
        # this order can't be changed ;<
        self.engine.hook_connect('translated', self.onTranslate)
        self.engine.hook_connect('stroked', self.onStroked)
        self.state.f = open(self.state.output_file_name, 'a')

        Defaults.start(self)

        hook.post(self)

    def stop(self) -> None:
        hook = Stop()
        hook.pre(self)

        self.engine.hook_disconnect('translated', self.onTranslate)
        self.engine.hook_disconnect('stroked', self.onStroked)
        self.state.f.close()

        hook.post(self)

    def onStroked(self, stroke):
        if not self.engine.output:
            return
        hook = OnStroked(stroke)
        hook.pre(self)
        # print(self.state.prev_stroke)
        # not sure what else to do here for now
        hook.post(self)

    def onTranslate(self, old, new):
        hook = OnTranslate(old, new)
        hook.pre(self)
        if hook.filter(self):
            for phrase in hook.generator(self):
                self.state.phrase = phrase
                # hook.suggest(self)
                if hook.distill(self):
                    hook.suggest(self)
        hook.post(self)
        # if noNewOutput(new):
        #     return
        # for phrase in self.translations.generator():
        #
        #     (
        #         self.state.english,
        #         self.state.stroked,
        #         self.state.suggestions
        #     ) = phrase
        #     print(f"phrase = {phrase}")
        #
        #     hook.call(self)
        #
        # hook.post(self)


##



# import re
#
# from plover.formatting import RetroFormatter
#
#
# WORD_RX = re.compile(r'(?:\w+|[^\w\s]+)\s*')
#
#
# class Clippy:
#
#     def __init__(self, engine):
#         self._engine = engine
#
#     def start(self):
#         self._engine.hook_connect('translated', self._on_translate)
#
#     def stop(self):
#         self._engine.hook_disconnect('translated', self._on_translate)
#
#     def _on_translate(self, old, new):
#         # Check for new output.
#         for a in reversed(new):
#             if a.text and not a.text.isspace():
#                 break
#         else:
#             return
#         # Get the last 10 words.
#         with self._engine:
#             last_translations = self._engine.translator_state.translations
#             retro_formatter = RetroFormatter(last_translations)
#             last_words = retro_formatter.last_words_with_translations(10, rx=WORD_RX)
#             print('last', len(last_words), 'words:')
#             for word, translations in last_words:
#                 print('-', repr(word), len(translations), translations)
#
#
# def test():
#     from mock import MagicMock
#     from plover import system
#     from plover.config import DEFAULT_SYSTEM_NAME
#     from plover.registry import registry
#     from plover.steno import Stroke
#     from plover.translation import Translation
#     from plover.formatting import Formatter
#
#     last_translations = []
#
#     registry.update()
#     system.setup(DEFAULT_SYSTEM_NAME)
#     engine = MagicMock()
#     formatter = Formatter()
#     engine.translator_state.translations = last_translations
#     on_stroked = Clippy(engine)
#     on_stroked.start()
#     assert len(engine.hook_connect.mock_calls) == 1
#     call = engine.hook_connect.mock_calls[0]
#     assert len(call.args) == 2 and call.args[0] == 'translated'
#     formatter.add_listener(call.args[1])
#
#     for line in '''
#     S-G      something
#     WEUBG    wick
#     -D       {^ed}
#     TH       this
#     WAEU     way
#     KOPL     come
#     '''.strip().split('\n'):
#         steno, translation = line.split(None, 1)
#         print(steno, '->', repr(translation))
#         strokes = list(map(Stroke.from_steno, steno.split('/')))
#         new = [Translation(strokes, translation)]
#         last_translations.extend(new)
#         formatter.format([], new, None)
#
# if __name__ == '__main__':
#     test()
#
#
# ##
#
# # playing around with mock
#
# # from unittest.mock import Mock
# # mock = Mock()
# # mock.some_attribute
# # mock.do_something()
# # json = Mock()
# # json.loads('{"k": "v"}').get('k')
#
# ##
#
#
#
