class SimpleConverter:
    regex = "[1-9]+"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return value
