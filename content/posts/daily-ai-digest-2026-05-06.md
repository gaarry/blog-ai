---
title: "AI资讯简报｜2026年5月6日：OpenAI发布GPT-5.5 Instant，幻觉率降低52.5%；ChatGPT广告平台正式上线"
date: 2026-05-06T08:00:00+08:00
draft: false
description: "OpenAI发布GPT-5.5 Instant，幻觉率大降52.5%；ChatGPT广告平台开放自服务；NVIDIA与ServiceNow推企业级自主Agent"
coverImage: "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&q=80"
tags: ["AI资讯", "OpenAI", "NVIDIA", "ChatGPT", "GPT-5.5"]
categories: ["AI资讯"]
---

## 今日概览
- OpenAI发布GPT-5.5 Instant：幻觉率降低52.5%，新增记忆来源功能，正式成为默认模型
- OpenAI ChatGPT广告平台全面开放：自服务Ads Manager上线，支持CPC竞价
- NVIDIA与ServiceNow联合推出企业级自主AI Agent：Project Arc基于OpenShell安全沙箱
- 马斯克诉OpenAI案进入第二周：Greg Brockman出庭作证，披露2017年股权谈判内幕

---

## 01 产品发布：OpenAI发布GPT-5.5 Instant，幻觉率降低52.5%重塑默认模型

5月5日，OpenAI正式发布GPT-5.5 Instant并将其确立为ChatGPT的默认模型。这是该公司2026年以来最重要的产品迭代之一，旨在解决长期困扰AI助手的准确性和个性化两大核心难题。

GPT-5.5 Instant最显著的变化体现在准确性上。OpenAI内部评估显示，在涵盖医学、法律、金融等高风险领域的测试中，GPT-5.5 Instant产生的幻觉性陈述比GPT-5.3 Instant减少了52.5%；在用户曾标记存在事实错误的困难对话中，不准确陈述更下降了37.3%。这一改进直接回应了外界对大模型可靠性的长期质疑。

除准确性提升外，新模型还在个性化能力上实现了重要突破。GPT-5.5 Instant现在能更主动地利用过往聊天记录、文件和已连接的Gmail内容来提供更相关的答案，同时响应更加简洁精准，避免不必要的后续问题和过度格式化。更重要的是，OpenAI引入了"记忆来源"（Memory Sources）功能：当回复涉及个性化内容时，用户可以看到哪些记忆或聊天记录被调用，并可随时删除或修正其中的过时信息。记忆来源不会在他人分享聊天时显示，用户始终掌控自己的数据。

GPT-5.5 Instant已在当日向所有ChatGPT用户推送，API用户可通过chat-latest访问。付费用户可在三个月内继续使用GPT-5.3 Instant，之后将被停用。个性化功能目前向Plus和Pro用户开放，网页端已上线，移动端和免费版将在数周内跟进。

**关键标签**
- 幻觉率降低52.5%：大模型可靠性里程碑
- 记忆来源功能：个性化透明化，数据控制权回归用户
- 默认模型更替：GPT-5.5 Instant正式接棒，成百亿次日常交互的新底座

