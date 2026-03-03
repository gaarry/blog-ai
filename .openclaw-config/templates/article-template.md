# 博客文章模板

## 文件命名规范

```
content/posts/YYYY-MM-DD-slug.md
```

例如：`content/posts/2026-03-02-ai-digest.md`

---

## 完整模板

```markdown
---
title: "文章标题"
date: 2026-03-02T20:00:00+08:00
draft: false
description: "第一条要点；第二条要点；第三条要点"
coverImage: "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&q=80"
tags: ["AI", "标签2", "标签3"]
categories: ["AI资讯"]
---

<div class="article-section">
<h2><span class="article-num">01</span>第一篇文章标题</h2>

<p>正文第一段...</p>

<p>正文第二段...</p>

<p>正文第三段...</p>

<div class="key-tags">
<span class="key-tag">关键要点1</span>
<span class="key-tag">关键要点2</span>
<span class="key-tag">关键要点3</span>
</div>

<div class="sources-list">
<div class="sources-label">来源</div>
<a href="https://example.com/article1" class="source-item" target="_blank"><span class="source-title">文章标题1</span><span class="source-domain">example.com</span></a>
<a href="https://example.com/article2" class="source-item" target="_blank"><span class="source-title">文章标题2</span><span class="source-domain">example.com</span></a>
<a href="https://example.com/article3" class="source-item" target="_blank"><span class="source-title">文章标题3</span><span class="source-domain">example.com</span></a>
</div>
</div>

<div class="article-section">
<h2><span class="article-num">02</span>第二篇文章标题</h2>

<p>正文第一段...</p>

<p>正文第二段...</p>

<div class="key-tags">
<span class="key-tag">关键要点1</span>
<span class="key-tag">关键要点2</span>
</div>

<div class="sources-list">
<div class="sources-label">来源</div>
<a href="https://example.com/article" class="source-item" target="_blank"><span class="source-title">文章标题</span><span class="source-domain">example.com</span></a>
</div>
</div>

<div class="article-section">
<h2><span class="article-num">03</span>第三篇文章标题</h2>

<p>正文内容...</p>

<div class="key-tags">
<span class="key-tag">关键要点1</span>
<span class="key-tag">关键要点2</span>
<span class="key-tag">关键要点3</span>
</div>

<div class="sources-list">
<div class="sources-label">来源</div>
<a href="https://example.com/article" class="source-item" target="_blank"><span class="source-title">文章标题</span><span class="source-domain">example.com</span></a>
</div>
</div>

<div class="quick-news-section">
<div class="quick-news-item"><span class="paper-num">04</span><div class="quick-news-body"><p><strong>快讯标题1</strong> 快讯内容... <a href="https://example.com" class="qn-source" target="_blank"><span class="source-domain">example.com</span></a></p></div></div>
<div class="quick-news-item"><span class="paper-num">05</span><div class="quick-news-body"><p><strong>快讯标题2</strong> 快讯内容... <a href="https://example.com" class="qn-source" target="_blank"><span class="source-domain">example.com</span></a></p></div></div>
<div class="quick-news-item"><span class="paper-num">06</span><div class="quick-news-body"><p><strong>快讯标题3</strong> 快讯内容... <a href="https://example.com" class="qn-source" target="_blank"><span class="source-domain">example.com</span></a></p></div></div>
</div>
```

---

## 字段说明

### Front Matter（文章头部）

| 字段 | 说明 | 示例 |
|------|------|------|
| `title` | 文章标题 | `"OpenAI签五角大楼合同，Anthropic被列为供应链风险"` |
| `date` | 发布日期和时间 | `2026-03-02T20:00:00+08:00` |
| `draft` | 是否为草稿 | `false`（发布）/ `true`（草稿） |
| `description` | 文章概览（用分号分隔） | `"要点1；要点2；要点3"` |
| `coverImage` | 封面图片URL | `"https://images.unsplash.com/..."` |
| `tags` | 标签列表 | `["AI", "OpenAI", "Anthropic"]` |
| `categories` | 分类列表 | `["AI资讯"]` |

### HTML 结构说明

#### 1. 文章区块（article-section）

用于包裹每一篇独立的文章内容：

```html
<div class="article-section">
  <h2><span class="article-num">01</span>文章标题</h2>
  <p>正文...</p>
  <div class="key-tags">...</div>
  <div class="sources-list">...</div>
</div>
```

**要点：**
- 每篇文章必须用 `<div class="article-section">` 包裹
- 标题使用 `<h2>` + `<span class="article-num">编号</span>`
- 编号格式：01, 02, 03...（两位数字）

#### 2. 文章编号（article-num）

```html
<h2><span class="article-num">01</span>文章标题</h2>
```

