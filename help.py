import discord
from discord.ext import commands

import user_db
import config

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        user_id = str(ctx.author.id)
        user_name = ctx.author.name

        if not user_db.check_user(user_id):
            user_db.add_user(user_id, user_name)

            embed = discord.Embed(
                title="**CPUchain tipbot Command List:**",
                color=0x7152b6)
            embed.set_author(
                name=ctx.author.display_name,
                icon_url=ctx.author.avatar_url_as(format='png', size=256))
            embed.add_field(
                name="**//help**",
                value="This is the command you have just used :wink:",
                inline=True)
            embed.add_field(
                name="**//info**",
                value="Show CPUchain Core wallet/blockchain info.",
                inline=True)
            embed.add_field(
                name="**//balance**",
                value="Show your CPUchain balances.",
                inline=True)
            embed.add_field(
                name="**//deposit**",
                value="Show your CPUchain deposit address.",
                inline=True)
            embed.add_field(
                name="**//tip**",
                value="Tip specified user. [//tip @minkcrypto 1] to tip 1 CPU",
                inline=True)
            embed.add_field(
                name="**//withdraw**",
                value="Withdraw CPU from your wallet. [//withdraw ADDRESS AMOUNT]",
                inline=True)
            embed.add_field(
                name="**//withdrawal**",
                value="Withdraw all CPU from your wallet. [//withdrawal ADDRESS]",
                inline=True)
            embed.set_thumbnail(url=self.bot.user.avatar_url_as(format='png', size=1024))
            embed.set_footer(text="CPUchain tipbot v{0}".format(config.VERSION), icon_url=self.bot.user.avatar_url_as(format='png', size=256))

            await ctx.channel.send(embed=embed)
        else:
            pass

            embed = discord.Embed(
                title="**CPUchain tipbot Command List:**",
                color=0x7152b6)
            embed.set_author(
                name=ctx.author.display_name,
                icon_url=ctx.author.avatar_url_as(format='png', size=256))
            embed.add_field(
                name="**//help**",
                value="This is the command you have just used.",
                inline=True)
            embed.add_field(
                name="**//info**",
                value="Show CPUchain Core wallet/blockchain info.",
                inline=True)
            embed.add_field(
                name="**//balance**",
                value="Show your CPUchain balances.",
                inline=True)
            embed.add_field(
                name="**//deposit**",
                value="Show your CPUchain deposit address.",
                inline=True)
            embed.add_field(
                name="**//tip**",
                value="Tip specified user. [//tip @minkcrypto 1] to tip 1 CPU",
                inline=True)
            embed.add_field(
                name="**//withdraw**",
                value="Withdraw CPUchain from your wallet. [//withdraw ADDRESS AMOUNT]",
                inline=True)
            embed.add_field(
                name="**//withdrawal**",
                value="Withdraw all CPUchain from your wallet. [//withdrawal ADDRESS]",
                inline=True)
            embed.set_thumbnail(url=self.bot.user.avatar_url_as(format='png', size=1024))
            embed.set_footer(text="CPUchain tipbot v{0}".format(config.VERSION), icon_url=self.bot.user.avatar_url_as(format='png', size=256))

            await ctx.channel.send(embed=embed)

def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Help(bot))
