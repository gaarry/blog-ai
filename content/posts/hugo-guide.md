---
title: "使用 Hugo 搭建个人博客完整指南"
date: 2026-01-30
draft: false
description: "详细介绍如何从零开始使用 Hugo 搭建个人博客，包括安装、配置、主题定制和部署。"
tags: ["Hugo", "静态网站", "博客", "教程"]
categories: ["技术"]
coverImage: "/images/hugo-cover.jpg"
---

## 为什么选择 Hugo

[Hugo](https://gohugo.io/) 是目前最流行的静态网站生成器之一，它具有以下优点：

- **速度快** - 几毫秒内生成数千页
- **易安装** - 单二进制文件，无需依赖
- **主题丰富** - 数百个免费主题可选
- **功能强大** - 内置模板、分类、标签等功能

## 安装 Hugo

### macOS

使用 Homebrew 安装：

```bash
brew install hugo
```

### Windows

使用 Chocolatey：

```bash
choco install hugo-extended -y
```

### Linux

```bash
wget https://github.com/gohugoio/hugo/releases/download/v0.139.0/hugo_extended_0.139.0_linux-amd64.tar.gz
tar -xzf hugo_extended_0.139.0_linux-amd64.tar.gz
sudo mv hugo /usr/local/bin/
```

## 创建新站点

```bash
hugo new site my-blog
cd my-blog
```

## 添加主题

```bash
git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
echo "theme = 'ananke'" >> config.toml
```

## 创建文章

```bash
hugo new posts/my-first-post.md
```

## 启动本地服务器

```bash
hugo server -D
```

访问 http://localhost:1313 即可预览。

## 部署到 Cloudflare Pages

1. 将项目推送到 GitHub
2. 在 Cloudflare Pages 中连接你的 GitHub 仓库
3. 配置构建设置：
   - 构建命令: `hugo --gc --minify`
   - 输出目录: `public`
4. 点击"部署"

## 结语

Hugo 是一个非常强大且易用的静态网站生成器。无论你是技术博主、摄影师还是普通写作者，Hugo 都能满足你的需求。

快开始你的 Hugo 之旅吧！
