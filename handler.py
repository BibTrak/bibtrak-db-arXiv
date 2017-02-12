from urllib2 import Request, urlopen, URLError
import xml.etree.ElementTree


def fetch(id):
	url = "http://export.arxiv.org/api/query?id_list="+id+"&&start=0&&max_results=1";
	request = Request(url);
	try:
		response = urlopen(request);
		paperData = response.read();
		#Turn string into xml.
		xmlData = xml.etree.ElementTree.fromstring(paperData);
		#Turn xml into dict
		dictData = concatAttribs(xmlData);
		
		return dictData
	except URLError as e:
		raise URLError("arXiv fetch command encountered URLError:"+repr(e))

def concatAttribs(xmlTree):
	xmlDict = {}
	try:
		startInd = xmlTree.tag.index("}")
		tag = xmlTree.tag[startInd+1:];	
		if xmlTree.text is not None and len(xmlTree.text) > 0:
			xmlDict[tag] = xmlTree.text
		children = xmlTree.getchildren();
		if children is not None and len(children) > 0:
			childDict = {}
			for child in xmlTree:
				childDict.update(concatAttribs(child))
			xmlDict[tag] = childDict
			
		return xmlDict
	except ValueError as e:
		print "ValueError:",e
		return {}

def main(*args):
	print(fetch(args[0]))

	return 0
		
if __name__ == "__main__":
	import sys
	raw_args = sys.argv[1:]
	sys.exit(main(*raw_args))