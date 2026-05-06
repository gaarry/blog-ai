---
title: "AI资讯简报｜2026年5月7日：Anthropic给Claude装上\"梦境\"功能；五角大楼签AI协议排除Anthropic；OpenAI与Anthropic各自牵手华尔街PE"
date: 2026-05-07T08:00:00+08:00
draft: false
description: "Anthropic为Claude推出\"梦境\"自主改进功能；五角大楼与7家AI公司签署协议排除Anthropic；两大AI巨头同日与华尔街PE成立企业服务合资公司"
coverImage: "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&q=80"
tags: ["AI资讯", "Anthropic", "Pentagon", "OpenAI", "企业AI"]
categories: ["AI资讯"]
---

## 今日概览
- Anthropic为Claude推出"梦境"功能：Agent可自主回顾会话模式实现自我改进
- 五角大楼与7家AI公司签署机密环境协议，明确排除Anthropic
- OpenAI与Anthropic同日宣布牵手华尔街PE：分别成立100亿与15亿美元企业AI服务合资公司

---

## 01 AI产品：Anthropic为Claude装上"梦境"功能，Agent进入自我进化时代

5月6日，Anthropic正式推出名为"梦境"（Dreaming）的Claude Managed Agents新功能，并同步宣布与SpaceX达成算力合作，大幅提升Claude Code和API的使用限制。这是Anthropic在AI Agent能力进化上的重要一步。

"梦境"功能目前以研究预览版形式发布，核心机制是让Claude Agent能够回顾过往会话记录，从中识别行为模式并自主实现自我改进。具体而言，当Agent发现频繁失误的任务类型、收敛到错误结果的共同特征，或团队偏好时，它可以在后续执行中主动调整策略。这类似于人类在睡眠后将白天的经验转化为长期记忆的过程——Agent不再每次从零开始，而是能积累和利用历史经验。

Anthropic同时宣布扩大与SpaceX的合作协议，获得其位于孟菲斯的Colossus 1数据中心全部算力资源。该数据中心拥有超过300兆瓦新容量、超过22万块NVIDIA GPU。这一新增算力与近期公布的亚马逊（5GW协议）、Google与Broadcom（5GW协议）、微软与NVIDIA（300亿美元Azure容量）及Fluidstack（500亿美元美国AI基础设施投资）等合作，共同支撑Anthropic的算力扩张。

受益于此，Anthropic即时生效三项使用限制调整：将Pro、Max、Team及基于席位的Enterprise计划的Claude Code五小时速率限制翻倍；移除Pro和Max账户的高峰时段限制降低；大幅提升Claude Opus模型的API速率限制。该公司还透露有意与SpaceX合作开发多个GW级别的轨道AI算力设施。

**关键标签**
- "梦境"功能：AI Agent首次具备基于会话历史的自我改进能力
- SpaceX算力：超30万GPU入网，Claude Pro/Max用户直接受益
- 轨道AI算力：Anthropic与SpaceX探索卫星集群提供AI计算服务

