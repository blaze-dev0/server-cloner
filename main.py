import discord
from discord.ext import commands
import os
import asyncio
from colorama import Fore
bot = commands.Bot(command_prefix=".",self_bot=True)

@bot.event
async def on_ready():
    print("\033[94m" + """
███╗░░░███╗░█████╗░███████╗██╗░█████╗░
████╗░████║██╔══██╗██╔════╝██║██╔══██╗
██╔████╔██║███████║█████╗░░██║███████║
██║╚██╔╝██║██╔══██║██╔══╝░░██║██╔══██║
██║░╚═╝░██║██║░░██║██║░░░░░██║██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
""" + "\033[0m" + "Made By @Mafiayt69")



    cloneguildid = int(input(f"\n {Fore.LIGHTYELLOW_EX}Which Guild You Want To Clone Guild Id : "))
    
 
    cloneguild = bot.get_guild(cloneguildid)
    
    if cloneguild == None: 
        print(f"{Fore.LIGHTRED_EX} Clone Guild Id Incorrect")
        return
    
    ownguildid = int(input(f"Where You Want To Clone Guild Id : "))
    ownguild = bot.get_guild(ownguildid)
    if (ownguild == None):
         print(f"{Fore.LIGHTRED_EX} Cloned Guild Id Incorrect")
         return
    print(f"{Fore.LIGHTBLUE_EX}{cloneguild.name}")
    print(f"{ownguild.name}")

    if ownguild.roles:

            for role in ownguild.roles:
                 
                    if role.name != "@everyone":
                            try:
                            
                                await role.delete()
                                await asyncio.sleep(1)
                            except Exception as e:
                                 print("e")

                        

    if ownguild.channels:
        for channel in ownguild.channels:
            try:
                await channel.delete()
            except Exception as e:
                 print('e')
            # await asyncio.sleep(1)



    roles = {}
    for role in cloneguild.roles[::-1]:
        permissions = role.permissions
        color = role.color
        role = await ownguild.create_role(name=role.name, permissions=permissions,color=color)
        roles[role.id] = role
        # await asyncio.sleep(1)

 
    for category in cloneguild.categories:
        categorys = await ownguild.create_category(category.name, overwrites=category.overwrites)
        # await asyncio.sleep(1)

        for channel in category.channels:
            if isinstance(channel, discord.TextChannel):
                channelss = await categorys.create_text_channel(channel.name, overwrites=channel.overwrites)
            elif isinstance(channel, discord.VoiceChannel):
                channelss = await categorys.create_voice_channel(channel.name, overwrites=channel.overwrites)
                # await asyncio.sleep(1)

            await channelss.edit(sync_permissions=True)
            # await asyncio.sleep(1)
            
        if role.name != "@everyone":
            await role.delete()
            

    rolename = "\n ".join([role.name for role in roles.values()])
    categoryname = "\n ".join([category.name for category in ownguild.categories])
    channelname = "\n ".join([channelss.name for channelss in ownguild.text_channels])


    print(f"{Fore.LIGHTBLUE_EX} roles : {rolename}")
    print(f"\n\n{Fore.LIGHTCYAN_EX} category : {categoryname}")
    print(f"\n\n{Fore.LIGHTRED_EX} channel : {channelname}")
  
    




bot.run("your token",bot=False)
