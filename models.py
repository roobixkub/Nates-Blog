# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 21:43:53 2020

@author: Nate
"""


from peewee import *

import config

DATABASE = SqliteDatabase('posts.sqlite')


class Post(Model):
    title = CharField()
    content = TextField(default='')

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Post], safe=True)
    DATABASE.close()
