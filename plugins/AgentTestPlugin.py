from AgentPlugin import AgentPlugin
class AgentTestPlugin(AgentPlugin):
	def __init__(self,name,*args,**kwargs):
            AgentPlugin.__init__(self,name,*args,**kwargs)

	def perform(self):
            for arg in self.args:
                print "arg is %s" % arg
            for key in self.kwargs.keys():
                print "kwarg is %s" % self.kwargs[key]

            self.status = "complete"
            self.result = "ran through all args and kwargs"

if __name__ == "__main__":
	job = AgentTestPlugin("testjob","foobar","barbaz",foo="foo",bar="bar",baz="baz")
	print "job status is %s" % job.getStatus()
	job.perform()
	print "job status is %s" % job.getStatus()
