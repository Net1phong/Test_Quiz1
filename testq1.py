from q1 import *

def test01():
    assert ball(100,96) == 'General'

def test02():
    assert ball(130,110) == 'Risk'

def test03():
    assert ball(150,130) == 'Hight Risk Level 1'

def test04():
    assert ball(170,160) == 'Hight Risk Level 2'

def test05():
    assert ball(190,188) == 'Hight Risk Level 3'