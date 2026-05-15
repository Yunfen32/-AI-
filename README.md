<div align="center">

# 🧬 Life Monster

**多模态 AI 生活导师系统**

把目标拆成每天可完成的行动，用打卡、数据和 AI 建议陪你持续成长。

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

---

## ✨ 功能概览

| 模块 | 说明 |
| --- | --- |
| **🎯 今日成长面板** | AI 每日生成 3 个可执行任务，支持勾选完成、连续打卡 |
| **📊 数据仪表盘** | 累计/连续打卡天数、近 7 天趋势、任务类型分布图表 |
| **🤖 AI 助手** | 多轮对话，支持复制、语音播放、一键生成任务 |
| **💡 智能建议** | 根据目标、任务完成率、日记内容生成个性化建议 |
| **📝 我的日记** | 多模态日记（文本/图片/音频/视频），支持心情标签 |
| **👤 个人中心** | 个人资料、目标管理、简历上传与 AI 分析 |
| **🗺️ 智能规划** | 根据目标自动生成学习路线和每日任务 |

---

## 🚀 快速开始

### 环境要求

- Python 3.9+
- 可选：MySQL 8.0+、Redis 7.0+

### 安装

```bash
# 1. 克隆仓库
git clone https://github.com/Yunfen32/Life_Monster.git
cd Life_Monster

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置环境变量
cp .env.example .env   # Linux / macOS
copy .env.example .env # Windows
```

编辑 `.env`，可按需填写以下配置：

```ini
# AI API（可选，mock 模式无需填写）
ALIBABA_API_KEY=your_key_here
ALIBABA_MODEL=qwen-turbo

# MySQL（可选，默认为 JSON 文件存储）
MYSQL_HOST=127.0.0.1
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=dk

# Redis（可选）
REDIS_HOST=127.0.0.1
REDIS_PORT=6379

# 应用模式：mock（离线） / live（真实 AI）
APP_MODE=mock
```

### 启动

```bash
python app.py
```

无需 MySQL 和 Redis，系统自动降级为 JSON 文件数据库。

---

## 🏗️ 技术栈

| 层 | 技术 | 说明 |
| --- | --- | --- |
| **前端** | CustomTkinter | 现代化桌面 GUI，支持明暗主题 |
| **后端** | Flask | RESTful Web API（localhost） |
| **数据库** | MySQL / JSON 文件 | MySQL 不可用时自动降级 |
| **缓存** | Redis / 内存缓存 | Redis 不可用时自动降级 |
| **AI** | 阿里云通义千问 / 本地规则 | 支持 mock 模式离线运行 |
| **可视化** | Matplotlib | 仪表盘图表绘制 |
| **语音** | pyttsx3 | AI 助手语音播报 |

---

## 📁 目录结构

```text
LifeMonster/
├── app.py                   # 统一启动入口
├── pyproject.toml           # 项目元数据
├── requirements.txt         # 依赖列表
├── .env.example             # 环境变量模板
├── LICENSE
├── README.md
│
├── config/                  # 配置文件
│   ├── ai_config.py         # AI API 配置
│   ├── mysql_config.py      # MySQL 连接配置
│   ├── redis_config.py      # Redis 缓存配置
│   └── app_config.py        # 应用全局配置
│
├── src/
│   ├── ui/                  # CustomTkinter 界面组件
│   │   ├── login_window.py       # 登录/注册
│   │   ├── main_window.py        # 主窗口框架（含侧边栏）
│   │   ├── home_tab.py           # 首页 / 今日任务
│   │   ├── dashboard_tab.py      # 数据仪表盘
│   │   ├── chat_tab.py           # AI 助手
│   │   ├── suggestion_tab.py     # 智能建议
│   │   ├── diary_tab.py          # 我的日记
│   │   ├── profile_tab.py        # 个人中心
│   │   ├── settings_dialog.py    # 设置弹窗
│   │   ├── change_password_dialog.py
│   │   ├── theme.py              # 主题定义
│   │   └── effects.py            # 动画特效
│   │
│   ├── ai/                  # AI 功能模块
│   │   ├── chatbot.py            # 多轮对话引擎
│   │   ├── task_generator.py     # 任务生成器
│   │   └── suggestion_generator.py # 建议生成器
│   │
│   ├── data/                # 数据管理
│   │   ├── database_config.py        # 数据库工厂模式
│   │   ├── json_database_manager.py  # JSON 文件数据库
│   │   ├── mysql_database_manager.py # MySQL 数据库
│   │   └── redis_cache_manager.py    # Redis 缓存
│   │
│   ├── services/            # 业务服务
│   │   ├── auth_service.py      # 认证（密码哈希、Token）
│   │   └── tts_service.py       # 语音合成
│   │
│   └── utils/               # 工具模块
│       ├── logger.py            # 日志系统
│       └── user_state.py        # 用户会话状态
│
├── assets/                  # 静态资源
│   ├── logo/                # 应用图标
│   ├── icons/               # UI 图标
│   └── images/              # 界面图片
│
├── docs/                    # 设计文档
│   ├── use_case_descriptions.md
│   ├── use_case_diagram.md
│   └── use_case_diagram.puml
│
├── scripts/                 # 工具脚本
│   └── seed_data.py         # 种子数据初始化
│
└── data/                    # 运行时数据（已 gitignore）
    ├── json_db/             # JSON 数据库文件
    └── diary_attachments/   # 日记附件
```

---

## ⚡ 性能优化

Life Monster 在桌面应用场景下做了多级性能优化：

| 优化 | 方案 |
| --- | --- |
| **数据库写入** | 写穿透内存缓存 + 500ms 防抖合并写入，避免频繁磁盘 I/O |
| **API 缓存** | 客户端响应缓存（300s TTL），写操作按 URL 前缀精准失效 |
| **数据库缓存** | Redis 缓存层（MySQL 模式），按实体类型设置差异化 TTL |
| **UI 渲染** | Tab 切换 30s 冷却保护，避免重复加载 |
| **建议生成** | AI 调用移至后台线程，不阻塞界面交互 |
| **日志** | QueueHandler + QueueListener 异步写入，避免 I/O 阻塞主线程 |
| **Flask** | 多线程模式，请求并发处理 |

---

## 🖼️ 项目截图

<!-- 截图待补充 -->
```text
| 登录页 | 首页 | 仪表盘 |
| --- | --- | --- |
|       |      |        |
```

---

## 🤝 贡献指南

欢迎贡献代码、报告 Bug 或提出新功能建议！

- [贡献指南](CONTRIBUTING.md) — 开发规范、PR 流程
- [Issues](https://github.com/Yunfen32/Life_Monster/issues) — 报告 Bug / 提议功能

---

## 📜 开源协议

本项目基于 [MIT License](LICENSE) 开源。

---

<div align="center">

**Life Monster — 让成长更智能，让坚持更简单！**

</div>
