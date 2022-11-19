"""
A common interface
"""
class Machine:
    @abstractmethod
    def print(self, document):
        raise NotImplementedError

    @abstractmethod
    def fax(self, document):
        raise NotImplementedError

    @abstractmethod
    def scan(self, document):
        raise NotImplementedError

"""
    Forced to implement all methods.
"""
class OldFashionedPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

"""
    Fix to comply with interface segregation principle.
    
    Common interface split into 3 different.
"""
class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class Fax:
    @abstractmethod
    def fax(self, document):
        pass



"""
    Implemenation Classes
"""

class MyPrinter(Printer):
    def print(self, document):
        print(document)

class PhotoCopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        # provide actual implementation
        pass


"""
    Machine interface can still be defined by inherting from all differnt interfaces.
"""
class MultiFunctionDevice(Printer, Scanner, Fax):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass