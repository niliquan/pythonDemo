#coding=utf-8
import urllib,sys
from BeautifulSoup import BeautifulSoup

reload(sys)
sys.setdefaultencoding("gb2312")

httpq = ['http://zhidao.baidu.com/question/189027634.html']

def iskey(sttr):
	keys = ['动漫',"导演","演员","贺岁剧","剧情","剧情",'恐怖']
	for key in keys:
		if sttr.find(key) != -1:
			return 0
		return -1

def getContent(http):
	html_src=urllib.urlopen(http).read()
	parser=BeautifulSoup(html_src.decode("gb2312","ignore"))
	question=parser.find("span","question-title")
	answer=parser.find("pre",attrs={"id":"best-answer-content"})
	if answer is None:
		no = -1
	else:
		#把记录写入文本中
		with file('page.txt','a') as f:
			f.write("Q:%s\n"% question.contents[0])
			f.write("A:%s\n"% answer.contents[0])
	
	base= "http://zhidao.baidu.com"
	urls=parser.findAll("a",attrs={'log':'relative.title.click'})
	for url in urls:
		strs= url.contents[0].encode("utf-8")
		print strs
		if (iskey(strs)!=-1):
			newHttp=base+url['href']
			httpq.append(newHttp)
def main():
	 while len(httpq) != 0:
		 getContent(httpq.pop(0))

if __name__=="__main__":
	 main()




