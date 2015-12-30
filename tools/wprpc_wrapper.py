#!/usr/bin/env python

import os
import time
import json
from wordpress_xmlrpc import Client, WordPressPost, WordPressTerm
from wordpress_xmlrpc.methods import taxonomies
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

class WpPostWrapper:
	def __init__(self, postid=0, title='', content='', tags='', categories=[]):
		self.postid = postid
		self.title = title
		self.content = content
		self.tags = tags
		self.categories = categories
		
	def set_postid(self, postid):
		self.postid = postid
	def set_title(self, title):
		self.title = title
	def set_content(self, content):
		self.content = content
	def set_tags(self, tags):
		self.tags = tags
	def set_categories(self, categories):
		self.categories = categories

class WpTermWrapper:
	def __init__(self, termid=0, name='', taxonomy_name=''):
		self.termid = termid
		self.name = name
		self.taxonomy_name = taxonomy_name

	def set_termid(self, termid):
		self.termid = termid
	def set_name(self, name):
		self.name = name
	def set_taxonomy_name(self, taxonomy_name):
		self.taxonomy_name = taxonomy_name

class WpWrapper:
	def __init__(self, host, username, password):
		self.xmlrpc = 'http://' + host + '/xmlrpc.php'
		self.username = username
		self.password = password
		self.wpconn = Client(self.xmlrpc, self.username, self.password)

	def new_post(self, post, extinfo=''):
		wppost = WordPressPost()
		wppost.title = post.title
		wppost.content = post.content
		if extinfo != '':
			wppost.content += u'<br />'
			wppost.content += extinfo
			wppost.content += u'<br />'
		#wppost.tags = post.tags
		#wppost.categories = post.categories
		wppost.post_status = 'publish'
		print 'Posting [%s]...' % wppost.title,
		postid = self.wpconn.call(NewPost(wppost))
		print 'done'
		return postid
	
	def post_from_json_file(self, json_file, batextinfo=''):
		json_data = open(json_file, 'r').read()		
		articles = json.loads(json_data)
		for article in articles:
			post = WpPostWrapper()
			post.set_title(article['keyword'])
			content = article['title']
			content += u'<br />'
			content += article['content']
			content += u'<a target="_blank" href="' + article['href'] + u'">'
			content += u'more'
			content += u'</a>'
			post.set_content(content)
			post.set_tags(article['keyword'])
			post.set_categories(['hotinfo'])
			postid = self.new_post(post, batextinfo)
			post.set_postid(postid)
			#time.sleep(1)
	
	def get_posts(self, number, offset):
		wpposts = self.wpconn.call(posts.GetPosts({'number': number, 'offset': offset, 'orderby': 'date', 'order':'ASC'}))
		postlist = []
		for wppost in wpposts:
			post = WpPostWrapper(wppost.id, wppost.title, wppost.content)
			postlist.append(post)
		return postlist
	
	def delete_posts_by_id(self, ids):
		for id in ids:
			print 'Deteting post %s...' % id,
			self.wpconn.call(posts.DeletePost(id))
			print 'done'
	
	def delete_posts(self, postlist):
		for p in postlist:
			print 'Deteting post %s [%s]...' % (p.postid, p.title),
			self.wpconn.call(posts.DeletePost(p.postid))
			print 'done'

	def clear_posts(self, maxnum=10000):
		offset = 0
		number = 1
		deleted = 0
		while True:
			postlist = self.get_posts(number, offset)
			postnum = len(postlist)
			if postnum == 0:
				break
			self.delete_posts(postlist)
			deleted = deleted + postnum
			if deleted >= maxnum:
				break
			
	def get_taxonomies(self):
		taxes = self.wpconn.call(taxonomies.GetTaxonomies())
		#for t in taxes:
		#	print '%s' % t.name,
		#print ' gotten'
		return taxes

	def delete_taxonomy(self, taxonomy):
		if taxonomy.name == 'category':
			return
		self.clear_terms(taxonomy.name)
	
	def clear_taxonomies(self):
		taxes = self.get_taxonomies()
		for tax in taxes:
			print 'Deteting taxonomy %s...' % tax.name,
			self.delete_taxonomy(tax)
			print 'done'

	def get_terms(self, taxonomy_name):
		wpterms = self.wpconn.call(taxonomies.GetTerms(taxonomy_name))
		terms = []
		for t in wpterms:
			term = WpTermWrapper(t.id, t.name, taxonomy_name)
			terms.append(term)
		return terms

	def delete_terms(self, terms):
		for t in terms:
			print 'Deteting term %s [%s:%s]...' % (t.termid, t.taxonomy_name, t.name),
			self.wpconn.call(taxonomies.DeleteTerm(t.taxonomy_name, t.termid))
			print 'done'
	
	def clear_terms(self, taxonomy):
		terms = self.get_terms(taxonomy)
		self.delete_terms(terms)
	

if __name__ == '__main__':
	wp = WpWrapper('localhost', 'wahaha', '123456')
	i = 0
	while i < 3:
		post = WpPostWrapper()
		post.set_title('test title' + str(i))
		post.set_content('test content' + str(i))
		post.set_tags('abc, wahaha')
		post.set_categories(['test t1', 'test t2'])
		print wp.new_post(post)
		print post.title
		print post.content
		print post.tags
		print post.categories
		i = i + 1
