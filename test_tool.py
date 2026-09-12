import unittest
from tool import check,parse
class EnvTests(unittest.TestCase):
 def test_parse_policy(self):
  values,dupes=parse('A=1\nB=\nA=2');self.assertEqual(values['A'],'2');self.assertEqual(dupes,['A']);self.assertEqual(check('A=\nX=1',['A','B'],['X'])['missing'],['B'])
if __name__=='__main__':unittest.main()
