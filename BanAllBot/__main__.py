from BanAllBot import app
from pyrogram import filters,enums

@app.on_message(filters.command("start"))
async def start(_,msg):
    await msg.reply_text("i am under creation by [ᏚᎢᎪᏒᏦ](https://t.me/NoobStark_21)")

    



if __name__ == "__main__":
    print("started")
    app.run()
