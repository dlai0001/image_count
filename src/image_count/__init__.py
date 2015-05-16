"""
Depedencies used by image_count module.

Dependencies are defined as lambas
"""

from dummy import return_bob

class Dependencies(object):

	def dummy_factory(self):
		return return_bob



"""
Singleton global instance of dependencies module.
"""
_dependencies = Dependencies()