from jsonrpc import ServiceProxy

access = ServiceProxy("http://owltest:dgsjkbksbJFg87qAiFBbgf9@50.66.72.155:9332")
print access.getmininginfo()