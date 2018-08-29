sudo apt remove libreoffice-commo
sudo apt remove unity-webapps-common
Win10 IPV4 :172.31.180.198
Linux IPV4 :192.168.137.128
cxitx
<package.deb>
sudo apt install libappindicator1 libindicator7
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt -f install
删除文件夹 rm -r 文件名
打包 tar -cvf 打包文件.tar 被打包的文件/路径...
解包 tar -xvf 打包文件.tar
移动文件 mv 文件名 目标路径
压缩 tar -zcvf 打包文件.tar.gz 被压缩的文件/路径...
解压 tar -zxvf 打包文件.tar.gz
解压到指定路径 tar -zxvf 打包文件.tar.gz -C 目标路径
压缩 tar -jcvf 打包文件.tar.bz2 被压缩的文件/路径...
解压 tar -jxvf 打包文件.tar.bz2
chmod -R 755 文件名|目录名
# -*- coding: utf-8 -*-
sudo tar -zxvf pycharm-edu-2018.1.1.tar.gz -C /opt
/opt/pycharm-edu-2018.1.1/bin$ ./pycharm.sh 
sudo gedit /usr/sh/are/applications/jetbrains-pycharm.desktop
sudo rm -r /opt/pycharm-edu-2018.1.1/
rm -r ~/.pycharm-edu-2018.1/
sudo passwd
su rootcd
/mnt/hgfs/Share/
sudo service network-manager stop  
	sudo rm /var/lib/NetworkManager/NetworkManager.state   
	sudo service network-manager start 
pip install xxx -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

pip install jieba -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

headers = {'User-Agent' : 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',}

写 CSS(CSS 选择器：BeautifulSoup4)时，标签名不加任何修饰，类名前加.，id名前加#
XPath	JSONPath	描述
/			$		根节点
.			@		现行节点
/			.or[]	取子节点
..			n/a		取父节点，Jsonpath未支持
//			..		就是不管位置，选择所有符合条件的条件
*			*		匹配所有元素节点
@			n/a		根据属性访问，Json不支持，因为Json是个Key-value递归结构，不需要。
[]			[]		迭代器标示（可以在里边做简单的迭代操作，如数组下标，根据内容选值等）
|			[,]		支持迭代器中做多选。
[]			?()		支持过滤操作.
n/a			()		支持表达式计算
()			n/a		分组，JsonPath不支持

scrapy startproject mySpider
scrapy genspider filename "allowed_domains"
scrapy genspider -t crawl tencent tencent.com
scrapy shell "url"

from scrapy import cmdline
cmdline.execute('scrapy crawl sunwz'.split())

CRITICAL - 严重错误(critical)
ERROR - 一般错误(regular errors)
WARNING - 警告信息(warning messages)
INFO - 一般信息(informational messages)
DEBUG - 调试信息(debugging messages)

subFilename = parentFilename + '/' + subTitle[j]
				# 如果目录不存在，则创建目录
				if (not os.path.exists(subFilename)):
					os.makedirs(subFilename)

response.xpath('//div[contains(@class, "pagecenter p3")]//strong/text()').extract()[0]

content = json.dumps(dict(item), ensure_ascii=False) + "\n"
self.filename.write(content)

net start MongoDB
net stop MongoDB

MONGODB_HOST = '127.0.0.1'
# 端口号，默认是27017
MONGODB_PORT = 27017
# 设置数据库名称
MONGODB_DBNAME = 'douban'
# 存放本次数据的表名称
MONGODB_DOCNAME = 'movies'

查看当前数据库				db
查看所有数据库				show dbs
连接到xxx数据库				use xxx
查看当前数据库下所有的表	show collections
查看yyy表里的数据			db.yyy.find()
删除当前数据库				db.dropDatabase()

账户密码：	scrapy.FormRequest.from_response
cookies：	scrapy.FormRequest
正则转换cookies:
	find:		\s?(.+?)=(.+?;)
	replace:	"\1":"\2",\n

git pull origin master --allow-unrelated-histories
gitbook-convert -m 1 section.1.html ./
gitbook-convert -m 1 courseware/section.1.html courseware/










































































































