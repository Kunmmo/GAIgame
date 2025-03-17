from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class SceneData:
    name: str
    bg_image: str
    time: str
    weather: str

@dataclass
class CharacterLine:
    name: str
    emotion: str
    position: str
    dialogue: str

class SceneParser:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.scene_data: Optional[SceneData] = None
        self.characters: List[CharacterLine] = []

    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith("scene:"):
                    self._parse_scene_line(line)
                elif line.startswith("character:"):
                    self._parse_character_line(line)
                elif line == "end":
                    break

    def _parse_scene_line(self, line: str):
        _, params = line.split(":", 1)
        parts = params.split("|")
        self.scene_data = SceneData(
            name=parts[0].strip(),
            bg_image=parts[1].strip(),
            time=parts[2].strip(),
            weather=parts[3].strip()
        )

    def _parse_character_line(self, line: str):
        _, params = line.split(":", 1)
        parts = params.split("|")
        self.characters.append(CharacterLine(
            name=parts[0].strip(),
            emotion=parts[1].strip(),
            position=parts[2].strip(),
            dialogue=parts[3].strip()
        ))
