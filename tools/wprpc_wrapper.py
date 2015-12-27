#!/usr/bin/env python

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

		self.wpconn.call(NewPost(post, True))

if __name__ == '__main__':
	wp = WpWrapper('localhost', 'admin-xtao', '123456')
	wp.set_title('test title')
	wp.set_content('test content')
	wp.set_tags('abc, wahaha')
	wp.set_categories(['test t1', 'test t2'])
	wp.do_post()