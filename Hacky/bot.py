import discord
from discord.ext import tasks
import requests
import datetime
import asyncio


# Function to fetch contests details
def fetch_contests_details(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            contests_data = response.json()
            ongoing_contests = contests_data.get("data", {}).get("ongoingContestsList", [])
            upcoming_contests = contests_data.get("data", {}).get("upcomingContestsList", [])
            return ongoing_contests, upcoming_contests
        else:
            print("Failed to fetch data. Status code:", response.status_code)
            return None, None
    except Exception as e:
        print("An error occurred:", str(e))
        return None, None


# Function to format contest details
def format_contest_details(contest):
    formatted_date = datetime.datetime.strptime(contest.get('startTime'), '%Y-%m-%dT%H:%M:%S.%fZ').strftime(
        '%A, %d %B %Y %I:%M %p')
    details = f"{contest.get('title')}: {formatted_date}\n"
    details += f"Link: {contest.get('url')}\n\n"
    return details


# Function to send contest details
async def send_contests_details(channel, ongoing_contests, upcoming_contests):
    current_time = datetime.datetime.now()

    message = "**@Dear Coders**\n\n"

    # Send details of ongoing contests
    if ongoing_contests:
        message += "**Live contests:**\n"
        for contest in ongoing_contests:
            message += format_contest_details(contest)

    # Send details of upcoming contests
    if upcoming_contests:
        message += "**Upcoming contests:**\n"
        for contest in upcoming_contests:
            message += format_contest_details(contest)
            # Check if the contest is starting within 60 minutes
            start_time = datetime.datetime.strptime(contest.get('startTime'), '%Y-%m-%dT%H:%M:%S.%fZ')
            if start_time > current_time and (start_time - current_time) <= datetime.timedelta(minutes=60):
                message += f"Reminder: This contest will start in the next 60 minutes.\n\n"

    await channel.send(message)


# Discord client
class MyClient(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.last_update = None

    async def on_ready(self):
        print('Logged on as', self.user)
        self.contest_check.start()

    @tasks.loop(minutes=15)  # Check every 15 minutes
    async def contest_check(self):
        current_time = datetime.datetime.now()

        # Fetch contests details if a week has passed since the last update or it's the first time
        if not self.last_update or (current_time - self.last_update) >= datetime.timedelta(weeks=1):
            api_url = "https://smartinterviews.in/api/contest/getContestsList"
            ongoing_contests, upcoming_contests = fetch_contests_details(api_url)
            if ongoing_contests or upcoming_contests:
                channel = self.get_channel(1242847205811945582)  # Replace YOUR_CHANNEL_ID with your channel ID
                await send_contests_details(channel, ongoing_contests, upcoming_contests)
                self.last_update = current_time

        # Check for contests starting within an hour and send reminders
        if upcoming_contests:
            for contest in upcoming_contests:
                start_time = datetime.datetime.strptime(contest.get('startTime'), '%Y-%m-%dT%H:%M:%S.%fZ')
                if start_time > current_time and (start_time - current_time) <= datetime.timedelta(minutes=60):
                    channel = self.get_channel(1242847205811945582)  # Replace YOUR_CHANNEL_ID with your channel ID
                    message = format_contest_details(contest)
                    message += f"Reminder: This contest will start in the next 60 minutes.\n\n"
                    await channel.send(message)


# Define intents
intents = discord.Intents.default()

# Run the bot
client = MyClient(intents=intents)
client.run('MTI0MzQ3ODY0Mjk3ODE5MzQ4MA.GxfiZq.T-h6wy06xCmUf3WJLsEGfHGfvA9l4i3f8vxz0E')  # Replace YOUR_DISCORD_BOT_TOKEN with your bot token
