import unittest

from click.testing import CliRunner

from src.ankitum.ankitum import generate


class TestGenerateCommand(unittest.TestCase):

    def test_gbstest(self):
        args = ["./resources/gbstest.yaml", "-o", "./out/out.apkg", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 0)

    def test_generate_1(self):
        args = ["./resources/test1.yaml", "-o", "./out/out.apkg", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 0)

    def test_generate_2(self):
        args = ["./resources/test1.yaml", "-o", "./out/out.apkg", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 0)

    def test_generate_3(self):
        args = ["./resources/test1.yaml", "-o", "./out/out.apkg", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 0)

    def test_invalid_1(self):
        args = ["./resources/invalid1.yaml", "-o", "./out/out.apkg", "--debug"]

        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 1)

    def test_invalid_2(self):
        args = ["./resources/invalid2.yaml", "-o", "./out/out.apkg", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 1)

    def test_invalid_3(self):
        args = ["./resources/invalid3.yaml", "-o", "./out/out.apkg", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 1)

    def test_invalid_4(self):
        args = ["./resources/invalid4.yaml", "-o", "./out/out.apkg", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 1)

    def test_invalid_5(self):
        args = ["./resources/invalid5.yaml", "-o", "./out/out.apkg", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 1)

    def test_invalid_6(self):
        args = ["./resources/invalid6.yaml", "-o", "./out/out.apkg", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 1)

    def test_invalid_7(self):
        args = ["./resources/invalid7.yaml", "-o", "./out/out.apkg", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 1)

    def test_invalid_8(self):
        args = ["./resources/invalid8.yaml", "-o", "./out/out.apkg", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 1)
        