**来源**
- [New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](https://claude.com/blog/new-in-claude-managed-agents) - Claude Blog
- [Higher usage limits for Claude and a compute deal with SpaceX](https://www.anthropic.com/news/higher-limits-spacex) - Anthropic
- [Anthropic's Claude Managed Agents can now "dream," sort of](https://arstechnica.com/ai/2026/05/anthropics-claude-can-now-dream-sort-of/) - Ars Technica

---

## 02 军事AI：五角大楼与7家AI公司签署机密协议，Anthropic被明确排除

5月1日，美国国防部正式与7家AI公司签署机密环境AI使用协议，OpenAI、Google、Microsoft、Amazon、Nvidia、SpaceX和初创公司Reflection AI均在名单之列，而此前在五角大楼拥有2亿美元机密合同额度的Anthropic被明确排除。

根据国防部研究工程副部长办公室副部长Michael J.，武断的说法在证词中被引用，这项名为"AI加速决策优势"（AI Decision Advantage）的倡议旨在为军事人员提供AI工具以维持竞争优势。协议覆盖分析、物流和大规模数据处理等场景，核心目标是推动AI在机密网络环境中的应用，而非公开互联网。

各家公司提供的技术能力各有侧重：Microsoft、Amazon和Oracle同时提供AI模型和运行所需的云端基础设施，在现有安全框架内承载AI能力；Nvidia的协议聚焦其Nemotron开源模型家族，该模型专为支持自主Agent执行多步骤任务设计。Nvidia CEO黄仁勋多次公开表示，开源模型架构对国家安全场景具有独特优势，因为允许国防部审查和修改模型内部结构；Reflection AI则是一家由Nvidia支持的初创公司，由前Google DeepMind研究员创立，目前估值为250亿美元。

Anthropic被排除的原因与此前一场合同纠纷直接相关。在失去合同后，国防部将Anthropic列为"供应链风险"并切断了其系统访问权限。国防部长Pete Hegseth在国会听证会上公开称Anthropic CEO Dario Amodei为"意识形态疯子"（ideological lunatic）。此前，Claude模型曾在军事行动中使用，包括伊朗冲突相关行动和针对委内瑞拉总统马杜罗的专项。Anthropic目前正在法院对这一供应链风险认定提出申诉。

多家参与公司明确表示，其技术不会被用于大规模监控或自主武器系统。国防部也重申此类用途违法，但尚未有公开的独立执行机制。

**关键标签**
- 供应链风险认定：Anthropic被国防部正式标记，2亿美元合同被取消
- Nemotron开源模型：Nvidia向国防部提供可审查的开源Agent模型
- 机密环境AI：AI应用从公开互联网扩展至五角大楼最高机密级别

**来源**
- [Pentagon Signs AI Deals With OpenAI, Google, Microsoft, Nvidia, and Others, Cutting Out Anthropic](https://www.ghacks.net/2026/05/04/pentagon-signs-ai-deals-with-openai-google-microsoft-nvidia-and-others-cutting-out-anthropic/) - ghacks
- [Pentagon Finalizes AI Partnerships With Seven Tech Giants, Anthropic Remains Excluded](https://computing.net/news/stocks/pentagon-finalizes-ai-partnerships-with-seven-tech-giants-anthropic-remains-excluded/) - Computing.net

---

## 03 企业AI：OpenAI与Anthropic同日宣布与华尔街PE成立合资公司，竞争企业AI服务市场

5月4日，OpenAI与Anthropic在不到24小时内先后宣布与华尔街私募股权公司成立合资企业，分别聚焦企业AI部署服务。这标志着两家AI巨头在商业化路径上同时选择借助PE资本和渠道资源，加速向大型企业客户渗透。

Anthropic率先披露，其与黑石集团（Blackstone）、Hellman & Friedman和 Goldman Sachs共同成立新合资企业，估值15亿美元。Anthropic、黑石和Hellman & Friedman各出资3亿美元。该公司还吸引了一大批VC、对冲基金和PE机构作为有限合伙人，包括Apollo Global Management、General Atlantic、GIC、Leonard Green和红杉资本。Anthropic表示，这家新公司将在金融服务、医疗和政府等受监管行业中部署企业AI服务，采用Palantir开创的"前端部署工程师"（FDE）模式——工程师团队直接驻场与客户业务团队共同构建适配工作流程的工具。

就在Anthropic公告发布后数小时，Bloomberg报道OpenAI已完成为一家名为"The Development Company"的新合资企业筹集40亿美元融资，估值达100亿美元，由19家投资机构参与，包括TPG、Brookfield Asset Management、Advent International和Bain Capital。OpenAI的合资公司规模约为Anthropic的七倍。

两家公司的整体逻辑相同：通过引入私募股权资本，创造新的企业AI销售渠道——PE机构优先向其投资组合公司推荐合资公司的服务，同时从由此产生的合同中捕获更多价值。这一模式与Palantir的企业AI服务模式高度相似，后者在联邦政府市场建立了强大的驻场工程师体系。值得注意的是，OpenAI近期刚完成122亿美元融资，估值852亿美元；Anthropic也在洽谈新一轮500亿美元融资，估值目标900亿美元。

**关键标签**
- 15亿 vs 100亿美元：两家AI巨头同日宣布PE合资，Anthropic更侧重深度驻场服务模式
- 前端部署工程师模式：AI企业服务正复制Palantir路线，强调定制化落地能力
- 投资机构全面押注：红杉、凯雷、贝恩等顶级PE/VC同时下注OpenAI和Anthropic

**来源**
- [Anthropic and OpenAI are both launching joint ventures for enterprise AI services](https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/) - TechCrunch
- [Anthropic, Goldman and others launch $1.5 billion AI venture](https://www.cnbc.com/2026/05/04/anthropic-goldman-blackstone-ai-venture.html) - CNBC

---

## 快速新闻

- **04** Adobe推出PDF生产力Agent：可将文档转化为播客、演示文稿和交互体验 Acrobat新Agent支持对话式文档编辑、智能重排和多人PDF Spaces协作，瞄准企业知识管理场景 [Adobe Blog](https://blog.adobe.com/en/publish/2026/05/06/adobes-new-productivity-agent-redefining-how-we-understand-create-share)

- **05** Google DeepMind投资EVE Online开发商，布局游戏AI研究 新独立的工作室Fenris Creations与DeepMind达成研究合作，将在离线版EVE Online上测试和评估AI模型，探索AI驱动的游戏玩法体验 [Bloomberg](https://www.bloomberg.com/news/articles/2026-05-06/google-deepmind-takes-minority-stake-in-maker-of-eve-online)

- **06** AMD数据中心业务营收同比增38%至58亿美元，AI推动CPU需求上扬 CEO Lisa Su表示AI Agent正在增加对CPU的需求，AMD与Intel的x86联盟近日发布了新的AI Compute Extensions指令集以缩小与GPU的性能差距 [AMD Investor Relations](https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results)

- **07** OpenAI与微软AGI合同定义曝光：超越人类从事大多数经济价值工作 在马斯克诉OpenAI庭审中，2019年OpenAI与微软的36页协议被公开，其中将AGI定义为"高度自主的系统，在大多数经济价值工作上超越人类" [The Verge](https://www.theverge.com/)

- **08** 43%美国民众将数据中心列为电费上涨的主要原因 皮尤研究中心调查显示，43%美国人认为数据中心是电费上涨的主因，民主党和共和党在此问题上罕见达成一致，数据中心正成为两党共同关注的能源议题 [Pew Research Center](https://www.pewresearch.org/short-reads/2026/05/05/many-americans-hold-utility-companies-responsible-for-their-rising-home-energy-bills/)

- **09** 犹他州批准4万英亩数据中心园区，总耗电量将超该州当前用电量两倍 Box Elder County的超大规模数据中心项目全面完工后预计耗电90亿瓦，是该州目前全州用电量的两倍以上，项目部分由"创智赢家"投资人Kevin O'Leary支持 [The Salt Lake Tribune](https://www.sltrib.com/news/2026/05/04/utah-data-center-final-vote-box/)

- **10** Meta正开发面向普通消费者的AI Agent，代号"Hatch" The Information报道，Meta内部正在开发一款类似OpenClaw的个人AI Agent，同时推进Instagram内Agent化购物工具，目标在Q4假期购物季前推出 [The Information](https://www.theinformation.com/articles/meta-building-ai-agent-called-hatch-agentic-shopping-tool-instagram)

- **11** OpenAI发布ChatGPT Futures路线图和B2B Signals企业AI采购指南 继GPT-5.5 Instant发布后，OpenAI同步推出面向企业买家的AI采购参考工具，帮助评估AI供应商能力差异 [OpenAI](https://openai.com/index/introducing-chatgpt-futures-class-of-2026/)