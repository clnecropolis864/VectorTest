class Vector(object):
	"""NO INSTANCE; Abstract parent class"""

class Vector2d(Vector):
	"""Instance is a vector x, y
    
    INSTANCE ATTRIBUTES:
        xcomponent  [int]
        ycomponent	[int]
    """
	def __init__(self, x, y):
		self.xcomponent = x
		self.ycomponent = y

	def getType(self):
		return "Vector2d"

class Vector3d(Vector):
	"""Instance is a vector x, y, z
    
    INSTANCE ATTRIBUTES:
        xcomponent  [int]
        ycomponent	[int]
        zcomponent	[int]
    """
	def __init__(self, x, y, z):
		self.xcomponent = x
		self.ycomponent = y
		self.zcomponent = z

	def getType(self):
		return "Vector3d"



