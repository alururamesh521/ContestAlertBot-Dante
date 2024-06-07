# Upcoming Coding Contests Bot

<div style="display: flex;">
    <img src="https://github.com/alururamesh521/ContestAlertBot-Dante/assets/142136138/c883756b-b11b-4213-8440-4b7072172341" style="width: 150px; height: auto; margin-right: 10px;">
    <img src="https://github.com/alururamesh521/ContestAlertBot-Dante/assets/142136138/cc293920-ecbe-4d47-88da-0469565315eb" style="width: 150px; height: auto;">
</div>

**Upcoming Coding Contests Bot** is a Discord bot designed to keep programmers informed about upcoming coding contests. It automatically fetches and posts details about contests from popular competitive programming platforms like LeetCode, Codeforces, CodeChef, and GeeksforGeeks. The bot ensures timely updates by posting contest details in a designated Discord channel as soon as they become available.

## Features

- Fetches upcoming contests from:
  - LeetCode
  - Codeforces
  - CodeChef
  - GeeksforGeeks
- Posts contest details in a specified Discord channel.
- Provides information such as contest title, start time, and contest link.

## Requirements

- Python 3.7+
- `discord.py` library
- `requests` library

## Setup

1. Clone this repository.
2. Install the required libraries:
    ```bash
    pip install discord.py requests
    ```
3. Replace `YOUR_DISCORD_BOT_TOKEN` with your Discord bot token and `YOUR_CHANNEL_ID` with your Discord channel ID in the `bot.py` file.
4. Run the bot:
    ```bash
    python bot.py
    ```

## Usage

Once the bot is running, it will automatically post the upcoming coding contest details in the specified Discord channel whenever new contests are available.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

Special thanks to [Shivakrishna212](https://github.com/Shivakrishna212) for contributing to this project.
