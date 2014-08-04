import unittest
# import commands
import subprocess
import os

class Filter(unittest.TestCase):

    def test_like(self):
        # result = commands.getoutput("cat /tmp/_filter.test.log | filter like '.3.5' ")
        like_process = subprocess.Popen("cat /tmp/_filter.test.log | filter like '.3.5'", stdout=subprocess.PIPE, shell=True)
        output,_ = like_process.communicate()
        self.assertEqual(output.strip(),"2345")

    def test_in(self):
        in_process = subprocess.Popen("cat /tmp/_filter.test.log | filter in /tmp/_filter.test.log", stdout=subprocess.PIPE, shell=True)
        output,_ = in_process.communicate()
        self.assertEqual(output.strip(),self.text)

    def setUp(self):
        self.text = '''\
12345
2345
345\
'''
        with open("/tmp/_filter.test.log","w") as file:
            file.write(self.text)


    def tearDown(self):
        os.remove("/tmp/_filter.test.log")

if __name__ == '__main__':
    unittest.main()
