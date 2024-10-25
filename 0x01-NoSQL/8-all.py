#!/usr/bin/env python3
"""
This module demonstrates how to interact with
MongoDB using the python module pymongo.

Functions:
    def list_all(mongo_collection: pymongo object): -> list
        Lists all documents in a collection.
"""


def list_all(mongo_collection):
    """
    List all documents in a collection.

    Args:
        mongo_collection (pymongo object): A pymongo collection of objects.
            from which to list documents.

    Returns:
        list: A list of all the documents in the collection.

    Example:
        >>> from pymongo import MongoClient
        >>> client = MongoClient('mongodb://127.0.0.1:27017')
        >>> school_collection = client.my_db.school
        >>> res = school_collection.delete_many({}) #supress output
        >>> res = school_collection.insert_one({"name": "Holberton school"})
        >>> list_all(school_collection) # doctest: +ELLIPSIS
        [{'_id': ..., 'name': 'Holberton school'}]
        >>> res = school_collection.delete_many({})
        >>> list_all(school_collection)
        []
    """
    result = list(mongo_collection.find())
    if len(result) == 0:
        return []
    return result

# Run tests if run as main module


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
