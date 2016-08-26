from halibot import HalModule
import re

regex = re.compile("^@(\d\d?)$")


emotes = [
"",
"Yes.",
"No.",
"Food please.",
"Wood please.",
"Gold please.",
"Stone please.",
"Ahh!",
"All hail, king of the losers!",
"Ooh!",
"I'll beat you back to Age of Empires.",
"(Herb laugh)",
"Ah! Being rushed.",
"Sure, blame it on your ISP.",
"Start the game already!",
"Don't point that thing at me!",
"Enemy sighted!",
"It is good to be the king.",
"Monk! I need a monk!",
"Long time, no siege.",
"My granny could scrap better than that.",
"Nice town, I'll take it.",
"Quit touching me!",
"Raiding party!",
"Dadgum.",
"Eh, smite me.",
"The wonder, the wonder, the... no!",
"You played two hours to die like this?",
"Yeah, well, you should see the other guy.",
"Roggan.",
"Wololo.",
"Attack an enemy now.",
"Cease creating extra villagers.",
"Create extra villagers.",
"Build a navy.",
"Stop building a navy.",
"Wait for my signal to attack.",
"Build a wonder.",
"Give me your extra resources.",
"(Ally sound)",
"(Enemy sound)",
"(Neutral sound)",
"What age are you in?"
]

class AoeModule(HalModule):

	def receive(self, msg):
		m = regex.match(msg.body)
		if not m:
			return
		self.reply(msg, body=emotes[int(m.group(1))])
