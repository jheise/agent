from threading import Thread
from threading import Semaphore
from time import sleep

class Agent(Thread):

	def __init__(self,name):
		Thread.__init__(self)
		self.name = name
		self.running = True
		self.state = "run"
		self.lock = Semaphore(0)
		self.counter = 0
		self.jobs = []
		self.results = []
		self.continuum = None

	def set_continuum(self,continuum):
		self.continuum = continuum

	def new_job(self,plugin,*args,**kwargs):
		self.jobs.append( self.continuum.plugins.newinstance(plugin,*args,**kwargs))

	def function(self):
		print "checking list of jobs"
		if self.jobs:
			print "jobs found, running first one"
			job =  self.jobs.pop(0)
			job.perform()
			self.results.append(job.getResult())
		print "checking for results"
		if self.results:
			while self.results:
				print self.results.pop(0)

		print "function complete"

	def status(self):
		pass
	
	def pause(self):
		self.state = "pause"

	def unpause(self):
		self.lock.release()

	def run(self):
		print "%s is running" % self.name
		while self.running:
			if self.state == "run":
				self.function()
				sleep(1)
			elif self.state == "pause":
				print "%s locking on semaphore to halt" % self.name
				self.lock.acquire()
				print "%s lock released, reseting state to run" % self.name
				self.state = "run"
			print "done sleeping"
		print "this should never be seen"

	def stop(self):
		self.running = False

	def join(self):
		self.counter += 1

        @property
	def is_active(self):
		return self.state == "run"


if __name__ == "__main__":
	print "performaing self test"
	cortana = Agent("cortana")
	cortana.start()
	#cortana.newJob("foobar","foo","bar",foo="bar",bar="foo")
	sleep(5)
	cortana.pause()
	sleep(10)
	cortana.unpause()
	cortana.stop()
