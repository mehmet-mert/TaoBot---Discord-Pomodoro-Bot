import asyncio
import datetime
import random

import discord
from discord import FFmpegPCMAudio
from discord.ext import commands
from pafy import new

TOKEN = ""
client = commands.Bot(command_prefix="tao ")

# ŞARKILAR İÇİN GERKLİ LİNKLER
rain = "https://www.youtube.com/watch?v=bhWJF9FlBqM"
fire = "https://www.youtube.com/watch?v=iz7wtTO7roQ"
water = "https://www.youtube.com/watch?v=GuCTnkDx72g"
lofi_links = ("https://youtu.be/jrTMMG0zJyI", "https://youtu.be/mMw6UFZuL9o",
              "https://youtu.be/6yXJtOdNnNk", "https://youtu.be/zPyg4N7bcHM")
gif_links = ("https://media1.tenor.com/images/103e195369f1e8b07d9e07ebce8cd3c5/tenor.gif?itemid=22126739",
             "https://media1.tenor.com/images/1af748d196e0c0c5262c5409e17b8e60/tenor.gif?itemid=22126738",
             "https://media1.tenor.com/images/b3cdd7c23f32e68a474152607d2fd810/tenor.gif?itemid=22126740")

linkler = {"rain": rain,
           "fire": fire,
           "water": water,
           }
link_list = {"rain", "fire", "water", "lofi"}
kullanıcı = "yok"

@client.event
async def on_ready():
    print("Bot Online")
    activity = discord.Game(name="tao yardım", type=3)
#YARDIM
@client.command()
async def yardım(message, konu="boş"):
    if (konu == "pomo"):
        helpEmbed = discord.Embed(title="⛩️ TaoBot Pomodoro Komutları ⛩️",
                                  description="Bir Pomodoro sayacı oluşturalım.",
                                  color=0xff4500)
        helpEmbed.add_field(name="Bir Pomodoro Sayacı Oluşturma",
                            value="`tao pomo görev set_başına_dakika set_sayısı`,"
                                  " `tao pomo yazılım 25 2`", inline=False)
        helpEmbed.add_field(name="Sayacı Sonlandırma",
                            value="`tao bitir` ile sayacı sonlandırabilirsiniz.", inline=False)
        await message.send(embed=helpEmbed)
    elif konu == "bilgi":
        helpEmbed = discord.Embed(title="⛩️ TaoBot Bilgi Komutları ⛩️",
                                  description="Büyük düşünür ve Taoizm'in kurucusu Lao Tzu tarihte birçok insana "
                                              "derin düşünmeyi öğretmiştir."
                                              " Ama ne yazık ki Sensei herkese aynı anda ulaşamadığından bu botu üretti."
                                              " Ve asırlardır bu bot kullanılıyor.",
                                  color=0xff4500)
        helpEmbed.add_field(name="Süleyman Hilmi Akkaya", value="https://github.com/hilmiAkkaya", inline=False)
        helpEmbed.add_field(name="Mehmet Mert Altuntaş", value="https://github.com/mehmet-mert", inline=False)

        await message.send(embed=helpEmbed)
    elif (konu == "müzik"):
        helpEmbed = discord.Embed(title="⛩️ TaoBot Müzik Komutları ⛩️",
                                  description="Arkanıza yaslanın ve TaoBot ile çalışırken müziğin keyfini çıkarın.",
                                  color=0xff4500)
        helpEmbed.add_field(name="Rahatlatıcı Lo-Fi Müzikler", value="`tao play lofi`", inline=False)
        helpEmbed.add_field(name="Doğa Sesleri", value="`tao play fire`, `tao play water`, `tao play rain`",
                            inline=False)
        helpEmbed.add_field(name="Botu Ses Kanalından Çıkarma", value="`tao leave` ile botu kanaldan çıkarabilirsiniz.",
                            inline=False)

        await message.send(embed=helpEmbed)
    elif (konu == "boş"):
        helpEmbed = discord.Embed(title="⛩️ TaoBot Yardım ⛩️",
                                  description="TaoBot çalışırken `Pomodoro Tekniği` ile zamanınızı yöneten bir Discord botudur.",
                                  color=0xff4500)
        helpEmbed.add_field(name="┬┴┬┴┤tao yardım pomo  ├┬┴┬┴", value="Pomodoro sayacı komutları", inline=False)
        helpEmbed.add_field(name="┬┴┬┴┤tao yardım müzik ├┬┴┬┴", value="Arkanıza yaslanın ve müziğin keyfini çıkarın.",
                            inline=False)
        helpEmbed.add_field(name="┬┴┬┴┤tao yardım bilgi     ├┬┴┬┴",
                            value="TaoBot hakkında birkaç bilgi.",
                            inline=False)
        await message.send(embed=helpEmbed)
    else:
        helpEmbed = discord.Embed(title="⛩️ TaoBot Yardım ⛩️",
                                  description="TaoBot çalışırken `Pomodoro Tekniği` ile zamanınızı yöneten bir Discord botudur.",
                                  color=0xff4500)
        helpEmbed.add_field(name="┬┴┬┴┤tao yardım pomo  ├┬┴┬┴", value="Pomodoro sayacı komutları", inline=False)
        helpEmbed.add_field(name="┬┴┬┴┤tao yardım müzik  ├┬┴┬┴", value="Arkanıza yaslanın ve müziğin keyfini çıkarın.",
                            inline=False)
        helpEmbed.add_field(name="┬┴┬┴┤tao yardım bilgi  ├┬┴┬┴",
                            value=""
                                  "TaoBot hakkında birkaç bilgi.",
                            inline=False)
        await message.send(embed=helpEmbed)
