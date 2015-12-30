
if [ $# -ne 2 ]; then
	echo "Usage: $0 <username> <password>"
	exit 1
fi

pushd top_baidu_com
rm top.json
scrapy crawl TopBaiduCom -o top.json
mv top.json ../search_baidu_com/
popd

pushd search_baidu_com
rm ../result.json
scrapy crawl SearchBaiduCom -o ../result.json
popd

pushd tools
python wprpc_new_posts_from_json.py -u $1 -p $2 -f ../result.json
popd
