# 贡献指南

感谢你对 Life Monster 的关注！🎉

## 如何贡献

### 报告 Bug

1. 确认 Bug 未被 [Issues](https://github.com/Yunfen32/Life_Monster/issues) 记录
2. 新建 Issue 时请包含：
   - 运行环境（OS、Python 版本）
   - 复现步骤
   - 期望行为和实际行为
   - 相关日志（`logs/` 目录下的 `.log` 文件）

### 提交 Pull Request

1. Fork 本仓库
2. 从 `main` 创建新分支：`git checkout -b feature/your-feature`
3. 确保代码风格与现有代码一致（见下方规范）
4. 提交前运行 `python test_app.py` 确保现有测试通过
5. 提交 PR 到 `main` 分支

### 开发规范

- **Python 版本**: 3.9+
- **编码风格**: 遵循 PEP 8（中文注释除外）
- **导入顺序**: 标准库 → 第三方库 → 项目内部模块
- **命名**:
  - 类名: `PascalCase`
  - 函数/变量: `snake_case`
  - 常量: `UPPER_SNAKE_CASE`
- **UI 组件**: 使用 `ctk.CTk*` 系列（CustomTkinter），不使用原生 `tk.*`
- **API 通信**: 统一通过 `src/api_client.py`，不直接调用 `requests`

### 数据库兼容

如果修改了数据访问层，请确保同时更新 `MySQLDatabaseManager` 和 `JSONDatabaseManager` 保持接口一致。

## 项目结构

请参考项目根目录的 `README.md` 中的目录结构图。
