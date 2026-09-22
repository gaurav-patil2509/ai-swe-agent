from dataclasses import dataclass

#@dataclass python object for carrying the structured data 
@dataclass 
class CodeChunk:
    content: str
    file_path: str
    start_line: int
    end_line: int
