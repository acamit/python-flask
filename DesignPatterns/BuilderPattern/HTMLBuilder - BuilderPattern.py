class HtmlElement:

    indent_size = 2

    def __init__(self, name='', text=''):
        self.text = text
        self.name = name
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * (indent * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent+1))

        lines.append(f'{i}</{self.name}>')

        return '\n'.join(lines)

    def __str__(self):
        self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(name=self.root_name)

    def __str__(self):
        return str(self.__root)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))

    # return self to allow chaining
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))
        return self

    def clear(self):
        self.__root = HtmlElement(name=self.root_name)


# ordinary non-fluent builder

#way 1
# builder = HtmlBuilder('ul')

# way 2
builder = HtmlElement.create('ul')
builder.add_child('li', 'hello')
builder.add_child('li', 'world')
print('Ordinary builder:')
print(builder)

# fluent builder
builder.clear()
builder.add_child_fluent('li', 'hello') \
    .add_child_fluent('li', 'world')
print('Fluent builder:')
print(builder)
