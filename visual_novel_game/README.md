# 视觉小说游戏引擎

[![Python版本](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![许可证](https://img.shields.io/badge/license-MIT-green)](LICENSE)

基于Python的轻量级视觉小说游戏引擎，支持章节式叙事、多角色对话和场景管理。

## 功能特性

- 📖 章节式场景管理
- 🎭 多角色对话系统
- 🖼️ 动态背景渲染
- 🎮 可视化界面管理
- 📂 模块化资源加载

## 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行示例
```python
from src.game_engine import GameEngine
from src.resource_manager import ResourceManager

def main():
    # 初始化资源管理器
    resource_mgr = ResourceManager()
    
    # 创建游戏引擎实例
    engine = GameEngine(resource_mgr)
    
    # 加载第一章场景
    engine.load_scene_list(chapter=1)
    
    # 启动游戏循环
    running = True
    while running:
        engine.advance_scene()
        # ... 渲染和事件处理逻辑 ...

if __name__ == "__main__":
    main()
```

## 项目结构
```
visual_novel_game/
├── src/                  # 源代码
│   ├── game_engine.py    # 游戏核心逻辑
│   ├── ui_manager.py     # 界面渲染管理
│   └── file_parser.py    # 场景文件解析
├── assets/               # 游戏资源
│   ├── backgrounds/      # 背景图片
│   ├── characters/       # 角色立绘
│   └── fonts/            # 字体文件
├── game_data/            # 剧本数据
│   └── story/            # 章节剧本
├── requirements.txt      # 依赖列表
└── README.md             # 项目文档
```

## 场景文件格式
```txt
# chapter_1_scene_0.txt
[background]
image = bg_cafe.jpg

[character]
name = 莉莉
position = left
image = lili_normal.png
dialogue = 今天天气真不错呢...
```

## 贡献指南
欢迎通过Issue或Pull Request参与项目改进，请遵循现有代码风格。

## 许可证
本项目采用 [MIT 许可证](LICENSE)
