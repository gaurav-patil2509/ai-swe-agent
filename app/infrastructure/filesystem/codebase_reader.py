from pathlib import Path

class LocalCodeRepository:

    IGNORED_DIRECTORIES = { ".git", ".venv", "__pycache__", ".pytest_cache", "node_modules", ".idea", ".vscode", }
    ALLOWED_EXTENSIONS = { ".py", ".java", ".js", ".ts", ".jsx", ".tsx", ".cpp", ".c", ".h", ".hpp", ".cs", ".go", ".rs", ".php", ".html", ".css", ".sql", ".xml", ".json", ".yaml", ".yml", ".md", }

    def __init__(self, root_path:str):
        self.root_path = Path(root_path)
    

    def list_files(self)->list[str]:
        files=[]

        for path in self.root_path.rglob("*"):
            if not path.is_file():
                continue

            if any(
                directory in self.IGNORED_DIRECTORIES
                for directory in path.parts
            ):
                continue

            if path.suffix.lower() not in self.ALLOWED_EXTENSIONS:
                continue

            files.append(
                str(path.relative_to(self.root_path))
            )

        return files

    def read_files(self, path:str)-> str:
        file_path = (self.root_path / path).resolve() #turns into an actual absolute path 
        root_path = self.root_path.resolve() 
        if not file_path.is_relative_to(root_path): 
             raise ValueError(f"Access outside repository is not allowed: {path}")

        if not file_path.exists():
            raise FileNotFoundError(f"file not found: {path}")

        if not file_path.is_file():
            raise ValueError(f"Path is not a file: {path}")

        try:
            return file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            raise ValueError(
                f"File is not valid utf-8 text: {path}"
            ) from exc