'''
MIT License

Name cs225sp20_env Python Package
URL https://github.com/Xiwei-Wang/cs225sp20_env

Version 1.0
Creation Date 26 April 2020

Copyright(c) 2020 Instructors, TAs and Some Students of UIUC CS 225 SP20 ZJUI Course
Instructorts: Prof. Dr. Klaus-Dieter Schewe
TAs: Tingou Liang, Run Zhang, Enyi Jiang, Xiang Li
Group 1 Students: Shen Zheng, Haozhe Chen, Ruiqi Li, Xiwei Wang
Other Students: Zhongbo Zhu

Above all, due to academic integrity, students who will take UIUC CS 225 ZJUI Course
taught with Python later than Spring 2020 semester are NOT authorized with the access
to this package.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files(the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
---------
File cs225sp20_env/demo.py
Version 1.1
'''
# %%
import sys
sys.path.append(__file__[:-len("cs225sp20_env/demo.py")])

print("loading basic modules, classes and methods given in class......")
from cs225sp20_env import *

# if False:
if True:
    print([class_ for class_ in locals()])
print("loading success")

# %%
# __str__ and __repr__ of PyList
print()
list1=PyList([1,2,3,4])
print(list1)
print(repr(list1))
list2=eval(repr(list1))
print(type(list2))
print(list2)