import unittest
import subprocess
import os


class TestGenerateCommand(unittest.TestCase):

    def test_generate_1(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/test1.yaml", "-o", "out", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEquals(result.returncode, 0)

    def test_generate_1(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/test1.yaml", "-o", "out", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEquals(result.returncode, 0)

    def test_generate_2(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/test1.yaml", "-o", "out", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEquals(result.returncode, 0)

    def test_generate_3(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/test1.yaml", "-o", "out", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEquals(result.returncode, 0)

    def test_invalid_1(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/invalid1.yaml", "-o", "out", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEquals(result.returncode, 1)

    def test_invalid_2(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/invalid2.yaml", "-o", "out", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEquals(result.returncode, 1)


    def test_invalid_3(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/invalid3.yaml", "-o", "out", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEquals(result.returncode, 1)

    def test_invalid_4(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/invalid4.yaml", "-o", "out", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEquals(result.returncode, 1)