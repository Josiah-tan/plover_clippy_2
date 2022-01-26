from .util import noNewOutput
from .state import State
from .default import Defaults
from .actions import Actions
from .translations import Translations

from .hooks.initialize import Initialize
from .hooks.start import Start
from .hooks.stop import Stop
from .hooks.translate import OnTranslate

from plover.engine import StenoEngine


class Clippy:
    def __init__(self, engine: StenoEngine) -> None:
        super().__init__()

        hook = Initialize()
        hook.pre(self)

        self.engine: StenoEngine = engine
        self.state = State()
        self.actions = Actions(self.state)
        self.translations = Translations(self)

        Defaults.init(self)

        hook.post(self)

    def start(self) -> None:
        hook = Start()
        hook.pre(self)
        self.engine.hook_connect('translated', self.onTranslate)
        self.state.f = open(self.state.output_file_name, 'a')

        hook.post(self)

    def stop(self) -> None:
        hook = Stop()
        hook.pre(self)

        self.engine.hook_disconnect('translated', self.onTranslate)
        self.state.f.close()

        hook.post(self)

    def onTranslate(self, old, new):
        hook = OnTranslate()
        hook.pre(self)

        if noNewOutput(new):
            return

        for phrase in self.translations.generator():

            (
                self.state.english,
                self.state.stroked,
                self.state.suggestions
            ) = phrase

            hook.call(self)

        hook.post(self)
