class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.properties = []

    def add_field(self, type, name):
        self.properties.append((type, name))
        return self

    def __str(self, indent):
        lines = []
        lines.append(f'class {self.root_name}')
        i1 = ' ' * (indent+1)
        lines.append(f'{i1}def __init__(self)')
        i2 = ' ' * (indent+2)
        for p in self.properties:
            lines.append(f'{i2}self.{p[0]} = {p[1]}')

        return '\n'.join(lines)

    def __str__(self):
       return self.__str(0)

cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
print(cb)