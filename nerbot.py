import lightbulb
from datetime import datetime
import random
import pytz
import hikari
from plugin.Quran import Quran

# Insert your client token here
with open('key.txt', 'r') as f:
    key = f.read()

bot = lightbulb.BotApp(key, prefix=".")
list_guild = [875718851097165824, 779752554137518130]


def check_pre_guild(context: lightbulb.Context) -> bool:
    return context.guild_id in list_guild


# time


@bot.command
@lightbulb.command('time', aliases=["tm"], description="Tells you current time")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def time(msg: lightbulb.Context) -> None:
    time = datetime.now(pytz.timezone('Asia/Dhaka')
                        ).time().strftime("%I:%M %p")
    await msg.respond(time)


@bot.command
@lightbulb.command('date', aliases=["dt"], description="Tells you current time")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def date(msg: lightbulb.Context) -> None:
    time = datetime.now(pytz.timezone('Asia/Dhaka')
                        ).date().strftime("%d-%m-%Y")
    await msg.respond(time)

# Random Quran Verse Generator


@bot.command
@lightbulb.command('random_verse', aliases=["rq", "rv", 'verse', 'rq', 'rqv', 'random_quran_verse'], description="Random Quran Verses")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def random_quran_verse(msg: lightbulb.Context) -> None:
    await msg.respond(Quran.random_verse())


# Quran Verse
@bot.command
@lightbulb.option('verse', 'The Holy Quran Verse number')
@lightbulb.option('chapter', 'The Holy Quran Chapter number')
@lightbulb.command('quran', description="Get The Holy Quran Verse", auto_defer=True)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def quran(ctx: lightbulb.Context) -> None:
    chapter = ctx.options.chapter
    verse = ctx.options.verse
    await ctx.respond(Quran(chapter, verse).get_verse())
# Upcoming ACC Exam


@bot.command
@lightbulb.command('next-exam', aliases=['ne', 'up'], description='Tells you about upcoming exam of ACC')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def next_exam(msg: lightbulb.Context) -> None:
    day = datetime.now(pytz.timezone('Asia/Dhaka')
                       ).date().day
    month = datetime.now(pytz.timezone('Asia/Dhaka')
                         ).date().month
    year = datetime.now(pytz.timezone('Asia/Dhaka')
                        ).date().year

    def current_time():
        cyear = datetime.now(pytz.timezone('Asia/Dhaka')
                             ).year
        cmonth = datetime.now(pytz.timezone('Asia/Dhaka')
                              ).date().month
        cday = datetime.now(pytz.timezone('Asia/Dhaka')
                            ).date().day
        chour = datetime.now(pytz.timezone('Asia/Dhaka')
                             ).time().hour
        cmin = datetime.now(pytz.timezone('Asia/Dhaka')
                            ).time().minute
        return datetime(cyear, cmonth, cday, chour, cmin)

    def m_time(hour, min):
        cyear = datetime.now(pytz.timezone('Asia/Dhaka')
                             ).year
        cmonth = datetime.now(pytz.timezone('Asia/Dhaka')
                              ).date().month
        cday = datetime.now(pytz.timezone('Asia/Dhaka')
                            ).date().day
        return datetime(cyear, cmonth, cday, hour, min)

    def exam():
        if month == 2 and year == 2022:
            pass
        else:
            return None
        if day <= 15:
            if day == 15 and current_time() >= m_time(9, 10):
                return 'English at 8:45AM\nBiology at 11:10AM'
            else:
                return 'Chemistry'
        elif day == 16:
            return 'English at 8:45AM**\nBiology at 11:10AM'
        elif day == 17:
            if m_time(9, 10) <= current_time() < m_time(11, 40):
                return 'Biology at 11:10AM'
            elif m_time(11, 40) <= current_time():
                return 'Higher Math'
            else:
                return 'English at 8:45AM'
        elif 17 < day <= 20:
            if current_time() >= m_time(9, 10):
                return None
            else:
                return 'Higher Math'

    if exam() == None:
        await msg.respond('You have No Exam :) yay!!!')
    else:
        await msg.respond(f'Upcoming Exam: **{exam()}**')


# Help
@bot.command
@lightbulb.command('about', aliases=['whoareyou'], description='More about this BOT!')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def about(msg: lightbulb.Context) -> None:
    message = """
This bot is created by **Nahian Labib Limon**
Its an early access. I am still under development...
Follow my master on Facebook: https://www.facebook.com/nahianlabib.limon
Also contact him on discord: `Lemonade#1325`
"""

    await msg.respond(message)

# ki kore
sadique = ['যৌবনটা লারা দিয়া কচু রান্না করে।',
           'বদনা নিয়ে ব্যস্ত',
           'সাইমুনের সাথে ব্যস্ত আসে',
           'লঞ্চে আসে একটা বিশেষ কাজ করার জন্য',
           'ঘুমাইয়া আসে',
           'Drama দেখতাসে',
           'Movie দেখতাসে']

rizon = ['মিরপুর ১৪ তে একটি শলাকায় আগুন ধরাচ্ছে',
         'Oxford Dictionary মুখস্ত করতেছে',
         'Harvard এর জন্য প্রস্তুতি নিচ্ছে',
         "COX'S Bazar গেছে"]

sarjil = ['পানু দেখে',
          'ঘাস কাটে',
          'শাড়ি পিন্দে',
          'ঘুমায়']


@bot.command
@lightbulb.add_checks(lightbulb.Check(check_pre_guild))
@lightbulb.option('member', 'Greet member', hikari.User)
@lightbulb.command('kikore', 'What are you doing?')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def kikore(msg: lightbulb.Context) -> None:
    if msg.options.member.id == 763072156350283786 or msg.options.member.username == 'sadique':
        await msg.respond(f'{msg.options.member.mention} {random.choice(sadique)}')
    elif msg.options.member.id == 721817563973156975 or msg.options.member.username == 'Rizon':
        await msg.respond(f'{msg.options.member.mention} {random.choice(rizon)}')
    elif msg.options.member.id == 779686900113080340 or msg.options.member.username == 'Sarjil':
        await msg.respond(f'{msg.options.member.mention} {random.choice(sarjil)}')
    elif msg.options.member.id == 763046913305346048 or msg.options.member.username == 'Seam':
        await msg.respond(f'এই সব আউল-ফাউল পোলাপানের খবর আমি রাখি না।')
    else:
        await msg.respond('জানি নিয়া।')


bot.run()
