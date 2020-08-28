import os
import time
from classes_objects import Vocabulary

print(os.getcwd())
print(time.strftime('%X %x'))
vc_hello = Vocabulary('Hello', '你好', 20)
vc_hello.up()
print(str(vc_hello) + ": " + str(vc_hello.prof))