<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upcoming Coding Contests Bot</title>
</head>

<body>

    <h1>Upcoming Coding Contests Bot</h1>

    <img src="https://github.com/alururamesh521/ContestAlertBot-Dante/assets/142136138/c883756b-b11b-4213-8440-4b7072172341"
        alt="ContestAlertBot Logo">

    <p><strong>Upcoming Coding Contests Bot</strong> is a Discord bot designed to keep programmers informed about upcoming
        coding contests. It automatically fetches and posts details about contests from popular competitive programming
        platforms like LeetCode, Codeforces, CodeChef, and GeeksforGeeks. The bot ensures timely updates by posting contest
        details in a designated Discord channel as soon as they become available.</p>

    <h2>Features</h2>

    <ul>
        <li>Fetches upcoming contests from:
            <ul>
                <li>LeetCode</li>
                <li>Codeforces</li>
                <li>CodeChef</li>
                <li>GeeksforGeeks</li>
            </ul>
        </li>
        <li>Posts contest details in a specified Discord channel.</li>
        <li>Provides information such as contest title, start time, and contest link.</li>
    </ul>

    <h2>Requirements</h2>

    <ul>
        <li>Python 3.7+</li>
        <li><code>discord.py</code> library</li>
        <li><code>requests</code> library</li>
    </ul>

    <h2>Setup</h2>

    <ol>
        <li>Clone this repository.</li>
        <li>Install the required libraries:
            <pre><code>pip install discord.py requests</code></pre>
        </li>
        <li>Replace <code>YOUR_DISCORD_BOT_TOKEN</code> with your Discord bot token and <code>YOUR_CHANNEL_ID</code> with
            your Discord channel ID in the <code>bot.py</code> file.</li>
        <li>Run the bot:
            <pre><code>python bot.py</code></pre>
        </li>
    </ol>

    <h2>Usage</h2>

    <p>Once the bot is running, it will automatically post the upcoming coding contest details in the specified Discord
        channel whenever new contests are available.</p>

    <h2>Contributing</h2>

    <p>Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to
        discuss what you would like to change.</p>

</body>

</html>
