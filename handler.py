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
		#results = xmlData[7]
		#print(results.tag)
		#print(results.attrib)
		"""for childA in xmlData:
			print(xmlData.tag +"->"+childA.tag)
			print(childA.attrib)
			dictData.update(childA.attrib)
			for childB in childA:
				print(xmlData.tag +"->"+childA.tag+"->"+childB.tag)
				print(childB.attrib)
				dictData.update(childB.attrib)
				for childC in childB:
					print(xmlData.tag +"->"+childA.tag+"->"+childB.tag+"->"+childC.tag)
					print(childC.attrib)
					dictData.update(childC.attrib)"""
		
		return dictData
	except URLError as e:
		raise URLError("arXiv fetch command encountered URLError:"+repr(e))

def concatAttribs(xmlTree):
	xmlDict = {}
	try:
		
		#print(xmlTree.tag)
		#print(xmlTree.keys())
		#print(xmlTree.text);
		#print(xmlTree.tail);
		#print(xmlTree.attrib)
		startInd = xmlTree.tag.index("}")
		tag = xmlTree.tag[startInd+1:];	
		if xmlTree.text != "":
			xmlDict[tag] = xmlTree.text
		"""if xmlTree.getchildren() != {}:
			childDict = {};"""
		for child in xmlTree:
			xmlDict.update(concatAttribs(child))
			#xmlDict[tag] = childDict;
			
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