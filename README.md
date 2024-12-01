# Cauly Bot  

**Cauly Bot** is a Discord bot designed for Minecraft players, supporting server status checking, player skin downloads, and module management functions.  

Cauly Bot 是一款專為 Minecraft 玩家設計的 Discord 機器人，支援查詢伺服器狀態、玩家皮膚下載，以及模組管理功能。

---

## Features  

### Public Commands  
1. **`/bedrockserver <server IP>`**  
   Check the status of a Bedrock Minecraft server.  

2. **`/javaserver <server IP>`**  
   Check the status of a Java Minecraft server.  

3. **`/player_skin <player name>`**  
   Check a player's Minecraft skin and generate a download link.  

### Authorized User Commands  
Only authorized users can use the following commands:  
1. **`!load <module name>`**  
   Dynamically load the specified module.  

2. **`!unload <module name>`**  
   Unload the specified module.  

3. **`!reload <module name>`**  
   Reload the specified module.  

---

## Installation Guide  

### 1. System Requirements  
- **Python**: Version 3.8 or above.  
- **discord.py module**: This is the Python module required to interact with Discord's API. Run `pip install discord.py` in the terminal.  
- **Discord Bot Token**: You need to create an application and obtain your Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications).  

### 2.File Configuration

```
cauly-bot/
├── main.py           # Main program, responsible for starting the bot
├── cogs/             # Folder for functional modules
│   ├── java.py       # Module for querying Java server status
│   ├── bedrock.py    # Module for querying Bedrock server status
│   ├── skin.py       # Module for querying player skins
```

### 3. Change Variables  
In your code, replace `your_user_id` with the Discord user ID of the authorized user, and replace `your_token` with your Discord bot token.  

### 4. Running the Program  
Run `main.py` to start the bot.  

---

## License  

This project uses the MIT license.  
Please refer to the [LICENSE](LICENSE) file for more details.  

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
- **discord.py 模組**：這是與 Discord API 進行互動所需的 Python 模組。可以在終端機中執行 `pip install discord.py`  
- **Discord Bot Token**：需在 [Discord 開發者](https://discord.com/developers/applications) 中創建應用並獲取。  

### 2.檔案配置

```
cauly-bot/
├── main.py           # 主程式，負責啟動機器人
├── cogs/             # 功能模組資料夾
│   ├── java.py       # 查詢 Java 伺服器狀態的模組
│   ├── bedrock.py    # 查詢 Bedrock 伺服器狀態的模組
│   ├── skin.py       # 查詢玩家皮膚模組
```

### 3. 改變變數  
在你的`main.py`中，將 `your_user_id` 替換成授權使用者的 Discord 用戶 ID，並將 `your_token` 替換成你的 Discord 機器人 Token。  

### 4. 執行程式  
執行 `main.py` 來啟動機器人。  

---

## 許可證  

此專案使用 MIT 許可證。  
請參閱 [LICENSE](LICENSE) 文件了解更多資訊。  
