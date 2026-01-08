class ParseError(Exception):
    def __init__(self, error):
        super().__init__(f"ParseError: {error}")
