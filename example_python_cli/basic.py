class Basic:
    def __init__(self):
        pass

    def run(self):
        print("Running basic class")

    def raises_runtime_error(self) -> None:
        raise RuntimeError("Runtime error raised")
