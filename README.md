# Discord Image Automation Bot (Python)

This project is a **Discord bot built with Python** using the `discord.py` library.  
It demonstrates **automated image delivery**, message rate control, and basic error handling within Discord servers.

The bot allows a user to send multiple images to a specified channel with a configurable delay between each message.

> ⚠️ **Important Notice**  
> This project is intended for **educational purposes and controlled environments only**.  
> Excessive message or media automation may violate **Discord’s Terms of Service**.  
> Always use this bot responsibly and only in servers where you have explicit permission.

---

## Overview

This bot showcases:
- Media message automation
- Channel-targeted message delivery
- Delay-based rate limiting
- Error handling for failed sends
- Discord API intent configuration

It is suitable for learning:
- Discord bot development
- Media handling via Discord APIs
- Event-driven automation in Python

---

## Features

- Send multiple images to a specific text channel
- Configurable number of images per execution
- Adjustable delay between each image
- Error handling with user feedback
- Uses Discord Gateway Intents for required permissions

---

## Prerequisites

- Python 3.6 or higher
- Discord Bot Token
- `discord.py` library
- Permission to send messages and attachments in the target channel

---

## Installation

Clone the repository:

```bash
git clone https://github.com/okntscgl/discord-image-flooder.git
cd discord-image-flooder
Install the required dependency:

bash
pip install discord.py
Configuration
Create a bot via the Discord Developer Portal

Enable required Gateway Intents

Copy your Bot Token

Add the token to the script (preferably via environment variables)

Example:

python
TOKEN = "YOUR_DISCORD_BOT_TOKEN"
Usage
Run the bot:

bash
python bot.py
Once the bot is online:

Specify the target channel

Define how many images to send

Set the delay between each image

The bot will send images sequentially according to the defined parameters.

How It Works (High-Level)
Bot Initialization

Connects to Discord using a bot token

Loads required gateway intents

Command Handling

Receives user command with image count and delay

Message Loop

Sends images one by one

Applies delay between each send to control rate

Error Handling

Catches failures when sending images

Notifies the user if an error occurs

Responsible Usage
This project should be used for:

Bot development practice

Media automation testing

Learning Discord API rate behavior

Avoid:

Harassment or spam

High-frequency flooding

Use in public servers without consent

Project Structure
graphql
.
├── bot.py       # Main Discord bot script
├── images/      # Images sent by the bot (if applicable)
├── README.md    # Documentation
License
This project is licensed under the MIT License.
See the LICENSE file for details.

Final Note
Automation without limits quickly becomes abuse.
Understanding rate control and responsible automation is essential for building compliant bots.
