# 论文优化系统 Skill 清单与 GitHub 迁移建议

来源目录：

```text
D:\哈工深\article\first Article\firstarticle3_7
```

本文档整理第一篇论文中已经迭代形成的论文优化系统，包括需要上传到 GitHub 的 skill、规则文件、检查脚本和推荐目录结构。

## 1. 总体结构

这套系统不是单个 prompt，而是一个“论文编辑工作流系统”：

```text
AGENTS.md
style/
skills/
scripts/
review/
```

其核心原则是：

```text
先诊断，再修改；
先保科学意义，再优化语言；
先控制术语和结构，再做句子润色；
不发明数据、引用、公式或更强 claim。
```

## 2. 必须上传的 Skill

### 2.1 paper-optimize

路径：

```text
skills/paper-optimize/SKILL.md
```

作用：

```text
论文优化总入口。
负责判断当前任务属于诊断、结构重建、摘要优化、反模板化、冗余压缩、术语检查还是最终验收。
```

必须保留。

它定义了所有论文编辑任务的 mandatory execution contract：

```text
1. 读取 AGENTS.md
2. 读取 style/paper_optimization_rules.md
3. 读取 style/terminology.yml
4. 读取 style/banned_phrases.txt
5. 明确任务阶段
6. 保留科学含义
7. 输出风险项和作者确认项
```

### 2.2 structure-diagnose

路径：

```text
skills/structure-diagnose/SKILL.md
```

作用：

```text
只诊断，不改写。
用于检查章节结构、段落职能、逻辑连续性、证据链、术语漂移、模板化表达和重复问题。
```

适用场景：

```text
用户问“这段有什么问题？”
用户问“这一节怎么改更好？”
用户还没有批准直接重写。
```

### 2.3 intro-rebuild

路径：

```text
skills/intro-rebuild/SKILL.md
```

作用：

```text
重构 Introduction。
把引言组织成：背景 -> 已有工作 -> 剩余 gap -> 本文目标/方法 -> 贡献。
```

适用场景：

```text
引言原始材料基本齐全，但段落顺序混乱、gap 不清楚、贡献位置不稳。
```

### 2.4 abstract-optimize

路径：

```text
skills/abstract-optimize/SKILL.md
```

作用：

```text
摘要优化。
强调 controlled scientific compression，不是普通润色。
```

目标结构：

```text
背景/问题
具体 gap
本文目标
方法或核心策略
关键结果
受限而准确的意义
```

### 2.5 anti-template-rewrite

路径：

```text
skills/anti-template-rewrite/SKILL.md
```

作用：

```text
降低 AI 味、模板味和空泛学术腔。
删除或替换空洞过渡词、泛泛重要性表述、机械对称句式和过强 claim。
```

注意：

```text
这个 skill 不是为了规避检测，也不是把论文写得口语化。
目标是让句子更像真实科研论证，而不是模板化包装。
```

### 2.6 redundancy-reduce

路径：

```text
skills/redundancy-reduce/SKILL.md
```

作用：

```text
压缩重复表达。
检查 abstract/introduction/results/discussion/conclusion 之间的自我重复。
```

原则：

```text
允许不同章节因职能不同而适度重复；
删除真正没有新增信息的重复解释、重复定义和重复转折。
```

### 2.7 terminology-guard

路径：

```text
skills/terminology-guard/SKILL.md
```

作用：

```text
术语、缩写、符号、大小写、连字符和命名一致性守护。
```

它依赖：

```text
style/terminology.yml
style/banned_phrases.txt
scripts/check_terminology.py
```

适用场景：

```text
改写前后；
投稿前；
全文术语漂移检查；
图表、正文、公式说明之间的术语一致性检查。
```

### 2.8 writing-coach

路径：

```text
skills/writing-coach/SKILL.md
```

作用：

```text
写作教学层。
不替代其他 skill，而是在诊断和修改时解释为什么这样改。
```

适用场景：

```text
用户希望学会论文写作；
需要解释语法、修辞、段落逻辑、claim calibration；
需要形成可迁移的写作规则。
```

## 3. Skill 调用关系

推荐关系：

```text
paper-optimize
  ├─ structure-diagnose
  ├─ intro-rebuild
  ├─ abstract-optimize
  ├─ anti-template-rewrite
  ├─ redundancy-reduce
  ├─ terminology-guard
  └─ writing-coach
```

其中：

```text
paper-optimize 是总调度；
writing-coach 默认作为辅助层；
terminology-guard 可在任意阶段前后插入；
其他 skill 按任务类型调用。
```

## 4. 必须配套上传的规则文件

### 4.1 AGENTS.md

路径：

```text
AGENTS.md
```

作用：

```text
项目级论文编辑宪法。
定义任务边界、编辑优先级、允许/禁止修改、输出规则。
```

必须上传。

### 4.2 paper_optimization_rules.md

路径：

