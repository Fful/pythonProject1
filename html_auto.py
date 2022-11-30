class Element:
    def __init__(self, text=None, subelement=None):
        self.text = text
        self.subelement = subelement

    def __str__(self):
        val = f'<{self.__class__.__name__}>\n'
        if self.text:
            val += f'{self.text}\n'
        if self.subelement:
            val += f'{self.subelement}\n'
        val += f'</{self.__class__.__name__}>'
        return val


class html(Element):
    def __init__(self, text=None, subelement=None):
        super().__init__(text, subelement)

    def __str__(self):
        return super().__str__()


class body(Element):
    def __init__(self, text=None, subelement=None):
        super().__init__(text, subelement)

    def __str__(self):
        return super().__str__()


class p(Element):
    def __init__(self, text=None, subelement=None):
        super().__init__(text, subelement)

    def __str__(self):
        return super().__str__()


para = p(text="this is some body text")
doc_body = body(text="This is the body", subelement=para)
doc = html(subelement=doc_body)
print(doc)
