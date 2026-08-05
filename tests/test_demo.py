from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = sorted((ROOT / "examples").rglob("*.py"))


class DemoRepositoryTests(unittest.TestCase):
    def test_contains_python_examples(self) -> None:
        self.assertTrue(EXAMPLES, "At least one runnable Python example is required")

    def test_examples_compile(self) -> None:
        for path in EXAMPLES:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")

    def test_examples_use_capsolver_agent(self) -> None:
        source = "\n".join(path.read_text(encoding="utf-8") for path in EXAMPLES)
        self.assertIn("capsolver_agent", source)

    def test_repository_is_not_a_distribution_package(self) -> None:
        self.assertFalse((ROOT / "pyproject.toml").exists())
        self.assertFalse((ROOT / "setup.py").exists())
        self.assertFalse((ROOT / ".github" / "workflows" / "publish.yml").exists())


if __name__ == "__main__":
    unittest.main()
