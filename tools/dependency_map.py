from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parent.parent

FOLDERS = [
    "core",
    "agents",
    "plugins",
    "dashboard"
]

OUTPUT = ROOT / "docs" / "ENGINEERING_HANDBOOK" / "21_Dependency_Map.md"


def get_imports(file_path):
    tree = ast.parse(file_path.read_text(encoding="utf-8"))
    imports = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)

    return sorted(set(imports))


def build():

    report = "# Dependency Map\n\n"

    for folder in FOLDERS:

        path = ROOT / folder

        if not path.exists():
            continue

        for file in sorted(path.rglob("*.py")):

            report += f"## {file.relative_to(ROOT)}\n\n"

            try:

                imports = get_imports(file)

                if imports:

                    for module in imports:
                        report += f"- {module}\n"

                else:

                    report += "- No imports\n"

                report += "\n"

            except Exception as e:

                report += f"Error: {e}\n\n"

    OUTPUT.write_text(report, encoding="utf-8")

    print("Created:", OUTPUT)


if __name__ == "__main__":
    build()