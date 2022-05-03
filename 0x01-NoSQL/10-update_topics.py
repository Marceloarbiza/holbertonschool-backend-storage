#!/usr/bin/env python3
"""
Write a Python function that changes all
topics of a school document based on the name
"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """ a comment """
    return mongo_collection.find_one_and_update({'name': name},
                                                {'$set': {'topics': topics}})
