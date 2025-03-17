import os
import json
import requests
from pathlib import Path
from typing import Optional
from config.settings import Config

class StoryGenerator:
    def __init__(self):
        self.api_key = Config.DEEPSEEK_API_KEY
        self.endpoint = Config.API_ENDPOINT
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def generate_story(self, world_setting: str, chapter: int, scene: int) -> Optional[Path]:
        """生成并保存剧情文件"""
        prompt = f"{Config.PROMPT_TEMPLATE}\n\n世界观设定：{world_setting}"
        
        payload = {
            "model": "deepseek-r1",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 2048
        }

        for retry in range(3):
            try:
                response = requests.post(self.endpoint, headers=self.headers, json=payload)
                response.raise_for_status()
                
                content = response.json()['choices'][0]['message']['content']
                return self._save_scene(content, chapter, scene)
                
            except Exception as e:
                print(f"生成失败，重试 {retry+1}/3: {str(e)}")
        
        return None

    def _save_scene(self, content: str, chapter: int, scene: int) -> Path:
        """保存生成的场景文件"""
        save_dir = Path(f"game_data/story/chapter_{chapter}")
        save_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = save_dir / f"chapter_{chapter}_scene_{scene}.txt"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        return file_path
