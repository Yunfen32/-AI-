# Life Monster — 多模态 AI 生活导师系统

> 把目标拆成每天可完成的行动，用打卡、数据和 AI 建议陪你持续成长。

## 项目概述

Life Monster 是一个基于 **CustomTkinter + Flask + MySQL/JSON + AI API** 的多模态 AI 生活导师桌面应用。它将传统的"我要做什么"计划模式，转变为"我今天要完成什么具体成果"的成果导向模式，通过 AI 提供规划、通过交互提供鼓励、通过数据提供反馈，形成完整的成长闭环。

## 功能模块

| 模块 | 说明 |
|------|------|
| **今日成长面板** | 每日 AI 生成 3 个具体可执行任务，支持打卡完成 |
| **数据仪表盘** | 累计/连续打卡天数、近 7 天趋势、任务类型分布 |
| **AI 助手** | 多轮对话，支持复制、语音播放、生成任务 |
| **智能建议** | 根据目标、任务完成率、日记内容生成个性化建议 |
| **我的日记** | 多模态日记（文字/图片/音频/视频），支持心情标签 |
| **个人中心** | 个人资料、目标设置、简历上传与 AI 分析 |
| **智能规划** | 根据目标自动生成学习路线和每日任务 |

## 技术栈

- **前端**: CustomTkinter — 现代化桌面 GUI，支持主题定制
- **后端**: Flask — RESTful Web API 服务
- **数据库**: MySQL（主用）/ JSON 文件（降级备用）
- **缓存**: Redis
- **AI**: 阿里云通义千问 API（支持 mock 模式离线运行）
- **可视化**: Matplotlib
- **其他**: pyttsx3（语音合成）、Pillow（图片处理）

## 目录结构

```
LifeMonster/
├── app.py                  # 统一启动入口
├── requirements.txt        # 项目依赖
├── .env.example            # 环境变量模板
├── .env                    # 实际配置（已 .gitignore）
├── .gitignore
├── README.md               # 项目文档
│
├── config/                 # 配置文件
│   ├── ai_config.py        # AI API 配置（从 .env 读取）
│   ├── mysql_config.py     # MySQL 连接配置
│   ├── redis_config.py     # Redis 配置
│   └── theme.py            # 统一主题配置
│
├── src/
│   ├── ui/                 # CustomTkinter 界面
│   │   ├── login_window.py      # 登录/注册
│   │   ├── main_window.py       # 主窗口框架
│   │   ├── home_tab.py          # 首页/今日任务
│   │   ├── dashboard_tab.py     # 数据仪表盘
│   │   ├── chat_tab.py          # AI 助手
│   │   ├── suggestion_tab.py    # 智能建议
│   │   ├── diary_tab.py         # 我的日记
│   │   ├── profile_tab.py       # 个人中心
│   │   ├── settings_dialog.py   # 设置弹窗
│   │   ├── change_password_dialog.py
│   │   ├── theme.py             # 主题定义
│   │   └── effects.py           # 动画特效
│   │
│   ├── ai/                 # AI 功能
│   │   ├── chatbot.py           # AI 聊天机器人
│   │   ├── task_generator.py    # 任务生成器
│   │   └── suggestion_generator.py  # 建议生成器
│   │
│   ├── data/               # 数据管理
│   │   ├── database_config.py       # 数据库工厂
│   │   ├── json_database_manager.py # JSON 文件数据库
│   │   ├── mysql_database_manager.py# MySQL 数据库
│   │   └── redis_cache_manager.py   # Redis 缓存
│   │
│   ├── services/           # 业务服务
│   │   ├── auth_service.py     # 认证服务
│   │   └── tts_service.py      # 语音合成
│   │
│   └── utils/              # 工具
│       ├── logger.py           # 日志
│       └── user_state.py       # 用户状态
│
├── assets/                 # 静态资源
│   └── logo/               # Logo 图标
│
├── data/                   # 运行时数据
│   ├── json_db/            # JSON 数据库文件
│   └── diary_attachments/  # 日记附件
│
├── docs/                   # 文档
│   └── use_case_descriptions.md
│
├── logs/                   # 运行日志
└── scripts/                # 工具脚本
    └── seed_data.py        # 种子数据
```

## 环境准备

### 系统要求
- Python 3.7+
- Windows 10/11（推荐）/ macOS / Linux
- 可选：MySQL 8.0+、Redis 7.0+

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

复制 `.env.example` 为 `.env`，填写真实配置：

```bash
cp .env.example .env     # Linux / macOS
copy .env.example .env   # Windows
```

编辑 `.env` 文件：

```ini
# AI API（可选，mock 模式无需填写）
ALIBABA_API_KEY=your_api_key_here
ALIBABA_MODEL=qwen-turbo

# MySQL（可选，默认降级为 JSON 文件存储）
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=dk

# Redis（可选）
REDIS_HOST=127.0.0.1
REDIS_PORT=6379

# 应用模式（mock=离线模拟，live=真实 API）
APP_MODE=mock
```

### 3. 启动 MySQL（可选）

```bash
# 创建数据库
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS dk DEFAULT CHARACTER SET utf8mb4;"
```

### 4. 启动 Redis（可选）

```bash
redis-server
```

### 5. 运行项目

```bash
python app.py
```

**无需 MySQL 和 Redis**，系统会自动降级为 JSON 文件数据库和缓存，离线也可运行。

## 常见问题

### MySQL 连接失败
- 系统会自动降级为 JSON 文件数据库，无需处理即可运行
- 如需使用 MySQL，检查 `.env` 中的数据库配置

### Redis 不可用
- 缓存不可用不影响核心功能，系统会自动跳过缓存

### AI API 调用失败
- 设置 `APP_MODE=mock` 可使用本地规则生成任务和建议，无需 API Key
- 如需使用 AI，在 `.env` 中填写 `ALIBABA_API_KEY`

### 登录问题
- 首次使用点击"注册"创建账号
- 也可点击"游客模式体验"直接进入

## 项目截图

截图位置：`docs/` 目录

## 后续优化方向

- [ ] 任务完成后 AI 自动复盘
- [ ] 成长报告导出（Markdown / PDF）
- [ ] 简历能力画像与技能分析
- [ ] 情绪陪伴与心情分析
- [ ] 多语言支持
- [ ] 打包为单文件 exe

---

**Life Monster — 让成长更智能，让坚持更简单！**
