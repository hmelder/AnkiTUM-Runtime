import unittest
import subprocess
import os


class TestGenerateCommand(unittest.TestCase):

    def test_generate_1(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/test1.yaml", "-o", "./out/out.apkg", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEqual(result.returncode, 0)

    def test_generate_1(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/test1.yaml", "-o", "./out/out.apkg", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEqual(result.returncode, 0)

    def test_generate_2(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/test1.yaml", "-o", "./out/out.apkg", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEqual(result.returncode, 0)

    def test_generate_3(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/test1.yaml", "-o", "./out/out.apkg", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEqual(result.returncode, 0)

    def test_invalid_1(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/invalid1.yaml", "-o", "./out/out.apkg", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEqual(result.returncode, 1)

    def test_invalid_2(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/invalid2.yaml", "-o", "./out/out.apkg", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEqual(result.returncode, 1)

    def test_invalid_3(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/invalid3.yaml", "-o", "./out/out.apkg", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEqual(result.returncode, 1)

    def test_invalid_4(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/invalid4.yaml", "-o", "./out/out.apkg", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEqual(result.returncode, 1)

    def test_invalid_5(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/invalid5.yaml", "-o", "./out/out.apkg", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEqual(result.returncode, 1)

    def test_invalid_6(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/invalid6.yaml", "-o", "./out/out.apkg", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEqual(result.returncode, 1)

    def test_invalid_7(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/invalid7.yaml", "-o", "./out/out.apkg", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEqual(result.returncode, 1)

    def test_invalid_8(self):
        cmd = ["python", "./../src/ankitum.py", "./resources/invalid8.yaml", "-o", "./out/out.apkg", "--debug"]
        result = subprocess.run(cmd, universal_newlines=True)
        self.assertEqual(result.returncode, 1)
        