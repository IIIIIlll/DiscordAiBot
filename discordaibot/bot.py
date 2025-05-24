import discord
import openai
import os

# Set your tokens here
DISCORD_TOKEN = 'enter-discord-token-here'
OPENAI_API_KEY = 'enter-openai-api-token-here'

openai.api_key = OPENAI_API_KEY
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ask'):
        prompt = message.content[len('!ask '):]
        if not prompt:
            await message.channel.send("Ask me something like `!ask What's the weather?`")
            return

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = response.choices[0].message.content.strip()
            await message.channel.send(reply)
        except Exception as e:
            await message.channel.send("Something went wrong.")
            print(e)

client.run(DISCORD_TOKEN)