**来源**
- [GPT-5.5 Instant: smarter, clearer, and more personalized](https://openai.com/index/gpt-5-5-instant/) - OpenAI
- [GPT-5.5 Instant System Card](https://openai.com/index/gpt-5-5-instant-system-card/) - OpenAI

---

## 02 商业化：OpenAI ChatGPT广告平台全面开放，自服务Ads Manager正式上线

同日，OpenAI宣布扩展ChatGPT广告试点，正式推出自服务Ads Manager并引入成本-per-click（CPC）竞价模式。这标志着ChatGPT广告从早期测试正式迈向规模化商业运营。

OpenAI最初与一小群广告主直接合作启动测试，如今已扩大至通过代理合作伙伴（包括Dentsu、Omnicom、Publicis、WPP）和技术合作伙伴（包括Adobe、Criteo、Kargo、Pacvue、StackAdapt）触达广告主。新上线的Beta版Ads Manager允许美国广告主自助注册、设置预算和竞价、上传广告、管理投放并查看效果数据，覆盖从中小型企业到全球品牌的各类客户。

此次产品更新的关键变化是引入CPC竞价模式。此前广告主仅能按CPM（每千次展示成本）购买，现在可选择按实际点击付费。OpenAI表示，ChatGPT对话通常是主动决策导向的场景——用户在学习了解某个品类、比较选项或决定下一步行动——此时一次点击是更有意义的信号。只有产生点击时广告主才需付费。

为帮助广告主追踪效果，OpenAI还推出了Conversions API和基于像素的归因工具，使广告主能了解用户与广告互动后的行为（如购买、注册等），同时不会获取个人对话内容。这些工具旨在平衡测量需求与用户隐私保护。

OpenAI强调，ChatGPT的回答保持独立性，对话保持私密，用户保持控制权。广告体验与ChatGPT答案清晰分离，不会影响回答质量。这是OpenAI在AI产品商业化路径上的重要一步。

**关键标签**
- 自服务广告平台：中小企业可直接在ChatGPT投放广告
- CPC竞价模式：广告付费从展示进阶到点击
- Conversions API：隐私保护下的效果归因体系

**来源**
- [New ways to buy ChatGPT ads](https://openai.com/index/new-ways-to-buy-chatgpt-ads/) - OpenAI

---

## 03 企业AI：NVIDIA与ServiceNow联手推出Project Arc，企业桌面Agent进入治理时代

5月5日，NVIDIA与ServiceNow在ServiceNow Knowledge 2026大会上宣布进一步扩展合作，推出名为Project Arc的企业级自主桌面Agent，标志着企业AI Agent从概念验证进入规模化落地阶段。

Project Arc是一款长期运行、自我进化的自主桌面Agent，面向知识工作者（包括开发者、IT团队和系统管理员）。与传统自动化工具不同，Project Arc通过ServiceNow Action Fabric原生连接到ServiceNow AI平台，将治理、审计和工作流智能带入自主Agent的每个操作中。它可以访问本地文件系统、终端和机器上安装的应用程序，完成复杂多步骤任务，同时满足企业大规模部署所需的控制要求。

这一合作的技术核心是NVIDIA OpenShell——一个开源的安全运行时环境，用于在隔离的、政策管理的沙箱中开发和部署自主Agent。ServiceNow正在为OpenShell做出贡献并在其基础上构建，推动企业级Agent执行通用基础的标准化。有了OpenShell，企业可以定义Agent能查看什么、能使用哪些工具以及每个操作如何被约束。

在模型层面，NVIDIA Agent Skills使ServiceNow AI Specialists等专业Agent能够在企业工作流中提供定向能力。NVIDIA AI-Q Blueprint用于构建专业深度研究Agent，Agent Toolkit包括NVIDIA Nemotron开源模型家族。两者正共同推进NOWAI-Bench企业AI Agent基准测试，其中EnterpriseOps-Gym是业界最具挑战性的企业Agent基准之一，Nemotron 3 Super在该基准的开源模型中排名第一。

效率层面，NVIDIA Blackwell平台每瓦特token输出超过Hopper 50倍以上，每百万token成本降低约35倍。这对于跨数百万工作流运行长期、自主AI Agent的企业而言至关重要。ServiceNow AI Control Tower与NVIDIA Enterprise AI Factory验证设计集成，为大规模AI工作负载提供治理和可观测性支持。

**关键标签**
- 企业级自主Agent从概念走向生产：Project Arc提供治理+执行一体化方案
- OpenShell开源安全运行时：企业Agent大规模部署的标准化基础设施
- 效率革命：Blackwell每瓦性能超Hopper 50倍，推动企业AI规模化

**来源**
- [NVIDIA and ServiceNow Partner on New Autonomous AI Agents for Enterprises](https://blogs.nvidia.com/blog/servicenow-autonomous-ai-agents-enterprises/) - NVIDIA Blog

---

## 快速新闻

- **04** 马斯克诉OpenAI案进入第二周，Greg Brockman出庭作证 The Verge live blog全程跟踪披露大量邮件和短信记录，马斯克2017年曾要求获得多数股权并获80亿美元用于火星城市 [The Verge](https://www.theverge.com/)

- **05** Anthropic、苹果、微软、Google等12家公司联合启动Project Glasswing安全计划 旨在保护全球最关键软件的开源安全计划，同时Broadcom、Cisco、CrowdStrike、JPMorganChase参与 [Anthropic](https://www.anthropic.com/news)

- **06** OpenAI_models和Codex正式登陆AWS 亚马逊云用户可直接调用OpenAI模型和托管Agent，OpenAI扩大企业分发渠道 [OpenAI](https://openai.com/index/openai-on-aws/)

- **07** 马斯克法庭上自称每周工作100小时，OpenAI反驳"他没分到钱酸了" 庭审进入第二周，马斯克出庭作证声称被Altman和Brockman背叛，后者反驳称马斯克当年主动放弃股权 [TechCrunch](https://techcrunch.com/)

- **08** NVIDIA推出Nemotron 3 Nano Omni：统一视觉、音频和语言的AI Agent模型，效率提升9倍 单芯片支持视觉/音频/语言多模态输入，为本地AI Agent提供更低成本的算力选择 [NVIDIA](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/)

- **09** OpenAI发布低延迟语音AI工程细节：通过预测性路由和模型级联实现大规模低延迟 在ChatGPT语音功能规模化的过程中，OpenAI工程团队披露了如何平衡延迟和质量的技术架构 [OpenAI](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/)

- **10** 苹果考虑让Anthropic和OpenAI为Siri提供后台AI模型支持 苹果"LLM Siri"项目因技术挑战推迟至2026年或更晚，现正测试让第三方AI公司训练可运行在苹果云基础设施上的模型 [TechCrunch](https://techcrunch.com/2025/06/30/apple-reportedly-considers-letting-anthropic-and-openai-power-siri/)

- **11** 马斯克律师要求解除Altman和Brockman在OpenAI的所有高管职务 作为诉讼准备工作的一部分，马斯克方面正式请求法庭解除两位高管的OpenAI职务，案件将于本月晚些时候开庭 [TechCrunch](https://techcrunch.com/)