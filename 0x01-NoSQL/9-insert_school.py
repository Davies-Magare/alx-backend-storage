#!/usr/bin/env python3

"""
This module demonstrates how to insert a
new document in a collection based on kwargs.

Functions:
    insert_school(mongo_collection: pymongo object, **kwargs: dict) -> str

"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on kwargs

    Args:
        mongo_collection (pymongo Object): The collection of objects in
            which to insert the new document.
        **kwargs (dict): A dictionary of the dictionary key values to
            insert to the document

    Return:
        str: The id of the newly inserted document.

    Example:
        >>> from pymongo import MongoClient
        >>> client = MongoClient('mongodb://127.0.0.1:27017')
        >>> school_collection = client.my_db.school
        >>> school_id = insert_school(school_collection, name="UCSF")
        >>> len(school_id) == 24 #Hexadecimals have 24 characters
        True
        >>> isinstance(school_id, str)
        True
    """
    if kwargs:
        result = mongo_collection.insert_one(kwargs)
        return str(result.inserted_id)

# Run the doctest to check correctness of the code


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
