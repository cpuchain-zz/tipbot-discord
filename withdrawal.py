from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import Decimal
import discord
from discord.ext import commands

import user_db
import config

# connect to coind
rpc_connection = 'http://{0}:{1}@{2}:{3}'.format(config.rpc_user, config.rpc_password, config.ip, config.rpc_port)

class Withdrawal(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def withdrawal(self, ctx, address=None):
        client = AuthServiceProxy(rpc_connection)
        user_id = str(ctx.author.id)

        if not user_db.check_user(user_id):
            embed = discord.Embed(
                title="**For first-use-user**",
                color=0x0043ff)
            embed.set_author(
                name=ctx.author.display_name,
                icon_url=ctx.author.avatar_url_as(format='png', size=256))
            embed.add_field(
                name="First of all, please type `//help`",
                value="Welcome to world of CPUchain tipbot !")
            embed.set_thumbnail(url=self.bot.user.avatar_url_as(format='png', size=1024))
            embed.set_footer(text="CPUchain tipbot {0} [Owner: {1}]".format(config.VERSION, self.bot.get_user(config.OWNER_ID)),
                             icon_url=self.bot.user.avatar_url_as(format='png', size=256))

            await ctx.channel.send(embed=embed)
        else:
            pass

            account = str(ctx.author.id)
            balance = Decimal(client.getbalance(account, config.CONFIRM))

            if address is None:
                embed = discord.Embed(color=0xffd800)
                embed.set_author(
                    name=ctx.author.display_name,
                    icon_url=ctx.author.avatar_url_as(format='png', size=256))
                embed.add_field(
                    name="Please check `//help` ",
                    value=" :mag: ")
                embed.set_footer(text="CPUchain tipbot {0} [Owner: {1}]".format(config.VERSION, self.bot.get_user(config.OWNER_ID)),
                                 icon_url=self.bot.user.avatar_url_as(format='png', size=256))

                await ctx.channel.send(embed=embed)
            else:
                pass

                if balance < Decimal('0.5'):
                    embed = discord.Embed(color=0xff0000)
                    embed.set_author(
                        name=ctx.author.display_name,
                        icon_url=ctx.author.avatar_url_as(format='png', size=256))
                    embed.add_field(
                        name="Amount must be at least 0.5 CPU.",
                        value="Your balances : ```{0} CPU```".format(client.getbalance(account, config.CONFIRM)))
                    embed.set_footer(text="CPUchain tipbot {0} [Owner: {1}]".format(config.VERSION, self.bot.get_user(config.OWNER_ID)),
                                     icon_url=self.bot.user.avatar_url_as(format='png', size=256))

                    await ctx.channel.send(embed=embed)
                else:
                    amount = balance - Decimal(str(config.FEE))
                    validate = client.validateaddress(address)

                    if not validate['isvalid']:
                        embed = discord.Embed(color=0xff0000)
                        embed.set_author(
                            name=ctx.author.display_name,
                            icon_url=ctx.author.avatar_url_as(format='png', size=256))
                        embed.add_field(
                            name="invalid address.",
                            value="`{0}`".format(str(address)))
                        embed.set_footer(text="CPUchain tipbot {0} [Owner: {1}]".format(config.VERSION, self.bot.get_user(config.OWNER_ID)),
                                         icon_url=self.bot.user.avatar_url_as(format='png', size=256))

                        await ctx.channel.send(embed=embed)
                    else:
                        txid = client.sendfrom(account, address, float(amount))
                        tx = client.gettransaction(txid)
                        txfee = tx['fee']

                        client.move(account, "tipcpu_wallet", Decimal(str(config.FEE)))
                        client.move("tipcpu_wallet", account, -txfee)

                        embed = discord.Embed(
                            title="**Block explorer**",
                            url='https://explorer.cpuchain.org/tx/{0}'.format(txid),
                            color=0x0043ff)
                        embed.set_author(
                            name=ctx.author.display_name,
                            icon_url=ctx.author.avatar_url_as(format='png', size=256))
                        embed.add_field(
                            name="Withdrawal complete `{0} CPU`\nwithdraw fee is `{1} CPU`\nPlease check the transaction at the above link.".format(amount, str(config.FEE)),
                            value="Your balances : `{0} CPU`".format(client.getbalance(account, config.CONFIRM)))
                        embed.set_footer(text="CPUchain tipbot {0} [Owner: {1}]".format(config.VERSION, self.bot.get_user(config.OWNER_ID)),
                                         icon_url=self.bot.user.avatar_url_as(format='png', size=256))

                        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Withdrawal(bot))
