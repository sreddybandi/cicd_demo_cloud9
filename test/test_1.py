''' File doc string -> Tells us the purpose of the file
 addtion of two numbers
 '''

import os
import sys

from script import addition

sys.path.insert(0, os.getcwd())


def test_add():
    ''' addition of two numbers
    '''
    subj = addition(7, 9)
    print(subj)
    assert subj == 16


test_add()
