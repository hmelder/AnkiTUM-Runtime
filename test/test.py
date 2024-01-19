import unittest

from click.testing import CliRunner

from ankitum.ankitum import generate


class TestGenerateCommand(unittest.TestCase):

    def test_bigtest(self):
        args = ["./test_yamls/big_test.yaml", "-o", "./out/out.apkg", "-r", "./images", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        print(result.stdout)

        self.assertEqual(result.exit_code, 0)

    def test_nested(self):
        args = ["./test_yamls/Nested_Test", "-o", "./out/out.apkg", "-r", "./images", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        print(result.stdout)

        self.assertEqual(result.exit_code, 0)

    def test_generate_markdown(self):
        args = ["./test_yamls/test_md.yaml", "-o", "./out/out.apkg", "-r", "./images", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        print(result.stdout)

        self.assertEqual(result.exit_code, 0)

    def test_generate_markdown_2(self):
        args = ["./test_yamls/test_md_2.yaml", "-o", "./out/out.apkg", "-r", "./images", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        print(result.stdout)

        self.assertEqual(result.exit_code, 0)

    def test_generate_markdown_3(self):
        args = ["./test_yamls/test_md_3.yaml", "-o", "./out/out.apkg", "-r", "./images", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        print(result.stdout)

        self.assertEqual(result.exit_code, 0)

    def test_generate_1(self):
        args = ["./test_yamls/test1.yaml", "-o", "./out/out.apkg", "-r", "./images", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        print(result.stdout)

        self.assertEqual(result.exit_code, 0)

    def test_generate_2(self):
        args = ["./test_yamls/test1.yaml", "-o", "./out/out.apkg", "-r", "./images", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 0)

    def test_generate_3(self):
        args = ["./test_yamls/test1.yaml", "-o", "./out/out.apkg", "-r", "./images", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 0)

    def test_invalid_1(self):
        args = ["./test_yamls/invalid1.yaml", "-o", "./out/out.apkg", "-r", "./images", "--debug"]

        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 1)

    def test_invalid_2(self):
        args = ["./test_yamls/invalid2.yaml", "-o", "./out/out.apkg", "-r", "./images", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 1)

    def test_invalid_3(self):
        args = ["./test_yamls/invalid3.yaml", "-o", "./out/out.apkg", "-r", "./images", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 1)

    def test_invalid_4(self):
        args = ["./test_yamls/invalid4.yaml", "-o", "./out/out.apkg", "-r", "./images", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 1)

    def test_invalid_5(self):
        args = ["./test_yamls/invalid5.yaml", "-o", "./out/out.apkg", "-r", "./images", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 1)

    def test_invalid_6(self):
        args = ["./test_yamls/invalid6.yaml", "-o", "./out/out.apkg", "-r", "./images", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 1)

    def test_invalid_7(self):
        args = ["./test_yamls/invalid7.yaml", "-o", "./out/out.apkg", "-r", "./images", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 1)

    def test_invalid_8(self):
        args = ["./test_yamls/invalid8.yaml", "-o", "./out/out.apkg", "-r", "./images", "--debug"]
        runner = CliRunner()
        result = runner.invoke(generate, args)
        self.assertEqual(result.exit_code, 1)
        