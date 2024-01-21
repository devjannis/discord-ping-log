import discord, asyncio, pytz, ctypes
from discord.ext import commands
from discord import Activity, ActivityType
from datetime import datetime

LOG_CHANNEL = 1234567890 # Replace with your log channel
TOKEN = 'your_token_here' # Replace with your token
allowed_guild_ids = {1234567890} #  Replace with your guild id

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def create_get_me_there_button(url):
    # Implementation to create a button that forwards the user to the message
    button = discord.ui.Button(label="GET ME THERE", url=url)
    view = discord.ui.View()
    view.add_item(button)
    return view

def get_log_channel(channel_id):

    channel = bot.get_channel(channel_id)
    if channel:
        return channel
    else:
        print(f"Log channel with ID {LOG_CHANNEL} not found.")


def create_ping_embed(role, author_id, channel_id):
    # Implementation to create a ping log embed with the important information
    everyone_roles = ["@here", "@everyone"]
    
    if role in everyone_roles:
        description = f"The role {role} has been tagged by <@{author_id}> in <#{channel_id}>."
    else:
        description = f"The role <@&{role}> has been tagged by <@{author_id}> in <#{channel_id}>."
    embed = discord.Embed(title="NEW PING DETECTED", description=description, color=0x20d08f)
    embed.set_footer(text='Click the "GET ME THERE" button to gain quick access to that message.')
    return embed


@bot.event
async def on_ready():
    activity = Activity(
        name="Watching channels...", type=ActivityType.playing, details="Working"
    )
    await bot.change_presence(activity=activity)
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Check if the author is not the bot
    if message.author != bot:
        # Message url
        url = f"https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}"
        # Create the button based on the message url
        view = create_get_me_there_button(url)
        if message.guild.id in allowed_guild_ids:
            # Check if Role is a everyone role or not
            if message.mention_everyone:
                # Define the role variable based on the pinged role
                if "@everyone" in message.content:
                    # Mentioned role == @everyone
                    role = "@everyone"
                elif "@here" in message.content:
                    # Mentioned role == @here
                    role = "@here"
                # Create the ping log embed
                embed = create_ping_embed(role, message.author.id, message.channel.id)
                try:
                    channel = get_log_channel(LOG_CHANNEL)
                    await channel.send(embed=embed, view=view)
                except Exception as e:
                    print(f"Error sending message to log channel: {e}")
            else:
                for role in message.role_mentions:
                    # Create the ping log embed
                    embed = create_ping_embed(role.id, message.author.id, message.channel.id)
                    try:
                        channel = get_log_channel(LOG_CHANNEL)
                        await channel.send(embed=embed, view=view)
                    except Exception as e:
                        print(f"Error sending message to log channel: {e}")

bot.run(TOKEN)
