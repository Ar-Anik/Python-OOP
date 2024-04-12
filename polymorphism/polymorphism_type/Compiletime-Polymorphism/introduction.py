# compile-time ----> overloading

''' Compile-time polymorphism, also known as static polymorphism or early binding, refers to a mechanism in programming languages where the decision about
 which method or function to call is made by the compiler at compile time rather than at runtime. This decision is based on the types of the objects involved
 in the function call. '''

''' In languages that support compile-time polymorphism, such as C++ with function overloading and templates, or Java with method overloading,
 the compiler determines which version of a function or method to call based on the static types of the arguments or objects involved.
 This determination is made at compile time because the types are known and fixed at that point. '''

''' Compile-time polymorphism offers performance benefits because the method resolution is done at compile time, eliminating the need for runtime type checks or
 dynamic dispatch mechanisms. However, it comes with the limitation that the decision about which method to call cannot change at runtime based on the actual 
 types of objects, as opposed to runtime polymorphism (dynamic polymorphism), which allows for this flexibility. '''

''' In summary, compile-time polymorphism allows the compiler to choose the appropriate method or function based on the static types of the objects involved,
 leading to efficient code execution but limited flexibility compared to runtime polymorphism. '''

#️⃣#️⃣#️⃣ Another Way

''' Compile-time polymorphism is like having a menu at a restaurant where each dish has a specific name and description. When you order, 
you know exactly what you're getting because the menu is fixed and clear. '''

''' In programming, when you use compile-time polymorphism, the compiler knows exactly which version of a function or method to use based on the 
types of the inputs you provide. It's like the compiler looks at a menu (the function definitions) and decides which "dish" (function implementation) 
to serve based on what you ordered (the types of the inputs). '''

''' This decision is made before the program runs, during the compilation process, hence the term "compile-time."
 It's efficient because everything is decided beforehand, just like knowing your meal before it's cooked.
 But, like ordering from a menu, you can't change your mind about what you want to eat (or which function to use) once the order (or code) is placed. '''

''' So, compile-time polymorphism is about the compiler figuring out which function or method to use based on the types of the inputs you provide,
 before the program starts running. '''