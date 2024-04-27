# private function, variable are not available for import all by (*)

from my_module import *

public_function()

'''
NameError: name '_private_function' is not defined
_private_function()
'''

object1 = PublicClass()

object1.public_method()

'''
AttributeError: 'PublicClass' object has no attribute '_private_function'
object1._private_function()
'''