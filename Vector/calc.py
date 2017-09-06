import vector as v

def dotProduct(v1, v2):
	"""Returns: Dot product of v1 and v2 as type int

	Precondition: v1 and v2 are of type Vector
	and the same type of Vector"""

	assert type(v1) == type(v2)

	if type(v1) == "Vector2d":
		return v1.xcomponent * v2.xcomponent + v1.ycomponent * v2.ycomponent
	elif type(v1) == "Vector3d":
		return v1.xcomponent * v2.xcomponent + v1.ycomponent * v2.ycomponent\
		+ v1.zcomponent * v2.zcomponent
