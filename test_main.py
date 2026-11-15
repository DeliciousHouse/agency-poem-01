"""Tests for main.py poem generation."""

import os
import tempfile
import unittest

from main import POEM, main


class TestPoem(unittest.TestCase):
    def test_output_is_deterministic(self):
        with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
            os.environ["MAKEFUN_OUTPUT_DIR"] = d1
            main()
            with open(os.path.join(d1, "entry.txt"), "rb") as f:
                first = f.read()

            os.environ["MAKEFUN_OUTPUT_DIR"] = d2
            main()
            with open(os.path.join(d2, "entry.txt"), "rb") as f:
                second = f.read()

            self.assertEqual(first, second)

    def test_output_is_utf8(self):
        with tempfile.TemporaryDirectory() as d:
            os.environ["MAKEFUN_OUTPUT_DIR"] = d
            main()
            with open(os.path.join(d, "entry.txt"), "rb") as f:
                raw = f.read()
            raw.decode("utf-8")

    def test_length_in_range(self):
        codepoints = len(POEM)
        self.assertGreaterEqual(codepoints, 1)
        self.assertLessEqual(codepoints, 1000)

    def test_has_non_whitespace(self):
        self.assertTrue(POEM.strip())


if __name__ == "__main__":
    unittest.main()
