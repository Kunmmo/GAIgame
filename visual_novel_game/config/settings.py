import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    # 显示设置
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    DIALOGUE_RECT = (50, 700, 1820, 200)  # x, y, width, height
    FONT_SIZE = 18
    TEXT_COLOR = (255, 255, 255)
    
    # 资源路径
    RES_DIR = Path("resources")
    BG_DIR = RES_DIR / "backgrounds"
    CHAR_DIR = RES_DIR / "characters"
    FONT_PATH = None  # 改为使用系统字体
    
    # API配置
    DEEPSEEK_API_KEY = os.getenv("sk-f5aef8acd7864c0eaada42e2d47a9f84")
    API_ENDPOINT = "https://api.deepseek.com/v1/chat/completions"
    PROMPT_TEMPLATE = """基于世界观设定生成视觉小说剧情，严格遵守以下格式：
scene:场景名称|背景图片路径|时间[晨/午/晚]|天气[晴/雨/雪]
character:角色名|表情[neutral/happy/angry]|位置[left/center/right]|对话内容
end"""
