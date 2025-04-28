class Staff:
    name: str
    is_cs: bool

    def __init__(self, name: str, is_cs: bool):
        self.name = name
        self.is_cs = is_cs

    # My Way
    def greet(self):
        if self.is_cs is True:  # Can just say "if self.is_cs" since it is a bool.
            return f"Hello, I'm {self.name} in CS"
        else:
            return f"Hello, I'm {self.name} NOT in CS"
