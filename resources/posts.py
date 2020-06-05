# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:00:29 2020

@author: Nate
"""


import json

from flask import Blueprint, abort, make_response

from flask_restful import (Resource, Api, reqparse, inputs, fields,
                           url_for, marshal, marshal_with)

import models


post_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String(default='')
    }

def post_or_404(post_id):
    try:
        post = models.Post.get(models.Post.id==post_id)
    except models.Post.DoesNotExist:
        abort(404)
    else:
        return post

class PostList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'content',
            required=False,
            nullable=True,
            location=['form', 'json'],
            default=''
        ),
        self.reqparse.add_argument(
            'title',
            required=True,
            help='No post title provided',
            location=['form', 'json']
        )
        super().__init__()
        
    def get(self):
        posts = [marshal(post, post_fields) 
                   for post in models.Post.select()]
        return {'posts': posts}

    @marshal_with(post_fields)
    def post(self):
        args = self.reqparse.parse_args()
        post = models.Post.create(**args)
        return (post, 201, {
                'Location': url_for('resources.posts.post', id=post.id)}
               )


class Post(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'content',
            required=False,
            nullable=True,
            location=['form', 'json'],
            default=''
        ),
        self.reqparse.add_argument(
            'title',
            required=True,
            help='No post title provided',
            location=['form', 'json']
        )
        super().__init__()
    
    @marshal_with(post_fields)
    def get(self, id):
        return post_or_404(id)

    @marshal_with(post_fields)
    def put(self, id):
        args = self.reqparse.parse_args()
        query = models.Post.update(**args).where(models.Post.id==id)
        query.execute()
        return (models.Post.get(models.Post.id==id), 200, 
                {'Location': url_for('resources.posts.post', id=id)})

    def delete(self, id):
        query = models.Post.delete().where(models.Post.id==id)
        query.execute()
        return '', 204, {'Location': url_for('resources.posts.posts')}


posts_api = Blueprint('resources.posts', __name__)
api = Api(posts_api)
api.add_resource(
    PostList,
    '/posts',
    endpoint='posts'
)
api.add_resource(
    Post,
    '/posts/<int:id>',
    endpoint='post'
)
