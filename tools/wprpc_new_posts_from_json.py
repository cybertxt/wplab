import argparse
from wprpc_wrapper import WpWrapper
from wprpc_wrapper import WpPostWrapper

parser = argparse.ArgumentParser()
parser.add_argument('-H', '--host', dest='host', default='localhost', action='store', help='Host name')
parser.add_argument('-u', '--user', dest='user', default='', action='store', help='Username')
parser.add_argument('-p', '--passwd', dest='password', default='', action='store', help='Password')
parser.add_argument('-f', '--file', dest='file', action='store', help='Json file path')

args = parser.parse_args()
wp = WpWrapper(args.host, args.user, args.password)
wp.post_from_json_file(args.file)
