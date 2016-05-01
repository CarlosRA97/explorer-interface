class ThreadUp(object):
	def __init__(self, f):
		from threading import Thread
		self.Thread = Thread
		self.f = f
		self.f_name = self.f.__name__

	def __call__(self, *args):
		functions = dict()
		functions[self.f_name] = self.f
		self.Thread(target=functions[self.f_name], args=args).start()
