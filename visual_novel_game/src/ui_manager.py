import pygame
from typing import List
from config.settings import Config
from src.file_parser import CharacterLine

class UIManager:
    def __init__(self, screen: pygame.Surface, resource_manager):
        self.screen = screen
        self.resource = resource_manager
        self.position_map = {
            "left": 200,
            "center": 960,
            "right": 1200
        }

    def draw_background(self, bg_image: str):
        bg = self.resource.backgrounds.get(bg_image)
        if bg:
            scaled_bg = pygame.transform.scale(bg, (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
            self.screen.blit(scaled_bg, (0, 0))
        else:
            self.screen.fill((0, 0, 0))  # 黑色背景作为fallback

    def draw_characters(self, characters: List[CharacterLine]):
        for char in characters:
            char_img = self.resource.get_character(char.name, char.emotion)
            if char_img:
                x = self.position_map[char.position] - char_img.get_width() // 2
                self.screen.blit(char_img, (x, 200))

    def draw_dialogue_box(self, text: str):
        # 绘制半透明对话框
        dialog_surface = pygame.Surface((Config.DIALOGUE_RECT[2], Config.DIALOGUE_RECT[3]), pygame.SRCALPHA)
        dialog_surface.fill((0, 0, 0, 76))  # 30%透明度
        
        # 渲染文字
        rendered_text = self._wrap_text(text, Config.DIALOGUE_RECT[2] - 100)
        y_offset = 30
        for line in rendered_text:
            text_surface = self.resource.font.render(line, True, Config.TEXT_COLOR)
            dialog_surface.blit(text_surface, (50, y_offset))
            y_offset += text_surface.get_height() + 5
        
        self.screen.blit(dialog_surface, (Config.DIALOGUE_RECT[0], Config.DIALOGUE_RECT[1]))

    def _wrap_text(self, text: str, max_width: int) -> List[str]:
        words = text.split(" ")
        lines = []
        current_line = []
        for word in words:
            test_line = ' '.join(current_line + [word])
            width, _ = self.resource.font.size(test_line)
            if width > max_width:
                lines.append(' '.join(current_line))
                current_line = [word]
            else:
                current_line.append(word)
        lines.append(' '.join(current_line))
        return lines
