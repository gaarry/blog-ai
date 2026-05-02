---
title: "OpenAI推最强账户保护、奥斯卡颁新规抵制AI演员——今日AI资讯简报"
date: 2026-05-02T08:00:00+08:00
draft: false
description: "OpenAI推出高级账户安全功能，奥斯卡新规明确禁止AI参与表演奖项，Musk v. Altman审判更多证据曝光"
coverImage: "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&q=80"
tags: ["AI资讯", "OpenAI", "Anthropic", "Academy Awards"]
categories: ["AI资讯"]
---

## 今日概览
- OpenAI推出高级账户安全功能，全面启用Passkeys和硬件安全密钥
- 奥斯卡颁布新规：AI生成内容不得参与表演类和编剧类奖项评选
- Musk v. Altman审判继续，多封早期内部邮件和证据被公开

## 01 安全 OpenAI推高级账户保护，彻底告别密码

4月30日，OpenAI正式推出"高级账户安全"（Advanced Account Security）功能，为ChatGPT和Codex账户提供顶级的账户防护。这一功能专门针对"面临较高数字攻击风险的用户"，包括政府官员、企业高管、研究人员和人权活动人士。

用户启用该功能后，将不再使用传统的邮箱+密码登录方式，而是必须使用硬件安全密钥或基于软件Passkeys完成身份验证。硬件安全密钥通过USB物理设备或NFC近场通信实现，无法被远程黑客窃取。与传统密码不同，Passkeys采用公钥加密技术，即使服务器被攻破，攻击者也无法利用泄露数据登录他人账户。

该功能还禁止通过邮件和短信验证码进行账户恢复——这正是SIM交换攻击和钓鱼邮件最常利用的突破口。用户必须注册至少两把密钥（两把硬件密钥，或一把硬件密钥+一个软件Passkeys），确保丢失后仍有备用登录手段。

OpenAI强调，这是预防性措施而非针对某次具体黑客事件的响应。"对于记者、当选官员、政治异见人士、研究人员以及特别注重安全的人士，风险更高。"OpenAI在一份声明中写道。ChatGPT和Codex已被广泛应用于处理个人对话和工作项目，承载着大量敏感信息。该功能目前已通过ChatGPT网页界面的"设置 > 安全"向用户开放，也支持直接访问chatgpt.com/advanced-account-security。

值得注意的是，OpenAI并非第一个推出此类顶配安全方案的公司。Google早在2017年就推出了"高级保护计划"（Advanced Protection Program），彼时因俄罗斯政府黑客通过钓鱼邮件攻破 Hillary Clinton竞选团队主席 John Podesta 的Gmail账户而设立。OpenAI的新方案在设计上与之类似，但扩展支持了软件Passkeys选项。

然而，这一功能也有明显的代价：由于安全等级极高，即使OpenAI本身也无法帮助用户恢复已丢失的硬件密钥或Passkeys。这意味着用户在享受最高级别保护的同时，必须承担起绝对保管密钥的责任——没有第二次机会。

### 关键标签
- 零密码认证成为AI平台安全新标配
- 高风险用户获得企业级安全保护
- Passkeys正在取代传统密码