#MUZIK OYNATICI
@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command(pass_context=True)
async def play(ctx, link):
    if ((link in link_list) == False):
        pass
    else:
        ffmpeg_opts = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        helpEmbed = discord.Embed(title="Çalınıyor",
                                  description="⛩️ Müziğin keyfini çıkarın ☕.",
                                  color=0xff4500)
        helpEmbed.set_image(url=random.choice(gif_links))
        await ctx.send(embed=helpEmbed)
        if (link == "lofi"):
            video = new(random.choice(lofi_links))
        else:
            video = new(linkler[link])
        audio = video.getbestaudio().url
        voice.play(FFmpegPCMAudio(audio, **ffmpeg_opts))
        voice.is_playing()
    await leave()

#POMODORO
@client.command()
async def bitir(message):
    global kullanıcı
    kullanıcı = message.author

async def mola(message, calisma):
    if kullanıcı == message.author:
        return
    dt_started = datetime.datetime.utcnow()
    zaman = int(calisma)*60
    mesaj = await message.send(content=("**{}** Sensei' nin molasının bitimine {} saniye"
                                        .format(message.author, str(zaman))))
    while True:
        if kullanıcı == message.author:
            break
        dt_ended = datetime.datetime.utcnow()
        await asyncio.sleep(1)
        fark = str(int((dt_ended - dt_started).total_seconds()))

        remaining = int(calisma)*60 - int(fark)
        if remaining >= 0:
            await mesaj.edit(content=("**{}** Sensei' nin molasının bitimine {} saniye"
                                      "".format(message.author, str(int(remaining)))))
        else:
            break

async def pomok(message, gorev, calisma, set_sayisi):
    dt_started = datetime.datetime.utcnow()
    mesaj = await message.send("**{}** Sensei' nin {} görevini tamamlamasına {} saniye ⏰"
                               .format(message.author, gorev, str(int(calisma) * 60)))
    while True:
        if kullanıcı == message.author:
            break
        dt_ended = datetime.datetime.utcnow()
        await asyncio.sleep(1)
        fark = str(int((dt_ended - dt_started).total_seconds()))
        remaining = int(calisma) * 60 - int(fark)
        if remaining >= 0:
            await mesaj.edit(content=("**{}** Sensei' nin {} görevini tamamlamasına {} saniye ⏰"
                                      .format(message.author, gorev, str(remaining))))
        else:
            await mesaj.edit(content="Mola Zamanı!")
            break

@client.command()
async def pomo(message, gorev, calisma, set_sayisi):
    global kullanıcı
    try:
        int(calisma)
        int(set_sayisi)

        helpEmbed = discord.Embed(title=str(message.author) + "' un Pomodoro Sayacı",
                                  description="10 saniye içinde başlıyor.",
                                  color=0xff4500)
        helpEmbed.add_field(name="Görev", value=gorev, inline=False)
        helpEmbed.add_field(name="Pomodoro Başına Dakika", value=calisma, inline=False)
        helpEmbed.add_field(name="Pomodoro Sayısı", value=set_sayisi, inline=False)

        await message.send(embed=helpEmbed)
        mesaj = await message.send("⛩️ Pomodoronun başlamasına son " + str(10) + " saniye ⛩️.")
        kullanıcı="yok"
        for i in range(10):
            if (kullanıcı == message.author):
                break
            await mesaj.edit(content=("⛩️ Pomodoronun başlamasına son " + str(9 - i) + " saniye ⛩️."))
            await asyncio.sleep(1)
        for i in range(int(set_sayisi)):
            if (kullanıcı == message.author):
                break
            await pomok(message, gorev, calisma, set_sayisi)
            if (i + 1) % 4 == 0:
                await mola(message, str(int(5) * 6))
            else:
                await mola(message, str(5))
        kullanıcı = message.author
        await message.send("Pomodoro tamamlandı!")
    except:
        await message.send("Parametreleri yanlış girdiniz. `tao yardım pomo` ile doğru kullanıma bakabilirsiniz.")

client.run(TOKEN)
