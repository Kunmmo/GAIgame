import pygame
import logging
from pathlib import Path
from typing import Dict, Optional
from config.settings import Config

class ResourceManager:
    def __init__(self):
        self.backgrounds: Dict[str, pygame.Surface] = {}
        self.characters: Dict[str, Dict[str, pygame.Surface]] = {}
        self.font: Optional[pygame.font.Font] = None
        self._load_resources()

    def _load_resources(self):
        # 加载默认字体
        try:
            self.font = pygame.font.Font(str(Config.FONT_PATH), Config.FONT_SIZE)
        except FileNotFoundError:
            logging.error("Font file not found, using system font")
            self.font = pygame.font.SysFont("Arial", Config.FONT_SIZE)

        # 预加载背景图
        for bg_file in Config.BG_DIR.glob("*.png"):
            try:
                self.backgrounds[bg_file.name] = pygame.image.load(bg_file)
            except pygame.error as e:
                logging.error(f"Failed to load background {bg_file}: {e}")

    def get_character(self, name: str, emotion: str) -> pygame.Surface:
        char_dir = Config.CHAR_DIR / name
        if name not in self.characters:
            self.characters[name] = {}
            for img_file in char_dir.glob("*.png"):
                emotion_name = img_file.stem
                try:
                    self.characters[name][emotion_name] = pygame.image.load(img_file)
                except pygame.error as e:
                    logging.error(f"Failed to load character {name}/{emotion_name}: {e}")
        
        return self.characters[name].get(emotion, self._get_placeholder())

    def _get_placeholder(self) -> pygame.Surface:
        """生成红色问号占位图"""
        placeholder = pygame.Surface((200, 400), pygame.SRCALPHA)
        placeholder.fill((255, 0, 0, 64))  # 半透明红色背景
        text = self.font.render("?", True, (255, 255, 255))
        placeholder.blit(text, (100 - text.get_width()//2, 200 - text.get_height()//2))
        return placeholder
