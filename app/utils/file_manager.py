from pathlib import Path
class ReportWriter:
    def __init__(self,path): self.path=Path(path); self.file=None
    def __enter__(self): self.path.parent.mkdir(parents=True,exist_ok=True); self.file=self.path.open("w",encoding="utf-8"); return self.file
    def __exit__(self,exc_type,exc,tb):
        if self.file and not self.file.closed: self.file.close()
        return False
