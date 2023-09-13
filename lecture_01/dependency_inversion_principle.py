""" Example of dependency inversion principle
"""
from abc import ABC, abstractmethod

# pylint: disable=too-few-public-methods
# Main Idea of principle: Abstractions should not depend upon details.
# Details should depend upon abstractions.


# That sounds pretty complex. Here’s an example that will help to clarify it.
# Say you’re building an application and have a FrontEnd class to display
# data to the users in a friendly way.
# The app currently gets its data from a database,
# so you end up with the following code:


class BackEnd:
    """class to define the backend of the app"""

    def get_data_from_database(self) -> str:
        """get data from the database

        Returns:
            str: data from the database
        """
        return "Data from the database"


class FrontEnd:
    """class to define the frontend of the app"""

    def __init__(self, back_end: BackEnd) -> None:
        """init frontend

        Args:
            back_end (BackEnd): backend of the app
        """
        self.back_end = back_end

    def display_data(self) -> None:
        """display the data used in the app"""
        data = self.back_end.get_data_from_database()
        print("Display data:", data)


# In this example, the FrontEnd class depends on the BackEnd class and its
# concrete implementation. You can say that both classes are tightly coupled.
# This coupling can lead to scalability issues. For example, say that your app is
# growing fast, and you want the app to be able to read data from a REST API.
# How would you do that?
# You may think of adding a new method to BackEnd to retrieve the data
# from the REST API.
# However, that will also require you to modify FrontEnd, which should be closed to
# modification, according to the open-closed principle.
# To fix the issue, you can apply the dependency inversion principle and make your
# classes depend on abstractions rather than on concrete implementations like BackEnd.
# In this specific example, you can introduce a DataSource class
# that provides the interface to use in your concrete classes:

# app_dip.py


class DIPDataSource(ABC):
    """class to define the data source interface"""

    @abstractmethod
    def get_data(self) -> str:
        """get data from the data source

        Returns:
            str: data from the data source
        """


class DIPFrontEnd:
    """class to define the frontend of the app"""

    def __init__(self, data_source: DIPDataSource):
        self.data_source = data_source

    def display_data(self) -> None:
        """print data from the data source"""
        data = self.data_source.get_data()
        print("Display data:", data)


class Database(DIPDataSource):
    """class to define the database"""

    def get_data(self) -> str:
        """get data from the database

        Returns:
            str: returned data
        """
        return "Data from the database"


class API(DIPDataSource):
    """class to define the API"""

    def get_data(self):
        return "Data from the API"


# In this redesign of your classes, you’ve added a DataSource class as an
# abstraction that provides the required interface, or the .get_data() method.
# Note how FrontEnd now depends on the interface provided by DataSource,
# which is an abstraction.
# Then you define the Database class, which is a concrete implementation for
# those cases where you want to retrieve the data from your database.
# This class depends on the DataSource abstraction through inheritance.
# Finally, you define the API class to support retrieving the data from the REST API.
# This class also depends on the DataSource abstraction.

# Now, you can use the FrontEnd class with any class that implements the
# DataSource interface.
# >>> from app_dip import API, Database, FrontEnd

# >>> db_front_end = FrontEnd(Database())
# >>> db_front_end.display_data()
# Display data: Data from the database

# >>> api_front_end = FrontEnd(API())
# >>> api_front_end.display_data()
# Display data: Data from the API
