import unittest

def ball(blood, sugar):
    if blood <= 120 and sugar < 100:
        return 'General'
    elif 120 <= blood <= 138 and 100 <= sugar <= 125:
        return 'Risk'
    elif blood > 138 or sugar > 125:
        blood_level = (
            1 if 140 <= blood <= 159 else
            2 if 160 <= blood <= 179 else
            3 if blood >= 180 else
            0 # Default
        )
        sugar_level = (
            1 if 125 <= sugar <= 154 else
            2 if 155 <= sugar <= 182 else
            3 if sugar >= 183 else
            0 # Default
        )
        return f'High Risk (Blood Level {blood_level}, Sugar Level {sugar_level})'

class TestPingPong(unittest.TestCase):
    def test_general(self):
        self.assertEqual(ball(100, 96), 'General')
    
    def test_risk(self):
        self.assertEqual(ball(130, 110), 'Risk')
    
    def test_high_risk_level_1(self):
        self.assertEqual(ball(150, 130), 'High Risk (Blood Level 1, Sugar Level 1)')
    
    def test_high_risk_level_2(self):
        self.assertEqual(ball(170, 160), 'High Risk (Blood Level 2, Sugar Level 2)')
    
    def test_high_risk_level_3(self):
        self.assertEqual(ball(190, 188), 'High Risk (Blood Level 3, Sugar Level 3)')

if __name__ == "__main__":
    unittest.main()
