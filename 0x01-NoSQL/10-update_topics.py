#!/usr/bin/env python3

"""
This module demonstrates how to update
documents in MongoDB.

Functions:
    update_topics(mongo_collection: pymongo object, topics: List) -> None
        Changes all topics of a school document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Change all topics of a school document based on the name

    Args:
        mongo_collection (pymongo object): The pymongo collection object
        to update the topic property.
        name (string): The school name to update.
        topics (list): The list of topics approached in the school.

    Examples:
        >>> from pymongo import MongoClient
        >>> client = MongoClient('mongodb://127.0.0.1:27017')
        >>> school_collection = client.my_db.school
        >>> res = school_collection.delete_many({}) #suppress output
        >>> res = school_collection.insert_one({"name": "Kioge", "topics": []})
        >>> update_topics(school_collection, "Kioge", ["Maths"])
        >>> list_all = __import__('8-all').list_all
        >>> schools = list_all(school_collection)
        >>> for school in schools:
        ...     print(f"{school.get('name')} {school.get('topics')}")
        Kioge ['Maths']
    """

    query_filter = {'name': name}
    update_operation = {'$set':
                        {'topics': topics}
                        }
    mongo_collection.update_many(query_filter, update_operation)

# Run the tests to verify the correctness of the code


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
