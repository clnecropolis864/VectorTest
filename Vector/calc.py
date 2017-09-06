import vector

def dotProduct(v1, v2):
	"""Returns: Dot product of v1 and v2 as type int

	Precondition: v1 and v2 are of type Vector
	and the same type of Vector"""

	assert v1.getType() == v2.getType()

	if v1.getType() == "Vector2d":
		return v1.xcomponent * v2.xcomponent + v1.ycomponent * v2.ycomponent
	elif v1.getType() == "Vector3d":
		return v1.xcomponent * v2.xcomponent + v1.ycomponent * v2.ycomponent\
		+ v1.zcomponent * v2.zcomponent

def crossProduct(v1, v2):
	"""Returns: Cross product of v1 and v2 as type
	Vector3d

	Precondition: v1 and v2 are of type Vector3d"""
	assert v1.getType() == "Vector3d"
	assert v2.getType() == "Vector3d"

	x = v1.ycomponent * v2.zcomponent - v1.zcomponent * v2.ycomponent
	y = -(v1.xcomponent * v2.zcomponent - v1.zcomponent * v2.xcomponent)
	z = v1.xcomponent * v2.ycomponent - v1.ycomponent * v2.xcomponent

	return vector.Vector3d(x, y, z)