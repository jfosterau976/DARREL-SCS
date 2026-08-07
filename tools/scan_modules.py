from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parent.parent

FOLDERS = [
    "core",
    "agents",
    "plugins",
    "dashboard"
]

OUTPUT = ROOT / "docs" / "ENGINEERING_HANDBOOK" / "20_Module_Reference.md"


def scan_python_file(file_path):

    tree = ast.parse(file_path.read_text(encoding="utf-8"))

    classes = []
    functions = []
    imports = []

    for node in ast.walk(tree):

        if isinstance(node, ast.ClassDef):
            classes.append(node.name)

        elif isinstance(node, ast.FunctionDef):
            functions.append(node.name)

        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)

        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            imports.append(module)

    return classes, functions, imports


def build():

    report = "# Module Reference\n\n"

    for folder in FOLDERS:

        path = ROOT / folder

        if not path.exists():
            continue

        for file in sorted(path.rglob("*.py")):

            report += f"## {file.relative_to(ROOT)}\n\n"

            try:

                classes, functions, imports = scan_python_file(file)

                report += "### Classes\n"

                if classes:
                    for c in classes:
                        report += f"- {c}\n"
                else:
                    report += "- None\n"

                report += "\n### Functions\n"

                if functions:
                    for f in functions:
                        report += f"- {f}\n"
                else:
                    report += "- None\n"

                report += "\n### Imports\n"

                if imports:
                    for i in sorted(set(imports)):
                        report += f"- {i}\n"
                else:
                    report += "- None\n"

                report += "\n---\n\n"

            except Exception as e:

                report += f"Error reading file: {e}\n\n"

    OUTPUT.write_text(report, encoding="utf-8")

    print("Created:", OUTPUT)


if __name__ == "__main__":
    build()