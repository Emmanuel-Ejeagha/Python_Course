#!/usr/bin/python3
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
  {
	'id': 1,
	'title': u'Learn Python',
	'discription': u'Need to find a good Python tutorial on the web',
	'done': False
  },
  {
	'id': 2,
	'title': u'Buy groceries',
	'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
	'done': False
  }
]

@app.route('/