```text
style/paper_optimization_rules.md
```

作用：

```text
最新合并后的论文优化总规则。
这是整套系统最重要的规则文件之一。
```

建议作为 GitHub README 或 docs 的核心引用文件。

### 4.3 terminology.yml

路径：

```text
style/terminology.yml
```

作用：

```text
术语、缩写、首用规则和标准写法。
```

如果迁移到新论文，应将其中具体术语替换成新项目术语。

### 4.4 banned_phrases.txt

路径：

```text
style/banned_phrases.txt
```

作用：

```text
禁用或慎用的模板短语。
```

现有例子：

```text
it is worth noting that
it should be noted that
deserves special attention
has important significance
provides a new idea
however
firstly
secondly
lastly
in a nutshell
all in all
```

### 4.5 preferred_patterns.txt

路径：

```text
style/preferred_patterns.txt
```

作用：

```text
推荐写作模式和导师偏好的表达倾向。
```

例如：

```text
State the evidence before the evaluation.
Use qualified claims when evidence is limited in scope.
Prefer concrete comparisons over generic novelty claims.
Keep one paragraph focused on one rhetorical job.
```

## 5. 建议上传的确定性检查脚本

路径：

```text
scripts/check_terminology.py
scripts/scan_repetition.py
scripts/detect_long_sentences.py
```

作用：

```text
check_terminology.py       检查术语/缩写/禁用表达
scan_repetition.py         检查重复短语和重复句式
detect_long_sentences.py   检查长句
```

这些脚本让论文优化系统不只是主观润色，而是有可重复检查的 harness。

## 6. 可选上传的总结文件

这些不是运行 skill 必需，但适合放到 `docs/` 中作为说明：

```text
review/paper_optimization_system_overview.md
review/skill_rules_and_workflow_for_advisor.md
review/acceptance_checklist.md
```

作用：

```text
paper_optimization_system_overview.md      中文系统说明
skill_rules_and_workflow_for_advisor.md    英文导师审阅版说明
acceptance_checklist.md                    投稿前检查清单
```

如果 GitHub 仓库是给自己用，建议上传。
如果仓库会公开，注意检查是否包含导师、个人、论文未公开信息。

## 7. 推荐 GitHub 目录结构

建议新建仓库结构：

```text
paper-optimization-system/
├─ README.md
├─ AGENTS.md
├─ style/
│  ├─ paper_optimization_rules.md
│  ├─ terminology.yml
│  ├─ banned_phrases.txt
│  └─ preferred_patterns.txt
├─ skills/
│  ├─ paper-optimize/
│  │  └─ SKILL.md
│  ├─ structure-diagnose/
│  │  └─ SKILL.md
│  ├─ intro-rebuild/
│  │  └─ SKILL.md
│  ├─ abstract-optimize/
│  │  └─ SKILL.md
│  ├─ anti-template-rewrite/
│  │  └─ SKILL.md
│  ├─ redundancy-reduce/
│  │  └─ SKILL.md
│  ├─ terminology-guard/
│  │  └─ SKILL.md
│  └─ writing-coach/
│     └─ SKILL.md
├─ scripts/
│  ├─ check_terminology.py
│  ├─ scan_repetition.py
│  └─ detect_long_sentences.py
└─ docs/
   ├─ paper_optimization_system_overview.md
   ├─ skill_rules_and_workflow_for_advisor.md
   └─ acceptance_checklist.md
```

## 8. 最小必需版本

如果只想上传一个最小可用版，至少需要：

```text
AGENTS.md
style/paper_optimization_rules.md
style/terminology.yml
style/banned_phrases.txt
skills/paper-optimize/SKILL.md
skills/structure-diagnose/SKILL.md
skills/anti-template-rewrite/SKILL.md
skills/terminology-guard/SKILL.md
scripts/check_terminology.py
```

但更推荐完整上传 8 个 skill。

## 9. 与后续科研项目的结合

后续每个论文项目建议先复制这套系统，然后只替换：

```text
style/terminology.yml
style/banned_phrases.txt 中的项目特定内容
AGENTS.md 中的 manuscript source 路径
README.md 中的项目说明
```

保留不变：

```text
先诊断后修改；
科学正确性优先；
不发明数据；
不夸大 claim；
结构问题先于句子润色；
术语和引用风险必须显式标出。
```

## 10. 建议的 README 开头

可以在 GitHub 仓库 README 中这样写：

```text
# Paper Optimization System

This repository contains a controlled manuscript-revision workflow for scientific papers.
It is designed to help diagnose, restructure, polish, de-template, and terminology-check manuscript sections without altering scientific meaning or inventing unsupported claims.

The workflow follows:

1. diagnose before rewriting;
2. preserve scientific meaning before improving fluency;
3. standardize terminology and notation;
4. reduce template-like phrasing;
5. keep section roles distinct;
6. flag high-risk scientific claims for author review.
```

