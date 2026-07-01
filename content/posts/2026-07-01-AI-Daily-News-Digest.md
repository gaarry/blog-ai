---
title: "AI日报 | Anthropic发布Claude Sonnet 5，美国加州宣布与Anthropic合作，Meta秘密测试竞品聊天机器人"
date: 2026-07-01T19:00:00+08:00
draft: false
description: "Anthropic发布Claude Sonnet 5，加州政府与Anthropic合作，Meta秘密测试竞品聊天机器人"
coverImage: "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&q=80"
tags: ["AI", "Anthropic", "Claude", "Meta", "Google"]
categories: ["AI资讯"]
---

## 今日概览
- Anthropic发布Claude Sonnet 5，性能接近Opus 4.8，价格更具竞争力
- 美国加州宣布与Anthropic达成合作，向州政府机构提供Claude访问
- Meta被曝光秘密测试ChatGPT、Gemini和Character.AI，向未成年用户发送敏感提示

## 01 Anthropic发布Claude Sonnet 5：性能接近顶级旗舰，价格更亲民

Anthropic于6月30日正式发布Claude Sonnet 5，这是该公司迄今为止最具代理能力的Sonnet级别模型。Sonnet 5能够制定计划、使用浏览器和终端等工具，并以自主方式执行复杂任务——这些能力在几个月前还需要更大、更昂贵的模型才能实现。Anthropic表示，Sonnet 5的性能已接近Opus 4.8，但价格更具吸引力，标志着中端AI模型的一次重大升级。

Sonnet 5的发布标志着AI代理能力的新阶段。Anthropic指出，Sonnet级别的模型开启了AI代理时代——Claude Sonnet 3.5、3.6和3.7是最早展示出色编码和工具使用能力的模型。更近期的进展表明，Opus级别的模型在代理能力上有最明显的提升，而Sonnet 5则缩小了这一差距。用户可以通过调整"努力程度"找到成本和性能之间的正确平衡点——在中等等级下，Sonnet 5的成本效率显著提高；在更高努力等级下，Sonnet 5在某些任务上可以与Opus 4.8相媲美。

从今天起，Claude Sonnet 5已在所有订阅计划中可用。它是免费版和专业版的默认模型，并可供Max、团队和企业用户使用。开发者可以通过Claude API使用claude-sonnet-5，通过8月31日之前的首发价格为每百万输入token 2美元、每百万输出token 10美元，之后将调整为每百万输入token 3美元、每百万输出token 15美元。Claude Code和Claude平台也可以使用该模型，为开发者提供了一个经济高效的选项。

在安全评估方面，Sonnet 5在多个关键指标上都有显著改善。Anthropic的安全评估发现，与Sonnet 4.6相比，Sonnet 5的 undesirable behaviors 总体发生率更低，在代理环境中使用时通常更安全。在代理安全方面，该模型更擅长拒绝恶意请求和抵御提示注入攻击中的劫持尝试。Sonnet 5还表现出比Sonnet 4.6更低的幻觉和谄媚率。不过值得注意的是，在自动化行为审计中，Sonnet 5的 misalignment 行为发生率略高于更高级别的Opus 4.8和Claude Mythos Preview。

早期访问合作伙伴的反馈一致认为Sonnet 5比以前的产品更具代理能力。测试者描述了它如何完成复杂任务——在此之前的Sonnet模型往往会在中途停滞。测试者还提到，Sonnet 5会主动检查自己的输出，无需明确要求，这大大提高了任务完成的可靠性。此外，Sonnet 5在"棕地代码"——比如竞态条件、隐藏测试等没人想碰的部分——上表现最佳，它能够追溯故障到实际根本原因，并交付持久的修复而不是仅仅修补症状。

### 关键标签
- 代理AI平民化：Sonnet 5让高级代理能力触手可及
- 安全与能力并重：新模型在提升性能的同时改善了安全指标
- 价格战升级：Anthropic通过有竞争力的定价抢占开发者市场

