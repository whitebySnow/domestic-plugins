# 发布指南

仓库采用插件市场结构，市场入口为仓库根目录的 `.agents/plugins/marketplace.json`，唯一插件目录为 `plugins/china-email`。发布时保留此结构，不要在插件内再复制一套仓库。

## 发布前检查

在仓库根目录执行：

```bash
python -m unittest discover -s plugins/china-email/tests -v
git diff --check
git status --short
```

确认没有提交真实账户配置、授权码、附件、缓存或备份文件。检查插件清单 `.codex-plugin/plugin.json` 的版本与 `CHANGELOG.md` 一致，当前版本为 `1.0.0`。

## 提交与发布

1. 在 GitHub 创建仓库，并将本地仓库的远程地址设置为实际仓库地址。
2. 审阅修改后提交并推送；已有远程仓库时不要重复添加 `origin`。
3. 发布首次版本时创建 `v1.0.0` 标签和 Release，以 `CHANGELOG.md` 为发布说明来源。后续发布需同步更新插件版本和变更记录。

## 用户运行方式

克隆仓库后，从仓库根目录执行：

```bash
cd plugins/china-email
python src/china_email_mcp.py setup
```

运行时只依赖 Python 3.10+ 标准库，无需 `pip install -e .`。当前仓库不是 Python 安装包，不提供通过 pip 或 `python -m china_email_mcp` 启动的安装方式。

MCP 客户端的启动命令、参数和工作目录见 [README](./README.md#installation)。

## 相关文档

- [使用与安装](./README.md)
- [安全说明](./SECURITY.md)
- [贡献指南](./CONTRIBUTING.md)
- [变更记录](./CHANGELOG.md)
