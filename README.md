# Discord Ping Logger Bot

## Overview

This Discord bot is designed to log mentions of roles, including `@everyone` and `@here`, in specified guilds. It creates a log embed with important information and a button to quickly access the original message.

## Setup

1. **Prerequisites:**
   - Python 3.x
   - Discord.py library (`discord.py`)
   - Ensure you have the necessary permissions to add the bot to your Discord server.

2. **Installation:**
   - Clone the repository or download the script.
   - Install dependencies with `pip install -r requirements.txt`.

3. **Configuration:**
   - Replace `your_token_here` in the script with your actual bot token.
   - Set the correct `LOG_CHANNEL` ID for the log messages.

## Usage

1. **Run the Bot:**
   - Execute the script to run the Discord bot.
   - Ensure the bot is added to your server and has the necessary permissions.

2. **Bot Commands:**
   - The bot listens for role mentions and logs them in the specified log channel.
   - The log embed includes information about who pinged the role and in which channel.
   - A "GET ME THERE" button is provided for quick access to the original message.

## Customization

- **Allowed Guilds:**
  - Adjust the `allowed_guild_ids` set to include the server IDs where you want the bot to operate.

## Notes

- **Token Security:**
  - Keep your bot token confidential. Do not share it publicly.

- **Error Handling:**
  - Ensure the log channel exists; otherwise, errors will be printed to the console.

## Contributing

Feel free to contribute by submitting issues, feature requests, or pull requests.
