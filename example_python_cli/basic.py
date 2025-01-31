"""
Basic class to demonstrate the usage of the CLI. Replace this with your own code.
"""
from typing import List, Optional
class Basic:
    """
    Basic class to demonstrate the usage of the CLI. Replace this with your own code.
    """
    def __init__(
        self,
        name: str,
        age: Optional[int] = None,
        city: str = "Unknown",
        email: str = "",
        married: bool = False,
        score: float = 0.0,
        languages: Optional[List[str]] = None,
        debug: bool = False,
        mode: str = "medium",
        verbose: bool = False,
        quiet: bool = False
    ) -> None:
        self.name = name
        self.age = age
        self.city = city
        self.email = email
        self.married = married
        self.score = score
        self.languages = languages or []
        self.debug = debug
        self.mode = mode
        self.verbose = verbose
        self.quiet = quiet

    def run(self):
        """
        Run the basic class
        """
        print("Running basic class")

    def raises_runtime_error(self) -> None:
        """
        Raise a runtime error
        """
        raise RuntimeError("Runtime error raised")
