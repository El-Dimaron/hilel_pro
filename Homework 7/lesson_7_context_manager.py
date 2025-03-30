class Colorizer:
    MAIN_COLORS_DICT = {
        "default": '\033[0m',
        "bold": '\033[1m',
        "faint": '\033[2m',
        "italic": '\033[3m',
        "underline": '\033[4m',
        "grey": '\033[90m',
        "red": '\033[91m',
        "green": '\033[92m',
        "yellow": '\033[93m',
        "blue": '\033[94m',
        "pink": '\033[95m',
        "turquoise": '\033[96m',
    }

    BACKGROUND_COLORS_DICT = {
        "default": '\033[0m',
        "grey": '\033[100m',
        "red": '\033[101m',
        "green": '\033[102m',
        "yellow": '\033[103m',
        "blue": '\033[104m',
        "pink": '\033[105m',
        "turquoise": '\033[106m',
    }

    def __init__(self, main_color: str, background_color: str = None):
        self.color = self.MAIN_COLORS_DICT.get(main_color, "default")
        if background_color:
            self.background_color = self.BACKGROUND_COLORS_DICT.get(background_color, None)
        else:
            self.background_color = background_color

    def __enter__(self):
        print(self.color, end='')
        if self.background_color:
            print(self.background_color, end='')

    def __exit__(self, type, value, traceback):
        print(self.MAIN_COLORS_DICT.get("default"), end='')
