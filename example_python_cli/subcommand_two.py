class SubcommandTwo:
    """
    SubcommandTwo class
    """
    def run(self) -> None:
        """
        Run the subcommand
        """
        print('Subcommand two executed')
        
    def raises_runtime_error(self) -> None:
        raise RuntimeError("Runtime error raised")