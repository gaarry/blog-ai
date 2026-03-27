---
title: "Anthropic叫板五角大楼，谷歌内存压缩算法引爆芯片板块"
date: 2026-03-27T08:00:00+08:00
draft: false
description: "Anthropic起诉国防部，谷歌TurboQuant压缩内存6倍"
coverImage: "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&q=80"
tags: ["AI", "军事", "政策", "大模型"]
categories: ["AI资讯"]
---

## 今日概览
- Anthropic正式起诉国防部，要求撤销"供应链风险"定性
- 谷歌发布TurboQuant算法，AI内存占用压缩6倍，芯片股集体暴跌
- OpenAI洽谈Helion核聚变电力，2035年目标50GW供电规模

## 01 军事 AI供应商身份争议，Anthropic起诉国防部

美国AI安全公司Anthropic正在对特朗普政府发起一场重大法律挑战。当地时间3月25日，Anthropic与美国国防部之间的诉讼在加州北区联邦地区法院开庭审理，法官Rita Lin听取了就初步禁令请求的口头辩论。这是Anthropic上月被五角大楼列为"军事供应链风险"后，首次在法庭上正面回击这一认定。

2月27日，特朗普总统下令所有联邦机构停止使用Anthropic的AI服务，理由是"国家安全风险"。虽然政府给了各机构六个月缓冲期逐步移除系统，但这一决定对Anthropic的商业前景构成直接冲击——联邦合同曾是该公司重要收入来源之一。Anthropic认为这一认定缺乏事实依据，要求法院颁布初步禁令，阻止该认定的执行。Wired报道称，法官在庭审中表示，五角大楼针对Anthropic的举措"令人深感不安"（troubling），并对政府方的论据提出质疑。庭审结束后，法官表示将在"未来数日内"作出裁决。

这一案件的意义远超个案本身。如果Anthropic胜诉，将成为法院首次介入AI供应商政府准入问题的标志性判例，为整个AI行业在军事应用领域的合规边界设立重要先例。《Lawfare》编辑Molly Roberts在庭审期间于Bluesky平台进行了实时追踪，指出这场诉讼的核心在于：政府是否有权基于主观判断将一家合法AI公司排除在政府采购之外，而无需提供具体证据。目前判决结果仍悬而未决，但行业普遍认为，无论结果如何都将对AI公司与政府的关系产生深远影响。

### 关键标签
- AI供应商政府准入
- 军事供应链风险认定
- 联邦政府AI采购政策

