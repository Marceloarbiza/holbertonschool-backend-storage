#!/usr/bin/env python3
"""
Write a Python function that returns the
list of school having a specific topic:
"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """ a comment """
    li = []
    x = mongo_collection.find({}, {'_id': 1, 'name': 1, 'topics': 1})
    for i in x:
        if i.get('topics') is not None and topic in i.get('topics'):
            li.append(i)
    return li
