---
title: "AI资讯简报 | OpenAI开源超算网络协议、Anthropic牵手SpaceX、美国政府推AI模型预审制度"
date: 2026-05-08T08:00:00+08:00
draft: false
description: "OpenAI联合多家巨头开源MRC超算网络协议；Anthropic与SpaceX达成计算合作；美国政府建立AI模型发布前审查制度。"
coverImage: "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&q=80"
tags: ["AI", "OpenAI", "Anthropic", "SpaceX", "政策监管"]
categories: ["AI资讯"]
---

## 今日概览
- OpenAI联合AMD、NVIDIA等五大厂商开源MRC超算网络协议，可连接超过13万GPU
- Anthropic与SpaceX（xAI）达成计算合作协议，获得Colossus 1全部算力
- 美国政府建立AI模型预发布审查制度，Google、Microsoft、xAI率先签署协议

## 01 [基础设施] OpenAI联合五大厂商开源MRC协议：一张网络如何连接13万GPU

大语言模型训练的核心瓶颈，从来不只是芯片算力。当数万个GPU需要同时协作时，它们之间的数据传输网络才是真正的挑战。OpenAI于5月5日宣布与AMD、Broadcom、Intel、Microsoft、NVIDIA联合开发并开源了**MRC（Multipath Reliable Connection，多路径可靠连接）协议**，旨在彻底重构超算网络的核心架构。

传统AI超算网络面临两大难题：一是网络拥塞——当大量GPU同时通信时，数据包会在同一链路上碰撞，造成延迟；二是网络故障的连锁反应——一个链路或交换机的失效，往往导致整个训练任务崩溃或重启，在同步预训练场景下这种问题尤为致命，因为数千GPU以"锁步"方式协同工作，任何一个节点的延迟都会像水波纹一样扩散到全局。

MRC的核心创新在于"多平面网络+数据包喷雾"。与其将每个800Gb/s网络接口当作一条高速通道，不如将其分割为8个独立的100Gb/s平面，构建8张并行的子网络。一个原本能连接64端口的交换机，现在可以连接512个端口，由此可以用仅两层交换机构建出一个能容纳**约13.1万GPU**的超大规模网络——传统方案需要三到四层架构才能实现同等规模。

在数据包层面，MRC不再让每个传输任务走单一路径，而是将单个传输的数据包分散喷洒到数百条不同路径上同时传输。数据包可以无序到达，接收端根据每个数据包内置的内存地址信息直接写入正确位置。这从根本上消除了网络热点——任何单个链路的拥塞都不会成为全局瓶颈。实验数据显示，在10万GPU级别的训练集群中，MRC将网络抖动降低了80%以上。

该协议基于RDMA over Converged Ethernet（RoCE）扩展，融合了Ultra Ethernet Consortium的技术成果并加入了SRv6源路由机制。目前已在OpenAI最大的NVIDIA GB200超算集群（包括Oracle云德州Abilene站点和微软Fairwater超算）部署使用，并通过Open Compute Project向全行业开放规范文档。

### 关键标签
- 开源协议降低行业进入门槛，网络设计成为AI竞争新维度
- 多路径冗余替代单点故障，13万GPU仅需两层交换
- AMD、Broadcom、Intel、NVIDIA首次在同一开源项目下协作

