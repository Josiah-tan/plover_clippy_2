# from .util import noNewOutput
from .state import State
from .default import Defaults
from .actions import Actions
from .translations import Translations
from .formatting import Formatting

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
        self.formatting = Formatting()

        Defaults.init(self)

        hook.post(self)

    def start(self) -> None:
        hook = Start()
        hook.pre(self)
        # this order can't be changed ;<
        self.engine.hook_connect('translated', self.onTranslate)
        self.engine.hook_connect('stroked', self.onStroked)
        self.state.f = open(self.state.output_file_name, 'a')

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
        print(self.state.prev_stroke)
        # not sure what else to do here for now
        hook.post(self)

    def onTranslate(self, old, new):
        hook = OnTranslate(old, new)
        hook.pre(self)
        if hook.filter(self):
            for phrase in hook.generator(self):
                self.state.phrase = phrase
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
