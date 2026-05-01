---
slug: "musk-openai-trial-day3"
title: "Musk出庭第三天：庭审实录直击OpenAI创办恩怨、Anthropic推代码安全扫描、OpenAI推高级账户保护"
date: 2026-05-01T08:00:00+08:00
draft: false
description: "Musk v. OpenAI案庭审第三天：Musk交叉盘问狼狈收场，承认未细读合同；Anthropic推出代码安全扫描工具Claude Security；OpenAI上线高级账户安全功能。"
coverImage: "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&q=80"
tags: ["AI", "OpenAI", "Musk", "Anthropic", "安全"]
categories: ["AI资讯"]
---

## 今日概览
- Musk v. OpenAI庭审第三天：交叉盘问持续数小时，Musk多次拒绝正面作答、法官当庭吐槽"太难对付"，庭审揭示创办初期股权与控制权争夺细节
- OpenAI于4月30日推出Advanced Account Security功能：支持Passkey与物理安全钥匙，联手Yubico，面向记者、政治人物等高风险用户
- Anthropic宣布Claude Security公开测试：基于Claude Opus 4.7模型扫描代码库漏洞并生成修复方案，向企业用户全球开放

## 01 Musk出庭第三天：交叉盘问狼狈，OpenAI创办恩怨全面曝光

4月30日，Musk v. OpenAI案进入庭审第三天，Elon Musk接受OpenAI代理律师William Savitt的交叉盘问，全程持续数小时，多个细节令陪审团和旁听者印象深刻——并非因为他的证词说服力强，而是因为他几乎拒绝回答任何需要"是"或"否"的简单问题。庭审结束后，法官Yvonne Gonzalez Rogers当着所有人的面评价Musk："他有时候真的很难对付（He was at times difficult）。"

这场庭审逐步揭开了OpenAI创办初期内部权力斗争的更多真相。据The Verge全程跟踪报道，Savitt在盘问中揭示：2017年前后，Musk曾向OpenAI管理层提出四项要求——获得四个董事会席位，并持股51%，实现对公司的完全控制权。这一要求被其他联合创始人拒绝后，Musk随即暂停了对OpenAI的季度捐款。法庭文件显示，Musk向OpenAI承诺的累计10亿美元捐款，实际以"捐款"形式（不求回报）支付约4400万美元，以及约15辆Tesla，总值约5000万美元。Savitt当庭指出，Musk放弃捐款并非出于安全顾虑，而是在未获控制权后的一次"赌气"行为。

更令陪审团印象深刻的细节出现在关于Tesla与OpenAI合并方案的讨论中。Musk曾在邮件中向Ilya Sutskever和Greg Brockman表示，OpenAI"注定失败"，并提议将OpenAI并入Tesla，称"Tesla是唯一能跟Google竞争的路径"。这一方案同样未获通过，Musk于2018年退出OpenAI董事会。法庭上，Musk承认自己在提出这一方案时，Tesla并未有实际的AGI研发计划——尽管他在社交媒体上曾暗示Tesla正在推进AGI。

关于Musk是否认真审查过OpenAI商业转型的条款文件，Savitt的追问令Musk的回应显得颇为狼狈。OpenAI曾于2018年前后发出提案，计划引入有限控股结构。Musk声称自己只读了封面段落，即"投资者应将投资视为可能无回报的捐款"这一免责声明。"我没仔细读，我只看了标题，" Musk在证词中说。而Savitt随即引用了Musk在取证时的说法——"我不确定我是否真的读了那份条款清单"——两者明显矛盾。法官Rogers当场打断Musk的冗长辩解，要求他给出直接回答。

庭审第三天还出现了若干花絮：Musk被问及是否理解线性时间的基本概念，因为他在某处称自己2018年前仍是OpenAI董事；他还承认，包括xAI在内，他目前所有的公司均为营利性质，"我以为我用OpenAI创立了一家非营利机构，结果他们偷走了那家慈善机构。"在解释自己为何签署2023年那封呼吁暂停大模型训练的公开信时，Musk称那只是一封"不具约束力的公开信"，签署前一周他已注册了xAI公司，但并未向外界披露这一关联。

本轮庭审揭示了大量此前未公开的邮件记录，包括Valve联合创始人Gabe Newell与Musk的通信——Musk曾在2018年通过Newell试图安排与Hideo Kojima的会面，并向OpenAI管理层为Kojima争取加入的机会。OpenAI最终拒绝了这一提议。

### 关键标签
- Musk庭审承认自己只看条款"标题"，未仔细阅读即放弃对OpenAI的反对意见
- 创办初期股权设计曝光：Musk曾索求51%控制权，被拒后断供
- 法官当面评价 Musk "难对付"，Tesla无AGI计划却提议合并OpenAI

