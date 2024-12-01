# Cauly Bot

Cauly Bot 是一款專為 Minecraft 玩家設計的 Discord 機器人，支援查詢伺服器狀態、玩家皮膚下載，以及模組管理功能。

---

## 功能概述

### 公開指令
1. **`/bedrockserver <伺服器 IP>`**  
   查詢 Bedrock Minecraft 伺服器的當前狀態。

2. **`/javaserver <伺服器 IP>`**  
   查詢 Java Minecraft 伺服器的當前狀態。

3. **`/player_skin <玩家名稱>`**  
   查詢玩家的 Minecraft 皮膚，並生成下載連結。

### 授權用戶指令
僅授權用戶可使用以下命令：
1. **`!load <模組名>`**  
   動態載入指定模組。

2. **`!unload <模組名>`**  
   卸載指定模組。

3. **`!reload <模組名>`**  
   重新載入指定模組。

---

## 安裝指南

### 1. 系統需求
- **Python**：3.8 或以上版本
- **discord.py 模組**：這是與 Discord API 進行互動所需的 Python 模組。可以終端機中執行```pip install discord.py```
- **Discord Bot Token**：需在 [Discord 開發者門戶](https://discord.com/developers/applications) 中創建應用並獲取。

### 2. 改變變數
在你的程式碼中，將your_user_id 替換成授權使用者的 Discord 用戶 ID，並將 your_token 替換成你的 Discord 機器人 Token。

### 3. 執行程式
執行main.py

---
## 許可證
### 此專案使用 MIT 許可證
你可以自由使用和修改程式碼，但請保留許可證聲明。


