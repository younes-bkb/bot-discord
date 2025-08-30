import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command()
async def bonjour(ctx):
    await ctx.send(f"Bonjour {ctx.author} !")


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong !")


@bot.command()
async def pileouface(ctx):
    await ctx.send(random.choice(["Pile", "Face"]))


@bot.command(
    help="Lance un dé cubique",
    description="Lance un dé et renvoie le résultat entre 1 et 6 compris")
async def roll(ctx):
    await ctx.send(random.randint(1, 6))


@bot.command(
    help="Efface tous les messages du salon",
    description="Supprime tous les messages du salon actuel (nécessite les permissions de gestion des messages)")
async def clear(ctx, amount=None):
    # Vérifier si l'utilisateur a les permissions nécessaires
    if not ctx.author.guild_permissions.manage_messages:
        await ctx.send("❌ Vous n'avez pas la permission de gérer les messages !")
        return

    try:
        if amount is None:
            # Supprimer tous les messages (par batch de 100 max à cause des limitations Discord)
            deleted = await ctx.channel.purge(limit=None)
            await ctx.send(f"✅ {len(deleted)} messages ont été supprimés !", delete_after=5)
        else:
            # Supprimer un nombre spécifique de messages
            amount = int(amount)
            if amount <= 0:
                await ctx.send("❌ Le nombre doit être supérieur à 0 !")
                return

            deleted = await ctx.channel.purge(limit=amount + 1)  # +1 pour inclure la commande
            await ctx.send(f"✅ {len(deleted)} messages ont été supprimés !", delete_after=5)

    except discord.Forbidden:
        await ctx.send("❌ Je n'ai pas les permissions pour supprimer les messages !")
    except discord.HTTPException:
        await ctx.send("❌ Une erreur s'est produite lors de la suppression des messages.")
    except ValueError:
        await ctx.send("❌ Veuillez entrer un nombre valide !")


token = "MonToken"
bot.run(token)