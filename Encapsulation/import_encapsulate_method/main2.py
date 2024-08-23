

# private function, variable are not available for import all by (*)

from my_module import *

public_function()

'''
NameError: name '_protected_function' is not defined
_protected_function()
'''

'''
NameError: name '__private_function' is not defined
__private_function()
'''

# _protected_function()
# __private_function()

object1 = PublicClass()

object1.public_method()
object1._protected_method()
object1.__private_method()

'''
object1.__private_method()
AttributeError: 'PublicClass' object has no attribute '__private_method'. Did you mean: '_protected_method'?
'''