### 来源
- [Pentagon's 'Attempt to Cripple' Anthropic Is Troubling, Judge Says](https://www.wired.com/story/pentagon-attempt-to-cripple-anthropic/) - Wired
- [Anthropic and the Pentagon just finished sparring in court](https://www.theverge.com/ai-artificial-intelligence/891377/anthropic-dod-lawsuit) - The Verge
- [Anthropic Denies It Could Sabotage AI Tools During War](https://www.wired.com/story/anthropic-denies-sabotage-ai-tools-war-claude/) - Wired

## 02 技术 谷歌TurboQuant发布：AI内存占用压缩6倍，存储芯片股崩盘

谷歌研究团队于3月25日正式发布TurboQuant算法，这是一种针对大语言模型的极端压缩技术，能够在不损失任何精度的前提下，将AI模型的内存占用减少至原来的六分之一。该技术通过将数据量化至3-bit实现显著压缩，消息发布当天即引发美股存储芯片板块剧烈震荡：美光科技（Micron）下跌4%，西部数据下跌4.4%，希捷下跌5.6%，闪迪（SanDisk）重挫6.5%，整体市值蒸发数百亿美元。

传统观点认为，AI计算需求的高速增长将持续推动对高带宽内存（HBM）和存储设备的需求。然而，摩根士丹利在随后的分析报告中指出，TurboQuant这类压缩技术的普及实际上可能"加速更密集AI应用的部署"，而非减少总体芯片需求——因为更低的内存成本使得更多边缘设备和消费级硬件能够运行大型模型，从整体上扩大了AI芯片市场。该算法主要针对LLM推理阶段的KV缓存（Key-Value Cache）进行优化，这是大模型在生成文本时存储中间计算结果的核心组件，通常占用大量内存资源。

谷歌在官方博客中表示，TurboQuant的研发历时超过一年，其核心创新在于"数据驱动的异常值感知量化"方法，能够智能识别并保留对模型精度影响最大的关键数据节点，同时对次要信息进行深度压缩。目前该技术已开始在谷歌内部的部分Gemini模型部署中测试，计划逐步向外部开发者开放API接口。对于整个AI行业而言，这标志着模型压缩技术从"可用可不用的优化选项"正式成为"控制成本的核心基础设施"。

### 关键标签
- 大模型推理优化
- 存储芯片市场影响
- 模型压缩技术

### 来源
- [Google's TurboQuant algorithm aims to slash AI memory usage](https://www.theverge.com/2026/3/25) - The Verge
- [Google's TurboQuant AI-compression algorithm can reduce LLM memory usage by 6x](https://arstechnica.com/) - Ars Technica
- [Google TurboQuant leads to more intense computing rather than dimming demand](https://news.futunn.com/post/70679648) - Futunn

## 03 商业 OpenAI锁定核聚变能源：2035年目标50GW供电

OpenAI正与核聚变初创公司Helion Energy进行深入谈判，计划采购其未来核聚变发电产能，以支撑AI基础设施不断膨胀的电力需求。3月23日，OpenAI首席执行官Sam Altman确认，由于Helion正在与OpenAI"开展大规模合作"，他将辞去Helion董事会主席一职，以避免利益冲突。Altman此前个人投资了Helion，此次辞职能使两家公司更顺畅地推进合作谈判。

根据Axios及财联社披露的协议细节，OpenAI的目标极为宏大：到2030年获得约50亿瓦（5GW）电力供应，并在2035年扩大至500亿瓦（50GW）规模。作为参考，5GW约相当于5座大型核电站的装机容量，而50GW则接近英国全国当前的总发电能力。Helion每座聚变反应堆设计发电能力为50MW，这意味着要在2030年前实现5GW目标，Helion需要部署约100座反应堆；到2035年实现50GW，则需累计部署约10000座。科学界普遍认为，尽管核聚变被视为能源领域的"圣杯"，但实现商业化可控核聚变仍有重大技术障碍待克服。

这一合作背后反映的是AI行业面临的能源瓶颈问题。随着数据中心规模不断扩大，电力供应已成为制约AI公司扩张速度的关键因素之一。微软、谷歌和亚马逊等科技巨头均在积极探索小型模块化核反应堆（SMR）和清洁能源项目，以锁定长期电力供应。OpenAI押注核聚变，虽然从时间表上看充满不确定性，但若技术取得突破，AI的清洁能源需求将获得根本性解决。目前Helion已承诺于2028年实现净能量增益发电，但许多分析师认为这一目标过于乐观。

### 关键标签
- AI能源基础设施
- 核聚变商业化
- 数据中心电力需求

### 来源
- [OpenAI洽谈购买核聚变电力](https://new.qq.com/rain/a/20260323A066TZ00) - 腾讯新闻
- [OpenAI与聚变初创公司Helion洽谈大型能源交易](https://so.html5.qq.com/page/real/search_news?docid=70000021_24669c196c998752) - 财联社
- [OpenAI Enters Its Focus Era by Killing Sora](https://www.wired.com/story/openai-shuts-down-sora-ipo-ai-superapp/) - Wired

## 快速新闻

- **04** [苹果与谷歌达成AI协议：Gemini将用于训练设备端小型模型] 据The Information报道，苹果与谷歌的协议允许苹果"完全访问"谷歌数据中心的Gemini模型。苹果计划利用Gemini蒸馏出可在iPhone等设备本地运行的小型"学生"模型，降低对云端计算的依赖。[The Verge](https://www.theverge.com/2026/3/25)

- **05** [英特尔发布Arc Pro B70台式GPU：瞄准AI推理市场，起售价949美元] 英特尔正式推出Arc Pro B70"Big Battlemage"桌面GPU，配备32GB GDDR6显存和32个Xe2核心，专为AI推理任务设计。合作伙伴定制版本价格各异，但英特尔公版设计定价949美元。[The Verge](https://www.theverge.com/2026/3/25)

- **06** [欧盟电池新规阻碍Meta智能眼镜欧洲扩张计划] Meta原计划在欧洲推出带显示屏的Ray-Ban智能眼镜，但受制于欧盟要求2027年后电子设备必须配备可拆卸电池的规定，被迫暂停该地区的上市计划。加上此前的AI法规限制，欧洲市场拓展面临双重阻力。[The Verge](https://www.theverge.com/2026/3/24)

- **07** [英伟达CEO称"AGI已实现"：定义模糊还是真正突破？] 英伟达CEO黄仁勋在公开场合表示通用人工智能（AGI）已经实现，但业界普遍质疑这一论断的准确性——因为科学界对AGI本身就没有统一定义，也没有客观的评估标准能够验证这一声明。[The Verge](https://www.theverge.com/ai-artificial-intelligence/899086/jensen-huang-nvidia-agi)

- **08** [维基百科正式禁止AI生成的编辑内容] 维基百科管理员报告称，近月来由大语言模型引发的问题编辑数量大幅上升，编辑团队已不堪重负。维基百科因此宣布全面禁止AI生成的编辑内容，并要求所有提交内容必须由人工编写和审核。[404 Media](https://www.404media.co/wikipedia-bans-ai-generated-content/)

- **09** [Beehiiv推出MCP集成：AI可直接草拟和发送Newsletter] 邮件订阅平台Beehiiv推出Model Context Protocol（MCP）beta测试，允许用户通过ChatGPT或Claude等AI助手直接协助Newsletter撰写、订阅者列表分析，以及定向发送优惠活动。该功能为付费用户专属，展示了AI与内容平台深度整合的新路径。[The Verge](https://www.theverge.com/2026/3/24)

- **10** [英伟达GTC 2026召开：Blackwell Ultra GPU全面亮相] 英伟达年度GPU技术大会（GTC）于3月在硅谷召开，Blackwell Ultra系列GPU正式全面推出，官方数据显示该系列在代理式AI推理任务中实现50倍性能提升和35倍成本降低。英伟达同时宣布与罗氏、ABB等工业巨头的AI工厂合作计划。[NVIDIA Blog](https://blogs.nvidia.com/blog/gtc-2026-news/)

- **11** [Bernie Sanders提出新AI安全法案：拟暂停新建数据中心] 参议员Bernie Sanders提出新立法，要求在联邦政府完成AI数据中心能源使用和安全影响全面评估前，暂停批准新的数据中心建设项目。法案引发了科技行业强烈反对，批评者称其将扼杀AI创新和就业增长。[Wired](https://www.wired.com/story/new-bernie-sanders-ai-safety-bill-would-halt-data-center-construction/)