### 来源
- [Supercomputer networking to accelerate large scale AI training](https://openai.com/index/mrc-supercomputer-networking/) - OpenAI
- [AMD Advances AI Networking at Scale with MRC](https://www.amd.com/en/blogs/2026/amd-advances-ai-networking-at-scale-with-mrc.html) - AMD Blog
- [NVIDIA Blog: Spectrum-X Ethernet & MRC](https://blogs.nvidia.com/blog/spectrum-x-ethernet-mrc/) - NVIDIA

---

## 02 [战略合作] Anthropic牵手SpaceX：算力饥渴的Claude与Musk的意外和解

Anthropic当地时间5月6日宣布与Elon Musk旗下公司SpaceX（xAI正在更名为SpaceXAI）签署重要计算合作协议，Anthropic将获得**SpaceX Colossus 1数据中心在孟菲斯的全部计算容量**，超过300兆瓦（MW）。双方还表达了在太空开发多个千兆瓦级算力设施的共同兴趣。

这笔交易的达成颇具戏剧性。就在数月前，Musk还在社交媒体上连续批评Anthropic，称其"注定会与自己的名字背道而驰（misanthropic，即反人类的）"，并质问"有没有比Anthropic更虚伪的公司"。然而本周三，Musk突然转变态度，在X平台上发帖称他花了一整周与Anthropic高管团队相处，结果是"印象非常深刻"——"我遇到的每个人都能力极强，且真正在乎做正确的事，没有人触发我的邪恶探测器。"这一180度的态度转变，与当前正在进行的Musk诉OpenAI案形成了微妙的对比。

对于Anthropic而言，这笔交易直击其最紧迫的痛点。自2026年以来，Claude用户需求持续爆发式增长，导致基础设施"不可避免地承压"，高峰时段的可靠性和性能均出现下滑。Anthropic已在近期密集签署多项算力协议，包括与亚马逊达成的**数百亿美元云服务协议**。此次获得Colossus 1全部容量，预计将直接改善Claude Pro和Claude Max付费订阅用户的服务质量。

值得关注的是，xAI本身也在快速扩张。Musk在5月2日完成了SpaceX与xAI的合并，xAI将作为独立公司不复存在，而是整合进SpaceX成为"SpaceXAI"。合并后不久，SpaceXAI便宣布了这一与Anthropic的合作。协议内容显示，Anthropic获得的300MW容量将使SpaceXAI接近盈亏平衡，而Anthropic则得以弥补其算力缺口，双方各自获得IPO前的关键筹码。

### 关键标签
- 商业利益跨越政治分歧，算力合作超越意识形态分歧
- Colossus 1全部容量将改善Claude用户付费体验
- Musk从"反Anthropic"到"印象深刻"，态度转变折射利益计算

### 来源
- [Anthropic, SpaceX announce compute deal](https://www.cnbc.com/2026/05/06/anthropic-spacex-data-center-capacity.html) - CNBC
- [New Compute Partnership with Anthropic](https://x.ai/news/anthropic-compute-partnership) - xAI
- [Anthropic Gets in Bed With SpaceX as the AI Race Turns Weird](https://www.wired.com/story/anthropic-spacex-compute-deal-colossus/) - Wired

---

## 03 [政策监管] 美国政府建立AI模型预发布审查制度：五家公司率先纳入监管框架

美国商务部下属的**AI标准与创新中心（CAISI）**于5月5日宣布，已与Google DeepMind、Microsoft和xAI签署新协议，将允许美国政府在AI模型公开发布前对其进行安全评估。同时，CAISI表示已与OpenAI和Anthropic就2024年签署的原有协议进行了重新谈判，以符合商务部长Howard Lutnick的指令和"美国AI行动计划"的要求。

根据协议，CAISI将对这些公司的前沿AI模型进行**"发布前评估"（pre-deployment evaluations）**，即在模型正式向公众开放前，先交给政府进行能力与安全评估。这一机制与药品监管中的"临床试验"逻辑类似，目的是在模型进入数亿用户手中之前，提前识别潜在安全风险。CAISI表示，评估重点是前沿AI能力以及这些能力对国家安全的影响。

这一政策的推进，与Anthropic上月发布的**Claude Mythos Preview**模型直接相关。该模型专注于识别软件安全漏洞和弱点，能力极为强大，Anthropic因此主动限制了推广范围，仅向部分企业客户提供。然而即便如此，Mythos的发布仍引起白宫高度关注——Anthropic CEO Dario Amodei在模型发布数日后便受邀赴白宫与高级官员会面，而彼时美国国防部已宣布将Anthropic列入供应链风险黑名单，禁止其参与美军相关合同。

与此同时，白宫正在考虑通过**行政令**成立新的AI工作组，整合政府官员和科技公司高管共同探讨AI监管框架。据The New York Times率先报道，该工作组可能会将模型发布前的政府审查制度进一步制度化、法定化。值得注意的是，在5月2日结束的Musk诉OpenAI案第一周庭审中，多位证人也详细披露了OpenAI董事会与Altman之间围绕安全与商业化优先级的长期矛盾，这为政府加强AI监管提供了更多舆论基础。

### 关键标签
- AI监管"药品化"趋势：预发布审查或成行业标准
- Anthropic身陷"政府黑名单"与"白宫座上宾"的双重身份矛盾
- CAISI协议标志着政府对前沿AI的介入从研究合作升级为制度性监督

### 来源
- [Trump admin moves further into AI oversight, will test Google, Microsoft and xAI models](https://www.cnbc.com/2026/05/05/ai-oversight-trump-google-microsoft-xai.html) - CNBC
- [CAISI Signs Agreements Regarding Frontier AI National Security Testing](https://www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-security-testing) - NIST
- [Federal government to vet AI models before release](https://thehill.com/homenews/5863937-google-microsoft-xai-ai-testing/) - The Hill

---

## 快速新闻

- **04** [Anthropic为Claude推出"Dreams"功能：AI开始具备自我反思能力](https://platform.claude.com/docs/en/managed-agents/dreams) Anthropic为其托管代理推出实验性功能"Dreams"，允许Claude在后台回顾历史会话记录，识别行为模式、发现高频错误并优化记忆存储。该功能目前处于研究预览阶段。Anthropic

- **05** [OpenAI发布GPT-5.5 Instant系统卡片](https://openai.com/index/gpt-5-5-instant-system-card/) OpenAI于5月5日发布GPT-5.5 Instant的安全系统卡片，详细披露模型的安全评估结果和已知局限性。该模型被定位为"更智能、更清晰、更个性化"的新一代GPT。OpenAI

- **06** [Pew调查：43%美国人将电价上涨归咎于数据中心](https://www.pewresearch.org/short-reads/2026/05/05/many-americans-hold-utility-companies-responsible-for-their-rising-home-energy-bills/) 皮尤研究中心调查显示，43%的美国民众将家庭电费上涨的主要原因归咎于数据中心的能源消耗。值得注意的是，该观点在共和党与民主党选民中呈现高度一致性，数据中心正成为罕见的"两党共识"议题。Pew Research

- **07** [Snap与Perplexity合作关系"友好结束"](https://www.theverge.com/ai) Snap在2026年Q1投资者信中告知分析师，不要再期望Perplexity对其营收产生任何贡献——这意味着曾被Snap寄予厚望的AI搜索合作已告终结。Snap同时暗示将于6月公布更多智能眼镜（Specs）进展。The Verge

- **08** [Nvidia与Corning达成大规模光纤合作，或将重塑AI数据中心基础设施](https://www.cnbc.com/2026/05/06/nvidia-corning-optical-factories-nc-texas-ai.html) Nvidia与Corning宣布达成大规模光缆合作协议，将在北卡罗来纳州和得克萨斯州建设光纤工厂。业界认为该合作将显著改善AI数据中心的内部通信带宽，降低长距离传输延迟。CNBC

- **09** [Samsung市值突破1万亿美元，AI芯片热潮推动韩国综合指数创历史新高](https://www.cnbc.com/2026/05/06/samsung-electronics-ai-chip-rally-kospi-record-1-trillion.html) 得益于AI芯片需求的持续爆发，三星电子股价年内涨幅超过15%，市值突破1万亿美元大关，成为韩国综合股价指数（KOSPI）历史上首个触及这一里程碑的公司。CNBC

- **10** [Musk诉OpenAI案庭审进行中：OpenAI前董事会成员Helen Toner作证](https://www.theverge.com/ai) 在Oakland进行的Musk诉OpenAI案中，前董事会成员Helen Toner详细陈述了Altman被解雇的真实原因——并非单一事件，而是"诚信与坦率方面的一系列行为模式"。她同时透露自己是从Twitter截图上才知道ChatGPT已经发布。The Verge

- **11** [Apple研发投入突破营收10%，AI竞争催生"紧迫感"](https://www.cnbc.com/2026/05/06/apples-rd-spending-climbs-to-10percent-of-revenue-on-ai-investments.html) 苹果公司最新财务数据显示，其研发支出已占营收的10%以上，主要由AI相关项目驱动。苹果正在加速将AI能力整合进Siri及iPhone全系列产品，以应对来自Google Gemini和OpenAI的竞争压力。CNBC