**样式：**
- 大号数字，棕色（#b87848）
- 与标题在同一行左对齐

#### 3. 关键要点标签（key-tags）

```html
<div class="key-tags">
<span class="key-tag">关键要点1</span>
<span class="key-tag">关键要点2</span>
<span class="key-tag">关键要点3</span>
</div>
```

**样式：**
- 浅绿色背景（#f0fdf4）
- 绿色边框（#d1fae5）
- 圆角胶囊形状

#### 4. 来源列表（sources-list）

```html
<div class="sources-list">
<div class="sources-label">来源</div>
<a href="URL" class="source-item" target="_blank">
  <span class="source-title">文章标题</span>
  <span class="source-domain">domain.com</span>
</a>
</div>
```

**要点：**
- `sources-label` 显示"来源"标签
- 每个来源包含标题和域名
- 所有链接使用 `target="_blank"` 新窗口打开

#### 5. 快讯区块（quick-news-section）

用于简短新闻条目：

```html
<div class="quick-news-section">
<div class="quick-news-item">
  <span class="paper-num">04</span>
  <div class="quick-news-body">
    <p><strong>标题</strong> 内容...
    <a href="URL" class="qn-source" target="_blank">
      <span class="source-domain">domain.com</span>
    </a></p>
  </div>
</div>
</div>
```

**要点：**
- 快讯编号接续前面的文章编号
- 标题使用 `<strong>` 加粗
- 来源链接使用 `qn-source` 类

---

## 写作规范

### 1. 段落结构

- 每段用 `<p>` 标签包裹
- 段落之间自动有间距
- 避免使用 `<br>` 换行

### 2. 强调文本

```html
<p>这是<strong>重点内容</strong>的示例。</p>
```

### 3. 链接

文章正文中的链接：
```html
<a href="https://example.com">链接文字</a>
```

### 4. 引用

```html
<blockquote>
<p>引用的内容...</p>
</blockquote>
```

### 5. 列表

无序列表：
```html
<ul>
<li>列表项1</li>
<li>列表项2</li>
</ul>
```

有序列表：
```html
<ol>
<li>第一项</li>
<li>第二项</li>
</ol>
```

---

## 图片使用

### 文章内图片

```html
<figure class="article-cover">
  <img src="/images/2026-03-02-example.jpg" alt="图片描述" loading="lazy">
  <figcaption>图片说明（可选）</figcaption>
</figure>
```

### 封面图片来源

推荐使用 Unsplash：
- URL 格式：`https://images.unsplash.com/photo-[ID]?w=800&q=80`
- 建议尺寸：宽度 800px
- 质量参数：q=80

---

## 快速开始

### 1. 复制模板

```bash
cp BLOG_TEMPLATE.md content/posts/YYYY-MM-DD-new-post.md
```

### 2. 修改 Front Matter

- 更新 `title`、`date`、`description`
- 选择合适的 `tags` 和 `categories`
- 设置 `coverImage`

### 3. 填写内容

- 按照模板结构填写文章内容
- 每篇文章使用 `<div class="article-section">` 包裹
- 添加关键要点（key-tags）
- 添加来源链接（sources-list）

### 4. 预览

```bash
hugo server --buildDrafts
```

访问：http://localhost:1313/

### 5. 发布

```bash
# 设置 draft: false
hugo --cleanDestinationDir
```

---

## 注意事项

### ✅ 必须做的

1. 每篇文章必须用 `<div class="article-section">` 包裹
2. 标题必须包含 `<span class="article-num">编号</span>`
3. 编号必须是两位数字格式（01, 02, 03...）
4. 所有外部链接必须添加 `target="_blank"`
5. description 字段用分号（；）分隔要点

### ❌ 不要做的

1. 不要在 article-section 外直接写内容
2. 不要忘记关闭 HTML 标签
3. 不要使用内联样式（style=""）
4. 不要使用 `<div class="container">`（模板已处理）
5. 不要使用 Markdown 标题（# ## ###），使用 HTML 标签

---

## 示例文章

参考现有文章：
- `content/posts/2026-03-02-ai-digest.md`

---

## 常见问题

### Q: 如何添加更多文章？

A: 继续添加 `<div class="article-section">` 区块，编号递增。

### Q: 快讯从哪个编号开始？

A: 接续前面的文章编号。例如前面有3篇文章（01-03），快讯从04开始。

### Q: 如何修改样式？

A: 不要在文章中修改样式，所有样式在 `static/css/main.css` 中统一管理。

### Q: 如何添加封面图？

A: 在 Front Matter 中设置 `coverImage` 字段，使用 Unsplash 或其他图片 URL。

---

## 更新日志

- 2026-03-03: 创建初始模板
- 基于参考网站 https://ai-digest.liziran.com/zh/ 设计
