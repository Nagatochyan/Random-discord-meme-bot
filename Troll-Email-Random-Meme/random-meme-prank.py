import discord
import requests
from bs4 import BeautifulSoup
TOKEN = 'DISOCRD BOT TOKEN'
client = discord.Bot()
@client.slash_command(name="random_meme")
async def random_meme(ctx):
    HTML_TEMPLATE = "<div><img src={}></div>"
    BASE_URL = "https://imgflip.com/i/"
    def get_random_meme():
        """Extract image url from website"""
        response = requests.get(BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            # for regular image
            img_url = 'https:' + soup.find('img', id='im')['src']
        except TypeError:
            # for gif/video
            img_url = 'https:' + soup.find('video', id='vid')['poster']
        return img_url
    def create_message():
        ranme="test"
        global html_body
        """Create an html formatted email message"""
        img_url = get_random_meme()
        html_body = HTML_TEMPLATE.format(img_url)
    create_message()
    kotae=(html_body.replace('></div>', ''))
    iine=(kotae.replace('<div><img src=', ''))
    await ctx.respond(iine)
client.run(TOKEN)
