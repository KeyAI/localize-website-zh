# localize-website-zh

一个适用于兼容 Agent Skills 的完整网站简体中文化 skill。

它把网站中文化作为端到端内容工程处理：完整抓取原站、制定翻译策略与术语规范、多 subagent 并行初译、统一双语审校与运行时验证，最终交付可提交的 Git 仓库。目标译文质量不低于高级专业人工翻译。

## 安装

```bash
npx skills add KeyAI/localize-website-zh
```

也可以直接克隆仓库，将其安装到 Agent 的 skills 目录。

## 使用

```text
使用 $localize-website-zh 完整抓取并专业中文化这个网站，
最终交付包含 origin/、zh/ 和过程文档的 Git 仓库。
```

可以提供远程网站 URL，也可以提供现成的本地源码。对于完整网站，skill 会优先保留原站结构、行为、资源、公式、图示和动态用户界面，而不是只翻译首页或静态正文。

## 工作流程

1. **完整抓取网站**
   - 固化未经修改的原文基准。
   - 捕获路由、HTML、CSS、JavaScript、图片、字体、媒体、动态分块、Worker、WASM 和懒加载资源。
   - 记录运行时依赖、源站问题与不可静态化边界。

2. **制定翻译策略**
   - 明确受众、语气、专业深度和简体中文区域规范。
   - 建立术语表、禁用译法、风格指南和受保护标记清单。
   - 盘点正文、元数据、ARIA、脚本字典、菜单、弹窗、Canvas/SVG 标签及条件状态。

3. **多 subagent 并行初译**
   - 按章节、路由或功能模块分配互不重叠的文件所有权。
   - 主 agent 同时承担独立翻译工作单元。
   - 本阶段只完成初译并记录问题，不提前进行零散的全站重写。

4. **整体审校与优化**
   - 集中检查遗漏、错译、术语、文风、动态语义、中文排版和可访问性。
   - 对弹窗和状态提示追踪“用户动作 → 状态 → 文案键 → 最终显示”。
   - 最后统一验证路由、资源、公式、图片、交互、404、控制台和构建结果。

## 标准交付结构

```text
origin/                   # 未修改的原文基准
zh/                       # 完整中文版本
docs/
  SOURCE_MANIFEST.md      # 来源、路由和资源清单
  LOCALIZATION_BRIEF.md   # 受众、语气和范围
  GLOSSARY.md             # 术语与受保护标记
  STYLE_GUIDE.md          # 中文表达和排版规范
  PROGRESS.md             # 阶段与工作单元进度
  DECISIONS.md            # 术语、范围和构建决策
  QA_REPORT.md            # 最终审校与验证结果
README.md
.gitignore
```

只有在第三方依赖可重建、需要编译或发布平台要求独立目录时，才增加构建脚本或 `Makefile`；不为静态站制造无必要的构建层。

## 实践案例

### 《沉浸式线性代数》简体中文版

- 原站：[Immersive Linear Algebra](https://immersivemath.com/ila/index.html)
- 在线阅读：[stellar-aurora-add9.here.now](https://stellar-aurora-add9.here.now/ila/index.html)

## skill 内容

- [`SKILL.md`](SKILL.md)：核心四阶段流程与交付约束。
- [`references/capture-and-inventory.md`](references/capture-and-inventory.md)：网站抓取与内容表面清单。
- [`references/translation-quality.md`](references/translation-quality.md)：专业翻译、并行协作和最终审校规范。
- [`references/repository-delivery.md`](references/repository-delivery.md)：仓库、构建和 Git-ready 交付标准。
- [`assets/project-docs/`](assets/project-docs/)：七份中文过程文档模板。
- [`scripts/scaffold_localization_repo.py`](scripts/scaffold_localization_repo.py)：安全创建标准目录和缺失模板，不覆盖现有文件。

初始化过程文档：

```bash
python3 scripts/scaffold_localization_repo.py /path/to/project
```
