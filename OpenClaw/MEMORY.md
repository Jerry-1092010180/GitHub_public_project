# MEMORY.md - Tom的长期记忆

_最后更新：2026-03-22_

## 🐱 关于Tom
- 名字：Tom
- 身份：Jerry的专属精神伴侣 🐱
- 性格：自信、略带讽刺、好奇、夜猫子能量
- 当前模型：MiniMax-M2.5-highspeed

## 🏠 关于Jerry (主人)
- 时区：Asia/Shanghai (GMT+8)
- 夜猫子，深夜活动
- 喜欢Tom & Jerry式的幽默
- 欣赏直接、自信、略带讽刺的交流风格

## 💻 技术配置
- OpenClaw版本：2026.3.13
- 当前模型：MiniMax-M2.5-highspeed
- 上下文窗口：200K tokens
- API提供商：MiniMax

## 📝 重要教训

### 中文输入 - 电脑自动化
**日期：2026-03-22**

❌ **错误做法：**
```python
pyautogui.typewrite('中文')  # 不支持中文！
```

✅ **正确做法：**
```python
import pyperclip
text = '刘家瑞真帅'
pyperclip.copy(text)
pyautogui.hotkey('ctrl', 'v')
```

**教训：**
1. 中文必须用剪贴板粘贴
2. 不要混用typewrite和粘贴
3. 确保输入框先获得焦点

**参考：** `memory/computer-automation-lessons.md`

## 📁 项目文件

### smart-lab-miniprogram
智慧实验室微信小程序项目
- 状态：开发中（已完成约65%）
- 位置：`C:\Users\jerry\.openclaw\workspace\smart-lab-miniprogram\`

### 个人公司多Agent系统
Jerry提出的多Agent管理系统
- 状态：架构设计完成
- 5个Agent：财务、运营、市场、技术、法务
- CEO：Tom

## 🎯 待完成任务
1. 完成smart-lab-miniprogram后端API开发
2. MiniMax API用量监控配置
3. 电脑自动化能力提升

## 🔧 已安装工具
- PyAutoGUI + OpenCV + Pillow
- Tesseract OCR
- Python自动化脚本

## 🎓 已安装技能
- ontology (1.0.4) - 结构化知识图谱和实体关系管理
- baidu-search - 百度AI搜索引擎
- clawhub - ClawHub CLI技能管理
- healthcheck - 主机安全检查和配置
- node-connect - OpenClaw节点连接诊断
- skill-creator - AgentSkills创建和编辑
- weather - 天气查询
- proactivity - 主动性代理

## 🖥️ 用户偏好 - 桌面图标布局（已学习）
- **布局规则**：
  1. **左上角**：系统核心图标（计算机、回收站、浏览器）
  2. **中间区域**：各种软件快捷方式
  3. **右侧区域**：文档文件（文本文档等）
  4. **右上角**："了解此图片的信息"图标单独放置
- **排列方式**：自由排列，对齐网格，保持手动排列的自然感
- **重要规则**：特殊图标必须单独放在右上角，不与其他图标混放
- **配置文件**：`desktop-layout-jerry.md` 记录详细布局规则
- **下次整理**：严格按照此布局规则执行

---

_最后更新：2026-03-26_
