from  enum import Enum
"""
    High level modules should not directly depend on low level modules,
    instead they should depend on abstractions.
"""

class RelationShip(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name

"""
    This interface is being created for fixing the DIP problem defined below.
"""
class RelationshipBrowser:
    @abstractmethod
    def find_all_childern_of(self, name):
        pass

# class RelationShips:
class RelationShips(RelationshipBrowser): # now this class is changed to inherit from relationship browser.
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent,child):
        self.relations.append(
                (parent, RelationShip.PARENT, child))

        self.relations.append(
            (child, RelationShip.CHILD, parent))

    def find_all_childern_of(self, name):
        for r in relations:
            if r[0].name == name and r[1] == RelationShip.PARENT:
                yield r[2].name

class Research: # high livel module

    """
     Problem - Dependency Inversion principle violated
     This module depends on a low level detail of Relations class.
     Now if we want to change storage from list to dictionary in Relationships class,
     we can not do so. Since this module depends on the list.

     Fix: We have to define interface and methods in relationships to search for the same.

     RelationshipBrowser above is that interface.
     The search funtionality is now moved to Relationship class which implements this interface.
    """

    # def __init__(self, relationships):
    # relations = relationships.relations
    #
    # for r in relations:
    #     if r[0].name == 'John' and r[1] == RelationShip.PARENT:
    #         print(f'John has a child called {r[2].name}')
    def __init__(self, browser):
        for p in browser.find_all_childern_of("John"):
            print(f'John has a child called {p}')


parent = Person("John")
child1 = Person("chris")
child2 = Person("matt")

relations = RelationShips()
relations.add_parent_and_child(parent, child1)
relations.add_parent_and_child(parent, child2)

Research(relations)