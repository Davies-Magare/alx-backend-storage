#!/usr/bin/env python3

"""
This document demonstrates how to query a database
for fields with array values containing a specific value

Functions:
    schools_by_topic(mongo_collection: pymongo object, topic: str) -> list:
        return list of schools with specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return the list of schools having a specific topic

    Args:
        mongo_collection (pymongo object): A pymongo collection object
            from which to search documents whose array fields have the
            topic value.
        topic (str): The topic to be searched in the collection.
    Returns:
        list: The list of schools having a specific topic

    Example:
        #The Res variable has been used to repress output
        >>> from pymongo import MongoClient
        >>> insert_school = __import__('9-insert_school').insert_school
        >>> client = MongoClient('mongodb://127.0.0.1:27017')
        >>> school_collection = client.my_db.school
        >>> code_schools = [
        ...    {'name': "UCLA", 'topics': ["C", "Python"]},
        ...    {'name': "UCSD", 'topics': ["Cassandra", "Python"]},
        ...    {'name': "Kioge", 'topics': ['Scheme']}
        ... ]
        >>> res = school_collection.delete_many({})
        >>> for school in code_schools:
        ...    res = insert_school(school_collection, **school)
        >>> schools = schools_by_topic(school_collection, "Python")
        >>> for school in schools:
        ...    print(f"{school.get('name')} {school.get('topics')}")
        UCLA ['C', 'Python']
        UCSD ['Cassandra', 'Python']
    """
    return list(mongo_collection.find({"topics": {"$in": [topic]}}))


# Run doctests to verify correctness of the code
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
