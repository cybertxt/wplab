import argparse
from wprpc_wrapper import WpWrapper

parser = argparse.ArgumentParser()
parser.add_argument('-H', '--host', dest='host', default='localhost', action='store', help='Host name')
parser.add_argument('-u', '--user', dest='user', default='', action='store', help='Username')
parser.add_argument('-p', '--passwd', dest='password', default='', action='store', help='Password')
parser.add_argument('-n', '--number', dest='number', type=int, default=1, action='store', help='Max post to delete')

args = parser.parse_args()
wp = WpWrapper(args.host, args.user, args.password)
wp.clear_posts(args.number)
#wp.clear_taxonomies()
