"""
example of interface segregated principle from
https://realpython.com/solid-principles-python/#liskov-substitution-principle-lsp
"""
# pylint: disable=too-few-public-methods

# The principle’s main idea is that:

# Clients should not be forced to depend upon methods that they do not use.
# Interfaces belong to clients, not to hierarchies.
# In this case, clients are classes and subclasses, and interfaces consist of
# methods and attributes. In other words, if a class doesn’t use particular
# methods or attributes, then those methods and attributes should be segregated
# into more specific classes.

from abc import ABC, abstractmethod


class Printer(ABC):
    """Printer interface"""

    @abstractmethod
    def print(self, document: str) -> None:
        """print a document

        Args:
            document (str): document to print
        """

    @abstractmethod
    def fax(self, document: str):
        """fax a document

        Args:
            document (str): document to fax
        """

    @abstractmethod
    def scan(self, document: str) -> None:
        """scan a documents

        Args:
            document (str): document to scan
        """


class OldPrinter(Printer):
    """Old printer class"""

    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document: str) -> None:
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document) -> None:
        raise NotImplementedError("Scan functionality not supported")


class ModernPrinter(Printer):
    """Modern printer class with all functionalities"""

    def print(self, document: str) -> None:
        print(f"Printing {document} in color...")

    def fax(self, document: str) -> None:
        print(f"Faxing {document}...")

    def scan(self, document: str) -> None:
        print(f"Scanning {document}...")


# In this example, the base class, Printer, provides the interface
# that its subclasses must implement. OldPrinter inherits from Printer
# and must implement the same interface. However, OldPrinter doesn’t use
# the .fax() and .scan() methods because this type of printer doesn’t support
# these functionalities.

# This implementation violates the ISP because it forces OldPrinter to expose
# an interface that the class doesn’t implement or need. To fix this issue,
# you should separate the interfaces into smaller and more specific classes.
# Then you can create concrete classes by inheriting from multiple interface
# classes as needed:


class ISPPrinter(ABC):
    """class to define printer interface"""

    @abstractmethod
    def print(self, document: str) -> None:
        """print a document"""


class ISPFax(ABC):
    """class to define fax interface"""

    @abstractmethod
    def fax(self, document: str) -> None:
        """fax a document

        Args:
            document (str): document to fax
        """


class ISPScanner(ABC):
    """class to define scanner interface"""

    @abstractmethod
    def scan(self, document: str) -> None:
        """scan a document"""


class ISPOldPrinter(Printer):
    """class to define old printer"""

    def print(self, document: str) -> None:
        print(f"Printing {document} in black and white...")


class ISPNewPrinter(ISPPrinter, ISPFax, ISPScanner):
    """class to define new printer"""

    def print(self, document: str) -> None:
        print(f"Printing {document} in color...")

    def fax(self, document: str) -> None:
        print(f"Faxing {document}...")

    def scan(self, document: str) -> None:
        print(f"Scanning {document}...")
