class SubcommandOne:
    def run(self) -> None:
        print('Subcommand One has been run')
        
    def raises_runtime_error(self) -> None:
        raise RuntimeError("Runtime error raised")