### 来源
- [Introducing Advanced Account Security](https://openai.com/index/advanced-account-security/) - OpenAI
- [OpenAI's Advanced Account Protection Dumps Passwords for Security Keys](https://www.pcmag.com/news/openais-advanced-account-protection-dumps-passwords-for-security-keys) - PCMag

---

## 02 行业 奥斯卡新规落地：AI演员和AI编剧无缘小金人

5月1日，美国电影艺术与科学学院（Academy of Motion Picture Arts and Sciences）公布了第99届奥斯卡金像奖的完整规则修订，其中最引人关注的规定是：AI生成内容将被明确排除在表演类和编剧类奖项之外。新规则将于2027年颁奖典礼正式生效。

新规明确要求，参与表演奖评选的角色必须"在影片的法定署名中标注，且必须由人类演员在获得本人同意的情况下真实出演"才能具备评选资格。编剧类奖项的剧本同样必须为"人类创作"。如果评委对影片中生成式AI的使用存疑，学院有权"要求提供更多信息，说明使用性质和人类创作归属"。

此次规则修订的背景是AI生成"演员"事件的持续发酵。此前，一家名为Xicoia的AI公司推出了一款名为"Tilly Norwood"的AI生成"女演员"，并向多家经纪公司推广其"出演"能力。Deadline等娱乐媒体报道后引发业界广泛争议。批评者认为，所谓的"AI演员"本质上只是一个可以被随意操控的数字木偶，其"表演"完全依赖于AI模型对真实演员表演素材的训练。

新规同时允许同一演员在单届奥斯卡中因不同角色获得多次提名——这是此前一直被禁止的做法。此外，国际影片的参评标准也进一步放宽，以适应全球电影产业日益跨国的制作现状。

对于AI行业而言，奥斯卡的新规是一个明确的信号：至少在创意表达最核心的领域，监管机构选择了站队人类创作者。这对于正在尝试将AI技术推向内容创作市场的科技公司来说，是一记现实主义的重锤。

### 关键标签
- 好莱坞以规则形式确立AI与人类创作者的边界
- "AI演员"Tilly Norwood事件推动规则落地
- 创意产业开始系统性回应AI渗透

### 来源
- [AI actors and writers will be ineligible for Oscars](https://www.reuters.com/lifestyle/ai-actors-writers-will-be-ineligible-oscars-2026-05-01/) - Reuters
- [Oscars changes allow for double acting nominations while banning AI](https://www.theguardian.com/film/2026/may/01/oscars-changes-double-acting-nominations-ai) - The Guardian
- [New Oscars rules battle rise of AI](https://ew.com/new-oscars-rule-changes-battle-ai-acting-categories-tweak-11963836) - Entertainment Weekly

---

## 03 法律 Musk v. Altman审判激战：更多内部邮件浮出水面

Musk与Altman、OpenAI之间的世纪诉讼于本周进入陪审团审判阶段，更多从未公开的内部邮件和证据文件正陆续被披露。这场纠纷的核心问题是：OpenAI是否背离了其"确保AGI造福全人类"的创始使命，转而服务于商业利益。

最新披露的证据显示，2015年6月，Altman向 Musk发送了一封详细的五步计划邮件，提出创办一家AI实验室的核心框架。Altman在邮件中列出了创始团队名单，包括Musk、Bill Gates、Pierre Omidyar和Dustin Moskovitzer，并提议"技术归基金会所有，用于造福世界"，五位治理委员会成员共同决策。Musk回复简短而明确："Agree on all."

另一份引人关注的证据则涉及Valve联合创始人Gabe Newell与Musk之间的邮件往来。Newell曾尝试通过Musk安排一次SpaceX参观之旅，并为知名游戏制作人小岛秀夫（Hideo Kojima）寻求OpenAI的介绍机会。邮件还显示，Musk曾表示自己"在OpenAI的参与度目前非常有限"，并称已对OpenAI与Google/DeepMind竞争失去信心，转而希望通过特斯拉实现这一目标，同时力推Neuralink的进展。Newell后来也创办了自己的脑机接口公司Starfish。

在财务层面，Musk的财务总监Jared Birchall作证称，Musk向OpenAI提供了约60笔捐款，由Birchall负责执行。Birchall还披露，Musk在2018年停止了对OpenAI的资助——彼时正值OpenAI讨论向营利性结构转型的时期。Birchall在证词中写道，他看到OpenAI的营利性结构条款后，向同事发出疑问："对于一个以'不为了赚钱而做伟大的事'为叙事核心的组织来说，这很难与投资者专注于ROI的现实相协调。"

随着审判继续，更多证据预计将陆续公开。这场诉讼的结果可能对OpenAI未来的公司治理和AGI发展方向产生深远影响。

### 关键标签
- 2015年邮件显示Altman与Musk曾就OpenAI使命达成一致
- Gabe Newell曾为小岛秀夫牵线OpenAI
- Musk于2018年停止资助OpenAI，彼时正值转型讨论期

### 来源
- [All the evidence revealed so far in Musk v. Altman trial](https://www.theverge.com/ai-artificial-intelligence/920775/evidence-exhibits-elon-musk-sam-altman-openai-trial) - The Verge

---

## 快速新闻
- **04** Anthropic CEO Dario Amodei被美国国防部长Pete Hegseth称为"意识形态狂人"，五角大楼此前曾与Anthropic合作处理机密信息 [The Verge](https://www.theverge.com/ai-artificial-intelligence/791680/oscars-ai-rules-acting-awards)
- **05** 奥斯卡新规同时允许同一演员凭不同角色获得多次提名，这是规则的重大突破 [The Guardian](https://www.theguardian.com/film/2026/may/01/oscars-changes-double-acting-nominations-ai)
- **06** OpenAI模型、Codex和Managed Agents现已登陆AWS，企业用户可直接在AWS平台调用OpenAI服务 [OpenAI](https://openai.com/index/openai-on-aws/)
- **07** Google DeepMind发布Gemma 4，官方称其为"按算力计算最强大的开源模型"，延续Gemma系列高效路线 [Google DeepMind](https://deepmind.google/blog/)
- **08** Anthropic推出Claude Design，允许用户与Claude协作创建设计稿、原型、幻灯片和一页文档等视觉作品 [Anthropic](https://www.anthropic.com/news)
- **09** OpenAI发布开源编排规范Symphony，旨在为AI智能体协作建立统一协议标准 [OpenAI](https://openai.com/index/open-source-codex-orchestration-symphony/)
- **10** AI生成圣经内容的市场需求远超预期，多个宗教内容平台已开始集成AI辅助创作工具 [The Verge](https://www.theverge.com/ai-artificial-intelligence/791680/tilly-norwood-particle6-xicoia-eline-van-der-velden)
- **11** AI对时尚行业的影响引发讨论，有观点认为AI设计工具和趋势抓取技术导致各大品牌个性日益趋同 [The Verge](https://www.theverge.com/ai-artificial-intelligence/791680/oscars-ai-rules-acting-awards)
