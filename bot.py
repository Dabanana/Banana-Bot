import discord
import random
from imgurpython import ImgurClient
import twitter
import Tictactoe

api = twitter.Api("7L5XmV18ORSnp9yGo1SLuexnL", "ZktX8HqTTFgn25iWvGxizsKovFUWFGVKmacMJ0CrEgTZ6Flmrq", "2799268561-5pXZJUPwTaXm0kFzupPl7jsBDHDbnEpFvy05dE2", "xo9G4HHUswae7z8IdmZ1nzuzvaE1yhUXvkWQb8M7ks2ed")
client = discord.Client()
imgurclient = ImgurClient("d0c24d1db4fb537","6d9578660c1ca1dd62c89c5ecc0f8fca289c7467")


@client.async_event
def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('#test'):
		yield from client.send_message(message.channel, "This is a fucking test", tts = True)

	if message.content.startswith('#frank'):
		yield from client.send_message(message.channel, "Hey I'm Frank. Would you like to know my opinion?", tts = True)
		opinions = ["Hey, I agree with your opinion.", "I'm fucking triggered!", "Hey, your opinion's stupid"]
		msg = yield from client.wait_for_message(timeout = 10, author = message.author)
		if msg is None:
			yield from client.send_message(message.channel, "Wow... I really wanted to share my opinion", tts = True)
			return
		if msg.content == "yes":
			num = random.randint(0,2)
			yield from client.send_message(message.channel, opinions[num], tts = True)
		elif msg.content == "no":
			yield from client.send_message(message.channel, "Um. Wu", tts = True)
		elif msg.content == "wu":
			while True:
				yield from client.send_message(message.channel, "Yo. Wu", tts = True)
				msg = yield from client.wait_for_message(timeout = 10, author = message.author,content = "wu") 
				if msg is None:
					yield from client.send_message(message.channel, "Wu!", tts = True)
					return

	if message.content.startswith('#choose '):
		msg = message.content[len('#choose'):].strip()
		if msg == "":
			yield from client.send_message(message.channel, "Give me some choices man!", tts = True)
			return
		choices = msg.split(",")
		xs = len(choices)
		if xs == 1:
			yield from client.send_message(message.channel, "You only gave me one choice, cunt.", tts = True)
			return
		num = random.randint(0,xs)
		yield from client.send_message(message.channel, "I choose {0}".format(choices[num]), tts = True)

	if message.content.startswith('#kierannudes'):
		yield from client.send_file(message.channel, "C://bananabot//kieran.jpg", filename = "kieran.jpg", content = "I don't have nudes but I have...")

	if message.content.startswith('#shutdown'):
		yield from client.send_message(message.channel, "Shutting down...")
		yield from client.logout()

	if message.content.startswith('#imgur '):
		items = imgurclient.gallery()
		for item in items:
			yield from client.send_message(message.channel, item.link)
			return

	if message.content.startswith('#tictactoe'):
		t = Tictactoe.Tictactoe()
		yield from client.send_message(message.channel, t)
		while True:
			message = yield from client.wait_for_message()
			if message.content.startswith('#naught'):
				coord = message.content.strip("#naught ")
				row = int(coord[2])
				column = int(coord[0])
				yield from client.send_message(message.channel, t.naught(column,row))
				yield from client.send_message(message.channel, t.check())
			elif message.content.startswith('#cross'):
				coord = message.content[len('#cross'):].strip()
				row = int(coord[2])
				column = int(coord[0])
				yield from client.send_message(message.channel, t.cross(column,row))
				yield from client.send_message(message.channel, t.check())
			if t.win != 0:
				return

	if message.content.startswith("#psr"):
		msg = message.content.strip("psr# ")
		psr = [":fist:", ":v:", ":raised_hand:"]
		num = random.randint(0,2)
		ans = psr[num]
		if num - 1 == -1:
			win = psr[2]
		else:
			win = psr[num - 1]
		if num + 1 == 3:
			lose = psr[0]
		else:
			lose = psr[num + 1]
		yield from client.send_message(message.channel, ans)
		if ans in msg:
			yield from client.send_message(message.channel, "It's a draw!")
			return
		elif win in msg:
			yield from client.send_message(message.channel, "You win!")
			return
		elif lose in msg:
			yield from client.send_message(message.channel, "You lose!")
			return


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run("MjIwNDk4NDgwMDk3OTE4OTg2.Cql3kw.aTquvKfAbubAnz97Dc8rfukqO68")