### 来源
- [Elon Musk's worst enemy in court is Elon Musk](https://www.theverge.com/tech/921022/elon-musk-cross-openai-altman) - The Verge
- [Musk v. Altman: Day three live updates](https://www.theverge.com/ai-artificial-intelligence/921022/elon-musk-cross-openai-altman) - The Verge
- [Evidence: Gabe Newell, Hideo Kojima and the OpenAI tour request](https://www.theverge.com/ai-artificial-intelligence/920775/evidence-exhibits-elon-musk-sam-altman-openai-trial) - The Verge

## 02 OpenAI推出Advanced Account Security：Passkey+物理安全钥匙保护高风险用户

4月30日，OpenAI正式推出Advanced Account Security功能，这是该公司面向ChatGPT和Codex账户推出的可选高级安全设置，主要针对记者、政治人物、研究人员和异议人士等面临定向网络攻击风险的用户群体。新功能的核心是与Yubico达成合作，用户可使用Passkey或物理安全钥匙（如YubiKey）登录账户，同时开启新设备登录提醒，并可选择退出AI模型训练数据使用。

这套安全机制旨在对抗近年来针对AI账户的高风险定向攻击。攻击者通常通过钓鱼手段获取登录凭证，随后滥用账户访问权限或提取会话历史。OpenAI在公告中表示，Advanced Account Security用户将被自动排除在AI模型训练数据之外，从根本上消除了账户会话被用于改善模型的顾虑。

TechCrunch报道指出，这是OpenAI首次与硬件安全钥匙制造商建立正式合作。Yubico是全球最主流的FIDO2物理安全钥匙供应商，其钥匙支持USB-A、USB-C和NFC多种接口，可插入电脑或触碰手机完成认证。由于物理安全钥匙无法被钓鱼网站欺骗，这一方案在安全社区被视为对抗账户劫持的最强手段之一。

该功能目前已向所有ChatGPT和Codex用户开放，用户可在账户设置中主动开启。OpenAI同时表示，该功能针对的是"高风险用户"，但并未设置任何资质审核机制——这意味着任何普通用户均可自愿升级到更高安全级别。对于在AI平台上处理敏感信息的用户而言，这一步意味着平台安全能力从单纯的口令保护向多因素、无密码认证体系的正式升级。

### 关键标签
- OpenAI联手Yubico推出物理安全钥匙登录，彻底告别密码钓鱼
- 高风险用户可退出AI训练数据，账户会话历史得到保护
- 无障碍开放：普通用户同样可主动升级安全级别

### 来源
- [OpenAI announces new advanced security for ChatGPT accounts](https://techcrunch.com/2026/04/30/openai-announces-new-advanced-security-for-chatgpt-accounts-including-a-partnership-with-yubico/) - TechCrunch
- [Introducing Advanced Account Security](https://openai.com/index/advanced-account-security/) - OpenAI
- [OpenAI adds stronger security features for users at high risk of hacks](https://www.theverge.com/ai-artificial-intelligence/921573/openai-adds-stronger-security-features-for-users-at-high-risk-of-hacks) - The Verge

## 03 Anthropic推出Claude Security：代码库漏洞扫描+自动修复，企业安全测试版全球开放

4月30日，Anthropic正式宣布Claude Security进入公开测试阶段，向全球企业用户开放。该工具基于Claude Opus 4.7模型构建，能够对企业的整个代码库进行全面扫描，识别安全漏洞、评估风险优先级并直接生成修复补丁。这是Anthropic在企业安全领域推出的首款垂直产品，标志着主流AI实验室正式将模型能力拓展至代码安全审计这一高价值场景。

Claude Security的核心工作流程分为三个阶段：扫描（Scan）、验证（Validate）和修复（Patch）。系统首先对代码库进行全量分析，识别已知漏洞类型和潜在攻击面；随后利用Opus 4.7的推理能力对发现结果进行二次验证，过滤误报；最后，由模型直接生成针对具体漏洞的修复代码，开发者可直接审查并应用。Anthropic披露，在预览阶段，Claude Security已在超过500个代码库中发现并生成了有效补丁，涵盖远程代码执行、SQL注入和身份认证绕过等多类高危漏洞。

这并非Anthropic首次进入安全领域。该公司此前曾发布"Mythos"模型——一个能够识别并利用操作系统和浏览器漏洞的强大模型，引发安全社区高度关注。与Mythos不同，Claude Security定位为防御工具，旨在帮助企业主动发现自身代码中的弱点，而非用于攻击性安全测试。Anthropic强调，Claude Security生成的修复方案经过充分推理，开发者可以看到漏洞发现的原因和修复逻辑，有助于提升整体安全意识。

Claude Security目前通过Claude Enterprise平台向企业客户提供服务，同时支持通过技术合作伙伴生态集成使用。Anthropic表示，未来计划将扫描能力扩展至容器配置、云基础设施和第三方依赖等更广泛的安全领域。该公司此前公布的Project Glasswing——与AWS、Apple、Broadcom、Cisco、Microsoft、NVIDIA等14家科技巨头联合的软件安全计划——也将成为Claude Security的重要合作伙伴落地渠道。

### 关键标签
- Claude Opus 4.7驱动代码安全扫描，预览阶段已修复500+漏洞
- Scan-Validate-Patch三阶段工作流，兼顾发现、验证与修复
- 企业安全赛道再加码，Claude Security与Project Glasswing形成生态协同

### 来源
- [Anthropic rolls out its codebase-scanning security tool for businesses](https://www.theverge.com/ai-artificial-intelligence/921198/anthropic-rolls-out-its-codebase-scanning-security-tool-for-businesses) - The Verge
- [Claude Security is now in public beta](https://claude.com/blog/claude-security-public-beta) - Anthropic
- [Anthropic's new Claude Security tool scans your codebase for flaws](https://www.zdnet.com/article/anthropic-claude-security-ai-tool-scans-codebase-for-flaws/) - ZDNET

## 快速新闻

- **04** [Musk承认Tesla目前不在研发AGI](https://www.theverge.com/ai-artificial-intelligence/921022/elon-musk-cross-openai-altman) 尽管近期推文暗示Tesla将实现AGI，Musk在法庭上明确表示Tesla目前并无相关计划。 [The Verge](https://www.theverge.com/ai-artificial-intelligence/921022/elon-musk-cross-openai-altman)

- **05** [美国议员推进AI聊天机器人年龄限制法案](https://www.theverge.com/ai-artificial-intelligence/921198/anthropic-rolls-out-its-codebase-scanning-security-tool-for-businesses) 国会正在审议新法案，要求AI聊天机器人平台对未成年用户实施年龄验证机制，科技行业对此反应不一。 [The Verge](https://www.theverge.com/ai-artificial-intelligence/921198/anthropic-rolls-out-its-codebase-scanning-security-tool-for-businesses)

- **06** [OpenAI、Anthropic与Google通过前沿模型论坛共享情报，追踪中国AI蒸馏攻击](https://www.mercurynews.com/2026/04/07/openai-anthropic-google-unite-to-combat-model-copying-in-china/) 三大AI实验室罕见联手，通过前沿模型论坛分享检测到的未授权模型蒸馏信息，已发现DeepSeek等中国公司系统性提取美国模型输出。 [Mercury News](https://www.mercurynews.com/2026/04/07/openai-anthropic-google-unite-to-combat-model-copying-in-china/)

- **07** [Anthropic封禁三家中国AI公司使用Claude](https://www.mercurynews.com/2026/04/07/openai-anthropic-google-unite-to-combat-model-copying-in-china/) Anthropic认定DeepSeek、Moonshot和MiniMax三家中国AI实验室通过蒸馏技术非法提取Claude模型能力，已全面封锁其访问权限。 [Mercury News](https://www.mercurynews.com/2026/04/07/openai-anthropic-google-unite-to-combat-model-copying-in-china/)

- **08** [Gabe Newell邮件曝光：Musk曾为Hideo Kojima争取加入OpenAI机会](https://www.theverge.com/ai-artificial-intelligence/920775/evidence-exhibits-elon-musk-sam-altman-openai-trial) 法庭证据显示，Musk曾通过Valve联合创始人Gabe Newell为游戏制作人小岛秀夫牵线，意图介绍其加入OpenAI，OpenAI最终拒绝了该提议。 [The Verge](https://www.theverge.com/ai-artificial-intelligence/920775/evidence-exhibits-elon-musk-sam-altman-openai-trial)

- **09** [Musk称xAI是"最小AI玩家"](https://www.theverge.com/ai-artificial-intelligence/921022/elon-musk-cross-openai-altman) 在法庭作证时，Musk称xAI是"最小的一家AI公司"，排在Anthropic、OpenAI、Google和中国AI模型之后。 [The Verge](https://www.theverge.com/ai-artificial-intelligence/921022/elon-musk-cross-openai-altman)

- **10** [OpenAI全产品线登陆AWS](https://openai.com/index/openai-on-aws/) OpenAI宣布GPT-5.5、Codex和Managed Agents全套产品上线亚马逊Amazon Bedrock，并披露亚马逊已承诺向OpenAI投资500亿美元。 [OpenAI](https://openai.com/index/openai-on-aws/)

- **11** [Project Glasswing启动：14家科技巨头联合保卫全球关键软件](https://www.anthropic.com/news) Anthropic牵头，与AWS、Apple、Broadcom、Cisco、CrowdStrike、Google、JPMorganChase、Linux Foundation、Microsoft、NVIDIA、Palo Alto Networks共同发起Project Glasswing，致力于保护全球关键开源软件安全。 [Anthropic](https://www.anthropic.com/news)
