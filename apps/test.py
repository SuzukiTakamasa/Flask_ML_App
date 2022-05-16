from pathlib import Path
import os

print(Path(os.path.basename(__file__)).parent.parent)