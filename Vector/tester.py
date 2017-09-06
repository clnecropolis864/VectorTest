import vector
import calc
import cornelltest as ct

#TESTING INITIALIZATIONS

print "Testing initialization of..."
print "\tA 2D vector"
Vector1 = vector.Vector2d(3, 4)
print type(Vector1)
print "Success"
print "Testing components"
ct.assert_equals(3, Vector1.xcomponent)
ct.assert_equals(4, Vector1.ycomponent)
print "Success"

print "\tA 3D Vector"
Vector2 = vector.Vector3d(3, 4, 5)
print type(Vector2)
print "Success"
print "Testing components"
ct.assert_equals(3, Vector2.xcomponent)
ct.assert_equals(4, Vector2.ycomponent)
ct.assert_equals(5, Vector2.zcomponent)
print "Success"

#TESTING DOTPRODUCT

