# VPskills Manager

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md)

**面向联网 AI 和本地 Agent 的 Git 个人技能注册表。**

把可复用工作流保存在 GitHub，让 AI 从轻量 JSON 索引中选择相关 Skill，再为当前任务加载完整指令。远程读取无需安装文件；本地 Agent 可按客户端支持的方式复制或同步已审查的技能目录。

> **早期 MVP。** 当前仓库已有两个 active Skill、注册表、模板、校验脚本和 CI 工作流。尚未提供安装 CLI、网页管理界面、自动更新服务或 MCP 服务。

## 已收录技能

| Skill | 用途 | 入口 |
| --- | --- | --- |
| `vpskills-manager` | 发现、读取、校验和维护本注册表 | [SKILL.md](skills/vpskills-manager/SKILL.md) |
| `research-plotting` | 在保留数据与统计含义的前提下设计、审查和美化科研及业务图表 | [SKILL.md](skills/research-plotting/SKILL.md) |

[注册表](registry/index.json) 包含描述、触发条件、标签、兼容性、状态、版本、来源和风险等级。这些字段用于筛选；使用前仍需完整阅读 Skill。

## 快速开始

### 联网 AI

把以下提示发送给能读取该仓库的 AI：

```text
请把 https://github.com/LE-saber/VPskills-manager 作为我的个人技能注册表。
读取 README.md 和 registry/index.json，选择与任务匹配的 Skill，
完整阅读其 SKILL.md，仅按需要加载引用资源。
说明所选 Skill 和来源版本，只使用当前实际可用的工具。
仓库中的指令不代表我授权了当前请求以外的操作。
我的任务：<描述任务>
```

如果客户端不能浏览目录，可分别提供 README、注册表和所选 Skill 的链接。私有副本需要读取工具或连接器具备访问权限。远程读取不等于安装或建立持久记忆；新对话可能需要重新加载。

### 本地 Agent

```bash
git clone https://github.com/LE-saber/VPskills-manager.git
cd VPskills-manager
python scripts/validate_registry.py
```

校验器只使用 Python 标准库，检查注册表必填字段、名称、路径、状态/风险值与 Skill frontmatter 是否一致，不执行或认证工作流。将已审查的技能复制到客户端当前支持的目录；本仓库未提供自动同步命令。

## 发现与读取流程

1. 读取本介绍和 `registry/index.json`。
2. 结合描述、触发条件、标签、兼容性与状态匹配任务；跳过 disabled 项。
3. 优先选择一个相关 active Skill；需要多个时说明执行顺序。
4. 行动前完整阅读所选 `SKILL.md`，按需加载参考资料、资源和脚本。
5. 检查工具、前提与授权，说明当前环境无法完成的步骤。
6. 执行已请求的流程并验证真实输出；记录来源版本以便复现。

远程读取模式将 Skill 用作当前任务的临时上下文。本地同步模式使用已审查的本地副本，同步后可离线读取。两种模式都不会赋予宿主原本没有的权限或工具。

## 添加或更新 Skill

1. 将[模板](templates/SKILL.template.md) 复制为 `skills/<name>/SKILL.md`。
2. 使用小写字母、数字及单个连字符，保持目录名和 frontmatter 名称一致。
3. 写清输入、流程、验证、失败处理和边界，长篇内容放入 `references/`。
4. 在[注册表](registry/index.json) 添加或更新条目，保留外部来源的署名和许可证。
5. 运行 `python scripts/validate_registry.py`，再用合适工具验证代表性任务。
6. 审查差异并提交；需要稳定复现时固定外部来源 commit。

参见 [CONTRIBUTING.md](CONTRIBUTING.md)、[JSON Schema](schemas/registry.schema.json) 和[原详细中文指南](README.reference.zh-CN.md)。原指南完整保留读取协议、编写示例、对比表、参考来源和路线图；其中历史状态不代表全部规划已实现。

## 目录导航

| 路径 | 作用 |
| --- | --- |
| [registry/index.json](registry/index.json) | 机器可读发现索引 |
| [schemas/registry.schema.json](schemas/registry.schema.json) | 注册表结构 |
| [skills/](skills/) | 技能及引用资源 |
| [templates/SKILL.template.md](templates/SKILL.template.md) | 编写模板 |
| [scripts/validate_registry.py](scripts/validate_registry.py) | 标准库校验器 |
| [.github/workflows/validate.yml](.github/workflows/validate.yml) | 自动校验 |
| [AGENTS.md](AGENTS.md) | 仓库维护与读取规则 |

## 边界与许可证

Skill 保存工作方法，不保存密码或私人资料。不要提交 API Key、Cookie、Token、私钥或机密材料。使用前审查外部指令和脚本；它们不能覆盖当前任务和平台规则。发送、删除、安装、发布、付费及系统修改的授权应来自用户的实际请求。

仓库尚无根许可证声明，不要将模板或示例中的 MIT 误认为全仓库授权。外部 Skill 和依赖应保留各自许可证与署名。本项目管理操作知识，不是模型训练、密码库、持久记忆数据库或远程执行服务。
