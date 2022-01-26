class Actions:
    def __init__(self, state):
        self.state = state

    def add(self, output, end="\n"):
        self.state.f.write(f"{output}{end}")
        self.state.f.flush()
