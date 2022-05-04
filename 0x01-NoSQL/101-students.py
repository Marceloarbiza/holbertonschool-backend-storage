#!/usr/bin/env python3
"""
Write a Python function that returns all students sorted by average score
"""


import pymongo


def top_students(mongo_collection):
    """ a comment """
    return mongo_collection.aggregate([
        {'$project': {
            'name': 1,
            'averageScore': {'$avg': '$topics.score'}
        }},
        {'$sort': {'averageScore': -1}}
    ])
