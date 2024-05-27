from flask import Flask, Blueprint, request
from flask_restx import Api, Resource, fields

app=Flask(__name__)

api=Api(app=app, version='1.0.0', title="Testing Swagger API", description="This swagger is only for testing purpose")


