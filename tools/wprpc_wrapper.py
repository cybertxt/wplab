#!/usr/bin/env python

import os
import json
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetRecentPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

class WpWrapper:
	def __init__(self, host, username, password):
		self.xmlrpc = 'http://' + host + '/xmlrpc.php'
		self.username = username
		self.password = password
		self.wpconn = Client(self.xmlrpc, self.username, self.password)

		self.title = ''
		self.content = ''
		self.tags = ''
		self.categories = []

	def set_title(self, title):
		self.title = title
	def set_content(self, content):
		self.content = content
	def set_tags(self, tags):
		self.tags = tags
	def set_categories(self, categories):
		self.categories = categories

	def do_post(self):
		post = WordPressPost()
		post.title = self.title
		post.description = self.content
		post.tags = self.tags
		post.categories = self.categories

		return self.wpconn.call(NewPost(post, True))
	
	def post_from_json_file(self, json_file):
		json_data = os.open(json_file, 'r').read()		
		articles = json.loads(json_data)
		for article in articles:
			self.set_title(article['keyword'])
			content = article['title'] + '<br />' + article['content']
			content += '<a target="_blank" href="' + article['href'] + '">'
			content += '详细</a>'
			self.set_content(content)
			self.set_tags(article['keyword'])
			self.set_categories(['hotinfo'])

if __name__ == '__main__':
	wp = WpWrapper('localhost', 'admin-xtao', '123456')
	i = 0
	while i < 3:
		wp.set_title('test title' + str(i))
		wp.set_content('test content' + str(i))
		wp.set_tags('abc, wahaha')
		wp.set_categories(['test t1', 'test t2'])
		wp.do_post()
		print i
		print wp.title
		print wp.content
		print wp.tags
		print wp.categories
		i = i + 1
