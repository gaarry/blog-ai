---
title: "MIT新突破：PaTH Attention让大语言模型具备更强的状态追踪能力"
date: 2026-01-31
draft: false
description: "MIT和MIT-IBM Watson AI Lab开发新型位置编码技术改善LLM推理能力"
coverImage: "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&q=80"
tags: ["AI", "LLM", "MIT", "Transformer"]
categories: ["AI"]
---

大多数语言使用词位置和句子结构来提取含义。但对于长文本如金融文件或小说，句法可能会演变。MIT和MIT-IBM Watson AI Lab研究人员开发了一种新的编码技术"PaTH Attention"，使位置信息具有适应性并且对上下文敏感。

## 当前Transformer的局限性

transformer中使用的主要位置编码方法"旋转位置编码(RoPE)"只考虑标记之间的相对距离，与输入数据无关。这意味着，例如，相隔四个位置的单词都会收到针对该相对距离的相同固定数学旋转。

"Transformer能够对许多领域进行准确和可扩展的建模，但它们在状态追踪方面存在局限性——这类现象被认为是我们想要的AI系统重要能力的基础，"论文资深作者Yoon Kim副教授说。

## PaTH Attention的创新

PaTH Attention不是根据标记之间的相对距离为每个词分配固定的旋转，而是灵活的，将中间词视为由小的、依赖于数据的转换组成的路径。每个基于Householder反射的数学转换就像一面小镜子，根据每个标记的内容进行调整。

序列中的每一步都会影响模型如何解释稍后的信息。这种累积效应使系统能够建模意义如何沿着词之间的路径变化，而不仅仅是它们相距多远。

## 性能提升

研究人员在合成和现实世界任务上探索了PaTH Attention的性能，包括推理、长上下文基准和完整LLM训练。PaTH Attention改进了困惑度，并在推理基准上超越了其他方法。他们还评估了数万个标记输入的检索、推理和稳定性。PaTH Attention始终证明了内容感知能力。

Kim说："我热衷于看到这些类型的数据依赖位置编码（如PATH）是否能提高transformer在结构化领域（如分析蛋白质或DNA）的性能。"

这项工作将在神经信息处理系统会议(NeurIPS)上发表。

*来源：[MIT News](https://news.mit.edu/2025/new-way-to-increase-large-language-model-capabilities-1217)*
