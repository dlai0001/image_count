from image_count import _dependencies

class Example(object): 

	def __init__(self, dummy_factory=_dependencies.dummy_factory()):
		self._dummy_factory = dummy_factory
		return


	def do_this(self):		
		return self._dummy_factory()
