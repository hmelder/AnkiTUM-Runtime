import mistune


class MdRenderer(mistune.HTMLRenderer):

    def __init__(self):
        super().__init__(escape=True)

    def image(self, text: str, url: str, title=None) -> str:
        """
        Ignore images
        """
        return ''

    def link(self, text: str, url: str, title=None) -> str:
        """
        Ignore links
        """
        return text
