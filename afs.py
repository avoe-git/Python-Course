import os
import re
import argparse

TEMPLATE = '''"""
Solution for problem #{number} [Generated by avoe's afs.py]

Statement of the problem:
{statement}
"""
'''
STATEMENT_ENTRY_TEMPLATE = '''
## Solution for problem #{number} [Generated by avoe's afs.py]

Statement of the problem:
{statement}

**Filename**: `{filename}`
'''
def get_next_numbered_filename(folder):
    existing = os.listdir(folder)
    numbers = []
    pattern = re.compile(r"solution_(\d+)\.py")

    for f in existing:
        match = pattern.match(f)
        if match:
            numbers.append(int(match.group(1)))

    next_num = max(numbers, default=0) + 1
    return f"solution_{next_num}.py", next_num

def prompt_problem_statement():
    print("📝 Paste the problem statement below. Press ENTER twice to finish:")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines)


def append_to_statements_md(number, filename, statement):
    with open("statements.md", "a", encoding="utf-8") as f:
        f.write(STATEMENT_ENTRY_TEMPLATE.format(
            number=number,
            filename=filename,
            statement=statement.strip()
        ))

def create_solution_file(name, get_problem):
    folder = "solutions"
    os.makedirs(folder, exist_ok=True)

    if name in ("standard", "standart"):
        filename, number = get_next_numbered_filename(folder)
    else:
        if not name.isidentifier():
            print(f"❌ Invalid file name: '{name}' is not a valid Python identifier.")
            return
        filename = f"{name}.py"
        number = name

    filepath = os.path.join(folder, filename)

    if os.path.exists(filepath):
        print(f"⚠️ File '{filepath}' already exists.")
        return

    statement = ""
    if get_problem:
        statement = prompt_problem_statement()

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(number=number, statement=statement))

    if get_problem and isinstance(number, int):
        append_to_statements_md(number, filename, statement)

    print(f"✅ Created: {filepath}")
    if get_problem:
        print(f"📘 Statement added to statements.md")

# CLI ARGUMENT HANDLING
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new solution file")
    parser.add_argument("name", help="The solution name or 'standard'")
    parser.add_argument("-P", "--problem", action="store_true", help="Add problem statement after creation")

    args = parser.parse_args()
    create_solution_file(args.name, args.problem)