import discord
from discord.ext import commands
from discord import app_commands
import random

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

# Store user data in-memory (balance and recharges)
user_data = {}

def init_user(user_id):
    if user_id not in user_data:
        user_data[user_id] = {"balance": 100, "recharges": 3}

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "🌟"]
    return [random.choice(symbols) for _ in range(3)]

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:
            case "🍒": return bet * 2
            case "🍉": return bet * 3
            case "🍋": return bet * 4
            case "🔔": return bet * 5
            case "🌟": return bet * 6
    return 0

class SlotView(discord.ui.View):
    def __init__(self, user_id):
        super().__init__(timeout=120)
        self.user_id = user_id

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("This is not your game session.", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="Spin ($50)", style=discord.ButtonStyle.green)
    async def spin(self, interaction: discord.Interaction, button: discord.ui.Button):
        init_user(self.user_id)
        user = user_data[self.user_id]
        bet = 50

        if user["balance"] < bet:
            await interaction.response.send_message("Not enough balance to spin.", ephemeral=True)
            return

        user["balance"] -= bet
        row = spin_row()
        payout = get_payout(row, bet)
        user["balance"] += payout

        result = " | ".join(row)
        msg = f"🎰 {result} 🎰\n"
        msg += f"{'You won' if payout > 0 else 'You lost'} ${payout or 0}!\n"
        msg += f"Balance: ${user['balance']}"

        await interaction.response.edit_message(content=msg, view=self)

    @discord.ui.button(label="Recharge (+$100)", style=discord.ButtonStyle.blurple)
    async def recharge(self, interaction: discord.Interaction, button: discord.ui.Button):
        init_user(self.user_id)
        user = user_data[self.user_id]

        if user["recharges"] <= 0:
            await interaction.response.send_message("No recharges left.", ephemeral=True)
            return

        user["balance"] += 100
        user["recharges"] -= 1
        await interaction.response.send_message(f"Recharged $100. Balance: ${user['balance']}, Recharges left: {user['recharges']}", ephemeral=True)

@tree.command(name="start", description="Start playing the slot machine")
async def start(interaction: discord.Interaction):
    user_id = interaction.user.id
    init_user(user_id)
    bal = user_data[user_id]["balance"]
    await interaction.response.send_message(f"Welcome! Your balance is ${bal}.", view=SlotView(user_id))

@tree.command(name="stats", description="Check your balance and recharges")
async def stats(interaction: discord.Interaction):
    user_id = interaction.user.id
    init_user(user_id)
    user = user_data[user_id]
    await interaction.response.send_message(f"Balance: ${user['balance']}, Recharges left: {user['recharges']}", ephemeral=True)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Bot is online as {bot.user}.")

# Replace with your Discord bot token
bot.run(" --- YOUR BOT TOKEN --- ")
