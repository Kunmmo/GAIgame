import pygame
from src.game_engine import GameEngine
from src.resource_manager import ResourceManager
from config.settings import Config

def main():
    pygame.init()
    screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
    pygame.display.set_caption("DeepSeek Visual Novel")

    resource = ResourceManager()
    engine = GameEngine(resource)
    
    # 初始化时加载章节1的场景列表
    engine.load_scene_list(chapter=1)  
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    engine.advance_scene()  # 每次空格触发场景推进

        screen.fill((0, 0, 0))
        engine.render(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
