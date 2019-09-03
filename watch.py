import requests
import re

class Zhenghun(object):
	url ='http://www.zhenai.com/zhenghun/';
	
	def __int__(self,city):
		self.newurl = Zhenghun.url+city+"/nv"
		
	def getHtml(self):
		return requests.get(self.newurl).content.decode("gbk")

	def prase(self):
		html= self.getHtml()
		rex ="zengze"
		list = re.findall(rex,html)
		return list


def main():
	citylist=['dongcheng','chaoyang1']
	for city in citylist:
		zhenhun = Zhenhun(city)
		list = zhenhun.prase()
		for l in list:
			u = l.split('"')
			n=l[l.rfind('"')+2:list.rfind('<')]
			print(u+'\t'+n)
			

if __name__ == "__main__"			
	main()
	
	
