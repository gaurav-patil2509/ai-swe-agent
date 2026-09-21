from app.infrastructure.filesystem.codebase_reader import LocalCodeRepository

repository = LocalCodeRepository("app")

files = repository.list_file()

print("files found:")
for file in files:
    print(file)

print("\n---Reading app/main.py----")
content = repository.read_files("main.py")

print(content)