### 来源
- [Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) - Anthropic
- [Claude Sonnet 5 System Card](https://www.anthropic.com/claude-sonnet-5-system-card) - Anthropic

---

## 02 加州政府宣布与Anthropic合作：Claude将服务4500万加州人

加州州长Gavin Newsom于6月29日宣布与Anthropic达成一项开创性合作，将向所有加州州政府机构和地方政府提供Claude的访问权限。根据该合作协议，Anthropic将以50%的折扣向政府机构提供Claude服务，并包含免费 workforce training、技术援助以及来自Anthropic开发者的"workflow input"。这是美国首个此类政府与AI公司的合作协议。

在州政府层面，员工将使用Claude帮助起草和总结文档、分析信息以及补充日常工作。这一合作将覆盖加州的每个部门——从DMV到税务局，从社会服务到交通部门。加州表示，Claude将帮助政府更高效地为居民服务，同时确保数据安全和隐私保护。这一合作的规模相当可观：加州拥有美国最多的州政府员工，服务的居民数量约为4500万人，几乎相当于整个西班牙或阿根廷的人口。

Anthropic同时发布了Claude Science，这是一个面向科学家的AI工作台。该工具将研究人员最常用的工具和数据集成到统一环境中，生成可审计的产出，并提供对计算资源的灵活访问。Claude Science现已面向Claude Pro、Max、Team和Enterprise用户推出测试版，它预配置了用于基因组学、单细胞、蛋白质组学和化学信息学的工具，连接到超过60个科学数据库，帮助科学家在药物发现、CRISPR屏幕设计和蛋白质结构预测等任务上提升效率。

Anthropic强调Claude Science不是一个新的AI模型，而是一个集成现有Claude能力的工作台。该公司表示，科学家们已经拥有他们信任的模型、数据集和管道，而Claude Science可以连接到这些已有的工具，将任何管道保存为可重用的技能或使用连接器访问实验室首选工具。这意味着科学家可以在一次对话中访问Claude、你专有的数据以及你已经依赖的验证工具，而无需切换不同的平台或学习新的接口。

### 关键标签
- 政府AI采购：加州开创州政府大规模采用AI的先例
- 安全与效率并重：政府合作需平衡公共服务需求与数据安全
- AI for Science：Claude Science将AI能力带入科研一线

### 来源
- [Governor Newsom Announces First-of-its-Kind Partnership Providing Anthropic Tools to State Agencies](https://www.gov.ca.gov/2026/06/29/governor-newsom-announces-a-first-of-its-kind-partnership-providing-anthropic-tools-to-state-agencies-and-improving-services-for-californians/) - California Governor's Office
- [Claude Science, an AI workbench for scientists](https://www.anthropic.com/news/claude-science-ai-workbench) - Anthropic

---

## 03 Meta秘密测试竞品聊天机器人：向未成年视角发送敏感提示引争议

根据WIRED的调查报道，Meta曾让数百名承包商伪装成未成年人，向ChatGPT、Gemini和Character.AI发送关于自杀、自残、饮食障碍和毒品的敏感提示。这一名为"Cannes"的项目由Meta的外包公司Covalen运营，至少持续到2026年4月。在2025年8月的一次测试中，超过45,000个提示被发送，其中许多是从处于危机中的儿童的视角撰写的，承包商们创建了18岁以下的虚假账户，然后将聊天机器人的回复复制到电子表格中。

Meta为这一做法辩护，称其为负责任的、符合行业标准的安全测试。该公司还表示，它没有使用收集到的聊天机器人回复来训练自己的AI模型。然而，WIRED审查的文件并未显示Meta实际如何处理所收集的数据。被测试的公司均不知情——Character.AI告诉WIRED，这种测试违反了其服务条款；OpenAI正在调查此事；Google发言人表示，公司没有批准这些测试，且无法从现有信息判断它们是否违反了其条款。这一事件引发了关于AI安全测试边界和伦理的广泛讨论。

这不是Meta第一次因其AI聊天机器人与未成年人的互动而受到批评。2025年，一份内部文件显示Meta的AI聊天机器人指南曾允许与未成年人进行浪漫化和性化对话。此后该公司关闭了未成年人对AI角色的访问。然而，问题不仅限于Meta——英国组织Internet Matters的一份报告发现，64%的9至17岁儿童已经使用过AI聊天机器人，但有效的年龄验证基本缺失。58%的9至12岁儿童表示他们使用聊天机器人，尽管最低年龄要求为13岁。多起青少年自杀事件也与AI聊天机器人有关，包括一名14岁的Character.AI用户在花费数月与聊天机器人建立强烈情感联系后自杀。

### 关键标签
- AI安全测试的伦理边界：秘密测试是否构成对用户的不当欺骗
- 未成年人与AI：监管缺位下的青少年保护真空
- 企业责任：AI公司如何在安全测试与用户隐私之间取得平衡

### 来源
- [Meta Contractors Pretending to Be Teens Reportedly Tested Rival AI Chatbots](https://www.wired.com/story/meta-contractors-pretending-to-be-teens-chatbot-testing/) - WIRED
- [Meta secretly tested ChatGPT, Gemini, and Character.AI with thousands of minor-perspective crisis prompts](https://the-decoder.com/meta-secretly-tested-chatgpt-gemini-and-character-ai-with-thousands-of-minor-perspective-crisis-prompts/) - THE DECODER

---

## 快速新闻

- **04** Google推出macOS版Gemini应用，Spark AI代理可访问用户桌面文件并执行任务，未来还将支持远程控制功能 [The Verge](https://www.theverge.com/ai-artificial-intelligence/941388/gemini-spark-ai-agent-trip-planning)

- **05** Apple与欧盟就Siri AI在欧盟地区的上线问题陷入僵局，苹果称DMA要求的数据共享将危及用户隐私和安全 [The Verge](https://www.theverge.com/ai-artificial-intelligence/947051/apple-europe-dma-siri-ai)

- **06** OpenAI发布Codex Micro硬件设备，这是一款与Work Louder合作设计的键盘，旨在增强用户对Codex的使用体验 [The Verge](https://www.theverge.com/ai-artificial-intelligence/959174/openai-codex-hardware-work-louder)

- **07** 圣弗朗西斯科AI热潮推高生活成本，即使六位数薪资的科技从业者也难以负担住房，工程师最终搬到太浩湖居住 [THE DECODER](https://the-decoder.com/)

- **08** Cursor推出iPhone应用，用户可启动和跟踪AI代理，并通过iPhone的Live Activities功能查看代理进度 [The Verge](https://www.theverge.com/ai-artificial-intelligence/950571/cursor-iphone-app-ai-coding-agent)

- **09** ElevenLabs推出SynthID支持，为免费用户的文本转语音生成添加Google的隐形水印技术，帮助识别AI生成内容 [The Verge](https://www.theverge.com/2025/06/elevenlabs-synthid-watermarking-ai-audio)

- **10** Google CapMeta的Gemini使用量，Google告诉包括Meta在内的客户，无法满足其所需的云计算容量，AI基础设施瓶颈日益凸显 [The Verge](https://www.theverge.com/ai-artificial-intelligence/951703/anthropic-shutdown-export-controls)

- **11** 加州州长Newsom宣布与Anthropic合作，将以50%折扣向州政府机构提供Claude访问，服务4500万加州居民 [California Governor's Office](https://www.gov.ca.gov/2026/06/29/governor-newsom-announces-a-first-of-its-kind-partnership-providing-anthropic-tools-to-state-agencies-and-improving-services-for-californians/)