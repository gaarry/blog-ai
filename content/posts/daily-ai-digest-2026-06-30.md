---
title: "OpenAI发布自研推理芯片Jalapeño，加州政府牵手Anthropic全面部署Claude"
date: 2026-06-30T08:00:00+08:00
draft: false
description: "OpenAI联手Broadcom发布自研AI推理芯片Jalapeño；加州宣布与Anthropic达成合作向所有政府机构提供Claude；Meta封堵Claude/Codex数据泄露"
coverImage: "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&q=80"
tags: ["AI", "OpenAI", "Anthropic", "Meta", "芯片"]
categories: ["AI资讯"]
---

## 今日概览
- OpenAI与Broadcom联合发布自研推理芯片Jalapeño，九个月从设计到流片，瞄准千兆瓦级数据中心部署
- 加州政府宣布与Anthropic达成首创合作，向全州所有政府机构和地方政府提供五折Claude访问
- Meta内部封堵Claude/Codex数据泄露，禁止工程师将竞品模型输出用于自身训练，正自建编程助手MetaCode

<!-- more -->

## 01 OpenAI联手Broadcom发布自研推理芯片Jalapeño，九个月打造AI算力新底座

芯片自主化浪潮中，OpenAI正式迈出关键一步。

6月24日，OpenAI与半导体巨头Broadcom联合发布首款自研AI推理加速芯片Jalapeño，代号意为"辣椒"。这是一款从零开始专为LLM推理设计的加速器，而非改造自通用AI负载的通用加速器。OpenAI从架构层面针对当前及未来大语言模型的核心计算模式进行优化，涵盖内核执行、内存调度、网络通信和模型服务等关键路径，目标是将实际利用率推向接近理论峰值。

芯片开发周期压缩到了极致的九个月。OpenAI CEO Sam Altman和联合创始人Greg Brockman从Broadcom CEO Hock Tan手中接过工程样片，标志着软硬协同战略正式落地。Jalapeño将搭配Broadcom的Tomahawk网络芯片共同部署，构建高带宽、低延迟的机群互联，支持千兆瓦（gigawatt）量级数据中心的扩展需求，首批部署预计2026年携手微软等合作伙伴启动。

从性能数据看，Jalapeño早期测试显示每瓦性能显著优于当前行业领先方案。OpenAI自身模型（包括GPT-5.3-Codex-Spark）已在实验室中于目标频率和功耗下完成验证运行。Greg Brockman表示："世界正在向算力经济转型，Jalapeño是我们全栈基础设施战略的组成部分，通过自主设计更多技术栈环节，我们可以更高效率地服务更多智能需求。"

这一芯片的推出，意味着OpenAI在GPU采购上对NVIDIA的依赖正在被逐步稀释。长期以来，大型科技公司自研芯片的案例已有谷歌TPU、亚马逊Trainium、Meta MTIA等，OpenAI的入局将推理芯片的竞争推向新高度。

### 关键标签
- 自研芯片降低对NVIDIA GPU依赖（推理端）
- 九个月从设计到流片，快速迭代能力验证
- 千兆瓦级数据中心基础设施竞争升级

