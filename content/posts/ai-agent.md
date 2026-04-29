---
title: "AI-Agent"
date: 2026-04-29
tags: [blog]
---
- #Blog
	- 好问题，这几个名词确实容易混淆——它们不全是 Agent 框架。我先帮你理清它们的真实身份，再系统对比所有好用的 Agent 工具。
	- ## 一、你提到的这几个，分别是什么？
	  
	  | 名称 | 真实身份 | 一句话解释 |
	  |------|---------|-----------|
	  | **Continue** | ❌ **不是 Agent 框架** | VSCode 编程助手插件，帮你写代码、补全、解释，但它不会“主动帮你干活” |
	  | **OpenClaw** | ✅ **是 Agent 框架** | 开源 AI 代理平台，能通过自然语言指令自动执行多步骤任务，是“能干活的数字员工” |
	  | **Little Coder** | ✅ **是 Agent（专注编程）** | 专门为代码任务调优的编程代理，Aider 基准得分 45.56%，是开发者专属 |
	  | **Agent Mini** | ⚠️ **参考命名** | 搜索结果中没有找到叫“Agent Mini”的主流框架，你可能指的是 **AgentForge** 或 **AllegroAgent** 这类轻量级框架 |
	  
	  **总结：**
	- **Continue** 只是插件，**不是 Agent**
	- **OpenClaw** 是全能型 Agent，可以帮你做各种事（文件整理、浏览器、代码等）
	- **Little Coder** 是编程专用 Agent
	- 如果你说的“Agent Mini”是指轻量级框架，那就是 **AllegroAgent** 或 **AgentForge** 这类
	- ## 二、所有好用的 Agent 框架全景对比
	- ### 🔥 全能型 Agent（帮你完成日常电脑工作）
	  
	  适合你的场景：完成代码任务 + 搜索资料 + 整理文件 + 日常工作
	  
	  | 框架 | 定位 | 内存需求 | 模型支持 | 特色 | 适合场景 |
	  |------|------|---------|---------|------|---------|
	  | **OpenClaw** | 全能 AI 代理 | 2-4GB | 阿里云百炼、Ollama、OpenAI等 | 多渠道网关(Telegram/钉钉)、可插拔技能库、双模记忆 | 自动整理文件、定时任务、跨工具协同 |
	  | **xopc** | 超轻量个人助手 | ~200MB | 20+种LLM，含Ollama | CLI+WebSocket网关、Telegram/微信插件、cron定时任务 | 终端党、想在微信/Telegram里控制AI |
	  | **NanoClaw** | 安全优先轻量版 | <500MB | 主要支持Claude | Docker容器隔离、攻击面小、可审计 | 对安全敏感的场景 |
	  | **SuperAGI** | 多代理协同框架 | 4-8GB | 多种模型 | 多Agent并行执行、长期记忆、插件生态 | 复杂任务需要多个专业代理协同 |
	- ### 💻 编程专用 Agent（专注代码任务）
	  
	  如果你主要想做代码开发，这些更专业：
	  
	  | 框架 | 定位 | 启动方式 | 特色 | 适合场景 |
	  |------|------|---------|------|---------|
	  | **Little Coder** | 轻量编程代理 | CLI | Aider基准45.56%、30+技能文件 | 代码生成、调试、重构 |
	  | **Claude Code** | 商业编程助手 | CLI/IDE | 多文件推理、PR/Issue工作流、沙箱建议 | 专业软件开发，但需付费 |
	  | **Continue** | VSCode插件 | IDE内 | 代码补全、解释、调试，但**不能主动执行任务** | 编程辅助，不是Agent |
	- ### 🧠 记忆优先型 Agent（越用越聪明）
	  
	  如果你希望 AI 能记住你的偏好和历史：
	  
	  | 框架 | 记忆架构 | 记忆方式 | 特色 |
	  |------|---------|---------|------|
	  | **Letta (原MemGPT)** | 三 tier记忆(核心/回忆/归档) | Agent自编辑记忆 | OS式内存管理、视觉化调试 |
	  | **Hindsight** | 四路并行检索 | 系统被动提取 | 91.4% LongMemEval得分、MCP原生 |
	- ### 🪶 极简/学习型 Agent（代码量小、易理解）
	  
	  如果你喜欢折腾、想理解原理：
	  
	  | 框架 | 核心代码量 | 语言 | 特色 |
	  |------|-----------|------|------|
	  | **Nanobot** | 小型Python代码库 | Python | 可在几小时内通读全部代码 |
	  | **AllegroAgent** | <1000行（核心） | Python | 零重型依赖、仅requests运行时 |
	  | **AgentForge** | 模块化框架 | Python | YAML声明式配置、开发时间减少62% |
	- ### 🔧 嵌入式/边缘设备 Agent（极低资源）
	  
	  如果你在树莓派等设备上运行：
	  
	  | 框架 | 语言 | 特色 |
	  |------|------|------|
	  | **DragonScale** | Go | MemGPT级tiered内存、DAG并行工具执行、libSQL向量存储 |
	- ## 三、针对你的需求的推荐
	  
	  根据你的描述：**代码任务 + 搜索资料 + 整理文件 + 日常工作 + 无独显 + 10GB以内模型**
	- ### 🥇 首选推荐：OpenClaw + Qwen2.5-Coder 7B (CPU运行)
	  
	  **为什么最适合你：**
	- OpenClaw 是“能干活的AI”，不是只会聊天——你可以直接说“帮我整理downloads文件夹”、“搜索Python异步编程的资料并汇总”
	- 支持对接本地 Ollama 运行的 Qwen2.5-Coder 7B（4.5GB），完全无独显可用
	- 有 Web 控制台和 Telegram/钉钉多渠道，随时随地指挥
	- 2026年最新版新增 60 多项安全加固，不用担心乱执行命令
	  
	  **安装方式（WSL Ubuntu）：**
	  ```bash
	  # 1. 安装 Node.js 22+
	  curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
	  sudo apt install -y nodejs
	  
	  # 2. 一键安装 OpenClaw
	  curl -fsSL https://openclaw.ai/install.sh | bash
	  
	  # 3. 运行配置向导（模型选 Ollama）
	  openclaw onboard
	  
	  # 4. 启动网关
	  openclaw gateway start
	  ```
	  浏览器打开 `http://localhost:18789` 即可使用 Web 控制台
	- ### 🥈 备选推荐：xopc（终端党/IM控制）
	  
	  如果你更喜欢在终端里操作，或者想通过微信/Telegram 控制 AI：
	- 单命令安装：`npm install -g @xopcai/xopc`
	- 支持 20+ 种模型（含 Ollama），内置文件搜索/编辑、网页搜索工具
	- 有 cron 定时任务，可以设置“每天早上8点汇总新闻”
	- ### 🥉 如果你想先从小白的开始：AllegroAgent
	  
	  如果你只是想先理解 Agent 怎么工作，不想一上来就面对复杂配置：
	  ```bash
	  pip install allegro-agent
	  ```
	  然后写几行 Python 就能跑起一个有工具调用能力的 Agent
	- ## 四、一句话总结
	  
	  | 你想要 | 选这个 |
	  |--------|--------|
	  | **AI 主动帮你干活（整理文件、搜索、写代码）** | **OpenClaw** |
	  | **终端/微信里控制 AI** | **xopc** |
	  | **只想写代码时辅助** | **Continue**（不是 Agent） |
	  | **研究原理、自己造轮子** | **AllegroAgent / Nanobot** |
	  | **需要超强记忆能力** | **Hindsight**（作为记忆层接入其他框架）|
	  
	  **最终建议：** 先装 **OpenClaw** + 本地 Ollama 跑 **Qwen2.5-Coder 7B**，这是目前最能实现“帮我干活”这个目标的组合，且完全满足你“无独显、10GB内”的限制。配置过程中有任何问题随时问我。
-
-