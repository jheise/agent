#!/usr/bin/env python
from Agent import Agent
from time import sleep
from PluginLoader import PluginLoader

class Continuum(object):
    def __init__(self):
           print "Continuum Online"
           self.running = True
           self.agents = []
           self.plugins = PluginLoader("./plugins")
           print "PluginLoader active with %s plugins" % self.plugins.plugins

    def stop(self):
        self.running = False

    def main(self):
        print "entering main processing loop"
        while self.running:
            try:
                sleep(1)
            except KeyboardInterrupt:
                print "pausing agents"
                for x in self.agents:
                    x.pause()
                sleep(10)
                for x in self.agents:
                    x.unpause()
        print "Continuum no longer running"

    def create_agent(self,name):
        print "creating agent %s" % name
        agent = Agent(name)
        agent.set_continuum(self)
        agent.start()
        self.agents.append(agent)




if __name__ == "__main__":
    continuum = Continuum()
    continuum.create_agent("cortana")
    continuum.create_agent("wintermute")
    continuum.create_agent("neuromancer")
    continuum.agents[0].new_job("AgentTestPlugin","foo","bar","baz",foobar="foobar",barbaz="barbaz")
    continuum.main()

