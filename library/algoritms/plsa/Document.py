class Document:

    def __init__(self, text, tag):
        self._text = text.strip()
        self._text_as_list = []
        self._tag = tag.strip()

    def get_text(self):
        return self._text
