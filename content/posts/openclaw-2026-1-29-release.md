---
title: "OpenClaw 2026.1.29 版本发布：品牌重塑与多项功能升级"
date: 2026-01-31
draft: false
description: "OpenClaw 发布最新稳定版本，完成品牌重命名并带来大量新功能"
coverImage: "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&q=80"
tags: ["OpenClaw", "AI Agent", "Chatbot", "Open Source"]
categories: ["AI"]
---

OpenClaw 是一款开源的 AI 助手框架，支持跨平台消息传递，已发布 2026.1.29 稳定版本。本次更新带来了重大品牌重塑和多项功能升级。

## 项目简介

OpenClaw = CLAW + TARDIS — 因为每只太空龙虾都需要一台时空机器。

这是一个开源项目，连接 WhatsApp、Telegram、Discord、iMessage 等多个平台到 AI 编程代理（如 Pi）。通过一个统一的 Gateway，实现多平台消息的统一管理。

## 品牌重塑

本次更新最显著的变化是品牌重塑：

- npm 包/CLI 重命名为 **openclaw**
- 添加了 openclaw 兼容性适配层
- 扩展模块移至 `@openclaw/*` 作用域

## 核心功能更新

### Gateway 改进
- 新增钩子令牌通过查询参数时的警告
- 添加危险控制 UI 设备身份验证绕过标志
- 增强网络安全警告机制

### Telegram 增强
- 支持媒体发送的标题参数
- 支持插件 sendPayload channelData（媒体/按钮）
- 支持编辑已发送的消息
- 支持引用回复
- 新增贴纸接收/发送功能（带视觉缓存）
- 新增静默发送标志（禁用通知）

### Discord 改进
- 添加可配置的特殊网关意图，用于在线状态/成员管理

### 浏览器控制优化
- 通过 gateway/node 路由浏览器控制
- 支持通过节点代理路由 browser.request
- 支持代理超时处理

### 开发工具
- 添加按发送者分组工具策略
- 改进 cron 工具文档
- 内存搜索支持额外路径索引

## 安全性增强

- **移除危险模式**：网关认证模式 "none" 已被移除，现在网关要求 token/password
- 新增安全警告机制
- 改进 macOS 安全性

## 多平台支持

OpenClaw 目前支持：
- 📱 WhatsApp（通过 Baileys）
- ✈️ Telegram Bot
- 🎮 Discord Bot
- 💬 iMessage（macOS）
- 🧩 Mattermost（插件）

## 快速开始

```bash
# 安装
npm install -g openclaw@latest

# 初始化
openclaw onboard --install-daemon

# 登录渠道
openclaw channels login

# 启动网关
openclaw gateway --port 18789
```

## 社区与贡献

OpenClaw 是一个活跃的开源项目，拥有众多贡献者。项目托管在 GitHub 上，欢迎社区贡献。

创始人 Peter Steinberger（@steipete）表示："我们都在玩自己的提示词。"

*来源：[GitHub Releases](https://github.com/openclaw/openclaw/releases/tag/v2026.1.29)*
