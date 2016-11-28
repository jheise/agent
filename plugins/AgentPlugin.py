class AgentPlugin(object):
	def __init__(self,name,*args,**kwargs):
		self.name = name
		self.status = "not started"
		self.args = args
		self.kwargs = kwargs
		self.result = "not started"

	def perform(self):
		pass

if __name__ == "__main__":
	plugin = AgentPlugin("testplugin","foobar","barbaz",foo="foo",bar="bar",baz="baz")
	print "plugin status is %s" % plugin.status
	plugin.perform()
	print "plugin status is %s" % plugin.status
