import os,sys

class PluginLoader:

    plugins = {}

    def __init__(self,folder):
        if not os.path.isdir(folder):
            raise Exception("%s is not a folder" % folder )

        sys.path.append(folder)

	plugins = [plugin for plugin in os.listdir(folder) if plugin.endswith(".py")]
		
	for plugin in plugins:
            self.plugins[plugin[:-3]] = __import__(plugin[:-3])

    def newinstance(self,name,*args,**kwargs):
        print "type args", type(args)
        args = list(args)
        plugin = self.plugins[name]
	create = "plugin.%s(" % name
	argstr = ""
	kwargstr = ""
	while args:
            argstr = "%s'%s'" % (argstr,args.pop(0))
            if args:
                argstr = "%s," % argstr
        tkeys = kwargs.keys()
	while tkeys:
            kwargstr = "%s%s='%s'" % (kwargstr,tkeys[0],kwargs[tkeys.pop(0)])
            if tkeys:
                kwargstr = "%s," % kwargstr
        if argstr:
            create = "%s%s" % (create,argstr)
            if kwargstr:
                create = "%s," % create
	if kwargstr:
            create = "%s%s" % (create,kwargstr)
        create = "%s)" % create
        print create
        return eval(create)


if __name__ == "__main__":
	plugins = PluginLoader("plugins")
	print "testing with only *args\n"
	testplugin = plugins.newinstance("ServatorTestPlugin","foobar","foo","bar")
	testplugin.perform()
	print "\ntesting with only **kwargs\n"
	testplugin = plugins.newinstance("ServatorTestPlugin","foobar",foobar="foobar",barbaz="barbaz")
	testplugin.perform()
	print "\ntesting with *args and **kwargs\n"
	testplugin = plugins.newinstance("ServatorTestPlugin","foobar","foo","bar",foobar="foobar",barbaz="barbaz")
	testplugin.perform()
