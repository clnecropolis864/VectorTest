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
print "Testing dotProduct"

Vector1a = vector.Vector2d(3, 4)
Vector1b = vector.Vector2d(5, 6)
ans = calc.dotProduct(Vector1a, Vector1b)
ct.assert_equals(39, ans)

Vector1a = vector.Vector2d(3, -4)
Vector1b = vector.Vector2d(-5, 6)
ans = calc.dotProduct(Vector1a, Vector1b)
ct.assert_equals(-39, ans)

Vector2a = vector.Vector3d(-3, 4, 5)
Vector2b = vector.Vector3d(5, -6, 7)
ans = calc.dotProduct(Vector2a, Vector2b)
ct.assert_equals(-4, ans)
print "Success"

#TESTING CROSSPRODUCT
print "Testing crossProduct"
ans = calc.crossProduct(Vector2a, Vector2b)
ct.assert_equals(58, ans.xcomponent)
ct.assert_equals(46, ans.ycomponent)
ct.assert_equals(-2, ans.zcomponent)

print "Testing __str__"
print Vector1a
print Vector2a


print "\nTesting complete."