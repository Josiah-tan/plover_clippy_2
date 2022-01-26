import os.path
from plover.oslayer.config import CONFIG_DIR

fname = os.path.join(CONFIG_DIR, 'clippy_2_cfg.py')
mod = {}

if os.path.isfile(fname):
    with open(fname, encoding='utf-8') as fp:
        source = fp.read()
    exec(source, mod)

Config = mod.get('Config')

if not Config:
    class Config:
        pass

    for key, value in mod.items():
        if key == "__builtins__":
            continue
        else:
            setattr(Config, key, staticmethod(value))
