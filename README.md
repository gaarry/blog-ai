# My Personal Blog

使用 Hugo + Cloudflare Pages 搭建的个人博客。

## 技术栈

- **静态网站生成器**: Hugo v0.139.x
- **托管平台**: Cloudflare Pages
- **图片处理**: Cloudflare Image Resizing
- **CI/CD**: GitHub Actions

## 功能特性

- 技术博客文章
- 摄影作品展示
- 响应式设计
- 暗黑模式支持
- RSS 订阅

## 快速开始

### 本地开发

```bash
# 安装依赖
brew install hugo

# 启动本地服务器
hugo server -D
```

访问 http://localhost:1313

### 创建新文章

```bash
hugo new posts/new-post.md
```

### 构建生产版本

```bash
hugo --gc --minify
```

## 部署

项目已配置 GitHub Actions，自动部署到 Cloudflare Pages。

1. 推送代码到 main 分支
2. GitHub Actions 自动构建和部署
3. 访问 https://your-project.pages.dev

## 配置

修改 `config.toml` 配置文件：

- 网站标题和描述
- 社交链接
- 导航菜单

## 内容管理

### 文章

在 `content/posts/` 目录创建 Markdown 文件：

```yaml
---
title: "文章标题"
date: 2026-01-31
draft: false
description: "文章描述"
tags: ["tag1", "tag2"]
categories: ["category"]
---

文章内容...
```

### 照片

在 `content/photos/` 目录创建照片文章。

## 许可证

MIT License