### 来源
- [OpenAI and Broadcom unveil LLM-optimized inference chip](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/) - OpenAI Blog
- [OpenAI and Broadcom unveil Jalapeño inference chip](https://the-decoder.com/openai-and-broadcom-unveil-jalapeno-inference-chip/) - The Decoder
- [OpenAI, Broadcom Developed Custom AI Chip in Nine Months](https://www.bloomberg.com/news/articles/2026-06-24/openai-broadcom-developed-custom-ai-chip-in-nine-months) - Bloomberg

## 02 加州政府与Anthropic达成首创合作，五折向全州部署Claude

政府与AI公司的合作在2026年走向制度化。

6月29日，加州州长Gavin Newsom宣布与Anthropic达成一项"首创性"合作协议：加州所有州政府机构及地方政府将获得Claude的访问权限，享用五折价格优惠，同时配套免费劳动力培训、技术支持和Anthropic开发者的"工作流输入"支持。该合作旨在将AI工具系统性地嵌入政府日常运作，涵盖文件起草与摘要、信息分析、辅助日常行政等场景。

此前，加州政府已与多家科技公司建立类似合作，但规模和深度均不及此次Anthropic协议。Anthropic表示，Claude的定价基于其性能表现所提供的价值进行了优化，加州政府将获得与其他大型企业客户不同的定制化服务条款。Newsom在声明中称这是"让AI真正服务于每一个加州人"的关键一步。

该合作的背景是Anthropic正面临Fable 5遭美国政府出口管制指令暂停的困境——这一政府合作有助于Anthropic在消费市场受阻的同时，拓展B端和G端收入来源，同时积累更多政府场景下的模型部署经验。

### 关键标签
- 政府+AI公司合作制度化，首创五折部署模式
- Anthropic在Fable 5受管制期间拓展B/G端市场
- 州级政府成为AI落地重要渠道

### 来源
- [Governor Newsom Announces First-of-its-Kind Partnership with Anthropic](https://www.gov.ca.gov/2026/06/29/governor-newsom-announces-a-first-of-its-kind-partnership-providing-anthropic-tools-to-state-agencies-and-improving-services-for-californians/) - California Governor's Office
- [California partners with Anthropic to make Claude available to all state agencies](https://www.theverge.com/2026/06/29/california-anthropic-claude-partnership-state-agencies) - The Verge
- [California announces Anthropic partnership for state Claude access](https://the-decoder.com/california-announces-anthropic-partnership-for-state-claude-access/) - The Decoder

## 03 Meta封堵Claude/Codex数据泄露：内部备忘录曝光，竞品输出禁止入训

AI行业对"蒸馏"（distillation）竞争的警惕正在从口水仗走向内部治理。

The Information获取的内部文件显示，Meta已严格限制工程师使用Anthropic的Claude Code和OpenAI的Codex进行编程工作，原因是一份内部备忘录发出警告：若这些竞品模型的输出数据流入Meta的训练流程，将引发"严重的合作伙伴关系升级事件"。Meta甚至一度暂停了与这两款工具的部分合作工作。

Meta当前正在内部构建自研编程助手MetaCode，目标是削减对外部AI编程工具的依赖。知情人士透露，Meta今年在内部AI使用上的支出预计将达到数十亿美元级别，这一成本压力是推动自研的核心动因之一。内部政策同时规定，工程师不得使用AI输出创建测试任务或进行代码分析，所有AI辅助工作仍需人工复核。

蒸馏问题正在引发行业级摩擦。Anthropic此前已公开指控阿里蒸馏了其模型能力，xAI也在4月承认部分蒸馏了OpenAI的模型。OpenAI、Anthropic和Google的服务条款均明确禁止使用其模型输出构建竞争系统。Meta发言人表示公司有明确的AI工具负责任使用规范，但未就具体政策细节置评。

### 关键标签
- 竞品模型输出蒸馏问题引发行业级法律与合规风险
- Meta自研编程工具MetaCode加速，减少外部依赖
- AI公司服务条款中的"禁止蒸馏"条款开始被执行

### 来源
- [Meta limits Claude Code and OpenAI Codex use over training data fears](https://www.theinformation.com/articles/meta-limits-claude-code-and-openai-codex-use) - The Information
- [Meta restricts Claude and Codex to prevent rival AI training data leaks](https://the-decoder.com/meta-restricts-claude-and-codex-to-prevent-rival-ai-training-data-leaks/) - The Decoder
- [Anthropic accuses Alibaba of largest known AI model distillation attack](https://www.reuters.com/technology/artificial-intelligence/anthropic-accuses-alibaba-largest-known-ai-model-distillation-attack-2026-06/) - Reuters

## 快速新闻

- **04** 韩国宣布$5900亿芯片投资计划：三星与SK海力士将联合投资800万亿韩元（约合5900亿美元）在韩西南部新建四座芯片工厂，同时建设封装中心，以应对AI数据中心驱动的高带宽内存（HBM）需求激增。[The Decoder](https://the-decoder.com/samsung-sk-hynix-800-trillion-won-chip-factories-590-billion-investment/)

- **05** Google限制Meta的Gemini使用配额：据Financial Times报道，Google因自身算力不足，已对Meta等大客户的Gemini使用量实施上限。Google虽投入数十亿美元建设芯片和数据中心，仍难以满足市场对前沿模型API的爆炸性需求。[The Verge](https://www.theverge.com/2026/06/28/google-cap-meta-gemini-usage)

- **06** Coinbase转向中国AI模型，成本砍半：Coinbase CEO Brian Armstrong将公司AI路由切换至GLM 5.2和Kimi 2.7等中国模型，配合更好的缓存策略将命中率从5%提升至60%，在Token消耗持续增长的同时将AI支出削减一半。[The Decoder](https://the-decoder.com/coinbase-joins-the-rush-to-chinese-ai-models/)

- **07** 亚马逊工程师蒸馏Anthropic模型自建轻量版：The Information报道，亚马逊部分工程师正在将Anthropic的Claude模型蒸馏为更小、更廉价的内部版本，以应对2025年起按Token计费新合同带来的成本飙升。亚马逊已投资Anthropic高达250亿美元。[The Decoder](https://the-decoder.com/amazon-engineers-distill-anthropic-models/)

- **08** OpenAI发布GPT-5.6预览版，安全性评估公开：OpenAI于6月26日发布GPT-5.6预览版，并同步公开了完整系统安全卡片（System Card），详细说明模型在生物安全、恶意软件和网络安全方面的评估结果，用户可通过API体验新版本。[OpenAI](https://openai.com/index/previewing-gpt-5-6-sol/)

- **09** Cursor推出iPhone应用，SpaceX收购后加速C端布局：AI编程工具Cursor（SpaceX刚宣布以600亿美元收购）发布iPhone版，支持启动和追踪AI编程代理，并通过iPhone Live Activities实时显示任务进度。[The Verge](https://www.theverge.com/2026/06/29/cursor-iphone-app-launch)

- **10** Gemini向所有美国用户开放个性化图片生成：Google Gemini的个人智能助手（Personal Intelligence）此前仅限AI Plus/Pro/Ultra订阅用户使用，现已取消订阅门槛，所有符合条件的美国用户均可使用Gemini根据个人照片生成定制化AI图片。[The Verge](https://www.theverge.com/2026/06/29/gemini-personalized-ai-images-all-us-users)

- **11** Spotify七月起对100%纯AI音乐下架并取消变现：Spotify宣布从7月开始对完全由AI生成的曲目实施下架处理，并从即日起停止对此类内容的广告分成支付，以此区分人类创作生态与AI批量生产内容。[The Verge](https://www.theverge.com/2026/06/29/spotify-ai-generated-music-policy)