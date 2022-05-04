#!/usr/bin/env python3
"""
Write a Python function that returns all students sorted by average score
"""


import pymongo


def top_students(mongo_collection):
    """ a comment """
    li = []
    x = mongo_collection.find({}, {'_id': 1, 'name': 1, 'topics': 1})
    for i in x:
        lito = []
        lii = i.get('topics')
        for h in lii:
            lito.append(h.get('score'))
        suma = sum(lito)
        leni = len(lito)
        i['averageScore'] = suma/leni
        li.append(i)
    return li
