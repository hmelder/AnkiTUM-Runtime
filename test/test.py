import unittest
import subprocess
import os


class TestGenerateCommand(unittest.TestCase):

    def test_generate_command(self):
        # Set the command and arguments
        cmd = ["python", "./../src/ankitum.py", "./resources/test1.yaml", "-o", "out", "--debug"]

        # Run the command as a subprocess
        result = subprocess.run(cmd, universal_newlines=True)
