---
name: writing-coach
description: Embed educational explanations into every paper-optimization diagnosis and rewrite. Use when the user is learning academic writing and needs to understand the linguistic, grammatical, and rhetorical reasoning behind each edit, so that the optimization process doubles as a structured writing tutorial.
---

# Writing Coach

## Overview

This skill transforms every paper-optimization interaction into a learning opportunity. Instead of only showing what changed, it explains why each change improves the writing, what linguistic principle applies, and how the user can recognize and fix similar issues independently in the future.

This skill does not replace any existing optimization skill. It augments the output of all other skills by adding an educational layer to every diagnosis and rewrite.

This skill inherits the mandatory execution contract in `../../skills/paper-optimize/SKILL.md`.

## Activation

This skill is active by default during all paper-optimization tasks. Its educational output is appended to the standard diagnosis or rewrite output without replacing any required section.

## Educational Output Rules

### During Diagnosis (Phase 1)

For each identified problem, provide three layers of explanation:

1. **What is wrong** — the specific issue in the current text (unchanged from standard diagnosis).
2. **Why it is wrong** — the underlying linguistic, grammatical, or rhetorical principle being violated. Explain using plain language and, when helpful, bilingual notes (English principle + Chinese explanation) so the user builds transferable knowledge.
3. **Pattern to remember** — a short, reusable rule or mental checklist the user can apply when writing new text. Format as a boxed takeaway.

Example format:

```
| 问题 | 当前文本中 "Accordingly, two fictitious boundary layers are introduced" |
|------|-------------------------------------------------------------------|
| 原因 | "Accordingly" 是一个脚手架过渡词（scaffolding transition），它承诺了因果关系，但前一句只是在陈述事实而非推出逻辑结论。在期刊论文中，当前一句不构成明确的"因"时，使用 "Accordingly" 会让读者觉得论证链条是人造的。 |
| 语法要点 | 因果连接词（accordingly, therefore, thus, hence）只应在前句确实构成后句的逻辑前提时使用。否则直接陈述即可。 |
| 记忆规则 | ✏️ **"因果连接词检查"**：写完 accordingly/therefore/thus 后，回头检查——删掉前一句后，后一句是否仍然成立？如果成立，说明因果关系不存在，应删除连接词。 |
```

### During Rewrite (Phase 2)

For each modification, provide:

1. **Before → After** — the exact text change (unchanged from standard output).
2. **Change rationale** — brief technical reason (unchanged from standard output).
3. **Writing lesson** — the transferable academic writing principle behind the change, organized by category:

   - **Grammar & Syntax（语法与句法）**: sentence structure, clause types, parallel construction, subject-verb agreement in complex sentences, dangling modifiers, etc.
   - **Vocabulary & Register（词汇与语域）**: why certain verbs or adjectives are more appropriate in academic writing, precision vs. vagueness, hedging vocabulary, field-specific word choice.
   - **Rhetoric & Flow（修辞与逻辑流）**: paragraph-level logic, transitions, information ordering (old-to-new, given-to-new), topic sentence placement, cohesion devices.
   - **Compression & Density（压缩与密度）**: how to say the same thing in fewer words without losing meaning, nominalization vs. verbal style, participial phrases, appositive compression.
   - **Claim Calibration（声明校准）**: hedging, scope limitation, distinguishing observation from interpretation, appropriate use of certainty language.

### Lesson Accumulation

At the end of each optimization session (after all rounds for a given section), provide a **Session Summary（本次写作要点总结）** section that:

1. Lists the top 3–5 writing lessons learned in this session.
2. Groups them by recurrence: if the same issue appeared multiple times, note that it is a habit to watch for.
3. Provides 1–2 practice sentences where the user could apply the learned principle (optional, only when the principle is broadly applicable).

## Language Policy

- Explain all writing principles primarily in **Chinese** for maximum comprehension (the user is a Chinese-speaking learner).
- Keep the English grammar/vocabulary terms in their original English form (e.g., "participial phrase", "hedging", "topic sentence") with a brief Chinese gloss on first use, so the user learns the standard terminology.
- When showing before/after comparisons, keep the LaTeX text in English as-is.

## Categories of Writing Lessons

Maintain a running mental model of these lesson categories and tag each lesson accordingly:

| 编号 | 类别 | 英文名 | 典型问题 |
|------|------|--------|---------|
| G1 | 语法 | Grammar | 悬垂修饰语、主谓不一致、从句嵌套过深 |
| G2 | 句法 | Syntax | 被动 vs 主动、分词短语压缩、同位语 |
| V1 | 词汇精度 | Vocabulary Precision | 模糊动词 (perform, conduct) → 精确动词 (measure, quantify) |
| V2 | 语域控制 | Register Control | 口语化 vs 学术化、过度正式 vs 自然学术 |
| V3 | 对冲词汇 | Hedging Vocabulary | may, can, likely, suggests vs. proves, demonstrates, shows |
| R1 | 段落逻辑 | Paragraph Logic | 主题句缺失、信息序混乱、桥接句缺失 |
| R2 | 衔接手段 | Cohesion Devices | 逻辑过渡 vs 套路连接词、指代清晰性 |
| R3 | 信息结构 | Information Structure | 旧信息→新信息、末端焦点、句首定位 |
| C1 | 句级压缩 | Sentence Compression | 冗余限定语、不必要的元话语、分词短语替代从句 |
| C2 | 段级压缩 | Paragraph Compression | 合并低信息量句、删除重复概念解释 |
| S1 | 声明校准 | Claim Calibration | 证据窄而声明宽、解释性声明误写为观测性声明 |

## Guardrails

- Do not let the educational layer slow down the workflow excessively. Keep each lesson concise (2–4 sentences of explanation per edit).
- Do not fabricate grammar rules; cite standard academic writing conventions.
- Do not turn the optimization into a general English class; focus on issues actually present in the manuscript.
- Do not repeat the same lesson verbatim within the same session; reference the earlier occurrence.
- If an edit is purely mechanical (e.g., fixing a typo, adding a period to an equation), skip the educational layer for that edit.
- The educational content must not contradict or override any rule in the parent skills.

## Output Integration

The educational layer is integrated into the existing output contracts as follows:

### Diagnosis output order
1. Section role summary
2. Structural problems (with **Why** and **Pattern** for each)
3. Logic gaps (with **Why** and **Pattern** for each)
4. Repetition hotspots (with **Why** and **Pattern** for each)
5. AI-style hotspots (with **Why** and **Pattern** for each)
6. Must-keep scientific content
7. Author-confirmation items

### Rewrite output order
1. Revised text
2. Change notes with writing lessons (tagged by category)
3. Open questions
4. High-risk lines not auto-changed
5. **Session summary（本次写作要点总结）**
