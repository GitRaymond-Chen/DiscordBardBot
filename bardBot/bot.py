import discord
from bardapi import Bard
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("BARD_API_KEY")
bard = Bard(token=token)
 
intents=discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is now running!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('AskBard:'):
        question = message.content[8:]
        if question[0] == " ":
            print("space in front")
            question = question[1:]
        print(question)
        result = bard.get_answer(question)
        await message.channel.send(result["content"])
            
client.run("MTEzNjQ0NDI3MTc5NzQ2OTI3Ng.GJVJLq._jLDGcDWGTqnnwSr6Y8sYlNq7RYpopmKP2A79Y")



# # Feature to ask Google bard questions
# question = input("Your question for Google Bard: ")
# result = bard.get_answer(question)
# content1 = result["content"]
# print(content1)
# print()

# # Feature to find educational video about topic
# topic = input("Find videos on topics you are confused about: ")
# result = bard.get_answer("Find a link to a video on Youtube about " + topic)
# content2 = result["content"]
# print(content2)