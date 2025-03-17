from src.file_parser import SceneParser
from src.ui_manager import UIManager
from pathlib import Path

class GameEngine:
    def __init__(self, resource_manager):
        self.resource = resource_manager
        self.current_chapter = 1
        self.current_scene_index = 0  # 当前场景索引
        self.scene_files = []  # 存储场景文件列表
        self.current_scene = None
        self.characters = []
        self.dialogue_text = ""
        self.ui = None

    def load_scene_list(self, chapter: int):
        """加载指定章节的所有场景文件"""
        self.current_chapter = chapter
        chapter_dir = Path(f"game_data/story/chapter_{self.current_chapter}")
        # 按场景编号排序文件
        self.scene_files = sorted(chapter_dir.glob("chapter_*_scene_*.txt"), 
                                key=lambda x: int(x.stem.split("_")[-1]))
        self.current_scene_index = -1  # 初始状态设为-1，首次推进时加载第一个场景

    def load_scene(self, scene_file: str):
        parser = SceneParser(Path(scene_file))
        parser.parse()
        self.current_scene = parser.scene_data
        self.characters = parser.characters
        self.dialogue_text = "\n".join([c.dialogue for c in self.characters])

    def render(self, screen):
        if self.current_scene:
            if not self.ui:
                self.ui = UIManager(screen, self.resource)
            self.ui.draw_background(self.current_scene.bg_image)
            self.ui.draw_characters(self.characters)
            self.ui.draw_dialogue_box(self.dialogue_text)

    def advance_scene(self):
        """推进到下一幕的核心逻辑"""
        if not self.scene_files:
            print("没有可用的场景文件")
            return

        # 首次推进时加载第一个场景
        if self.current_scene_index == -1:
            self.current_scene_index = 0
        else:
            self.current_scene_index += 1

        if self.current_scene_index < len(self.scene_files):
            scene_path = self.scene_files[self.current_scene_index]
            self.load_scene(scene_path)
        else:
            print("已到达章节末尾")
