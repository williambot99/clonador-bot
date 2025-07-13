import asyncio
from telethon import TelegramClient, events
from telethon.tl.types import Message

api_id = 25898839
api_hash = '699f51fea67c98f94c5b4f08cf8ea9ef'
session_name = 'clonador_session'

grupos_origem = {
    -1002008424849: "Fire TV - Oficial",
    -1002150781193: "Rush Play Oficial",
    -1001466611266: "BLAZE | Atualizações",
    -1001585223484: "Central/BRAZ/FIVE informativo",
    -1001308547232: "BLADE UHD Informative",
    -1001771511490: "Uniplay UHD",
    -1002257239595: "DBOXTV",
    -1002173241816: "Avisos DG",
    -1001916474686: "Canal Apoio",
    -1002684878729: "LIVE 21",
    -1002389967565: "GOCine",
    -1001857217396: "OPERA OFICIAL",
    -1002221984640: "Yellow-Box",
    -1001521617997: "NEW TVS OFICIAL",
    -1002388555664: "NEKO TV",
    -1001787129919: "PlayOn",
    -1001481981505: "Suporte e Aviso",
    -1002327952083: "Alpha Play Oficial",
    -1001307910478: "P2Speed",
    -1001283502666: "Bit",
    -1002041575742: "Power Play",
    -1002180440597: "Power banner",
    -1002183858471: "E3 PLAY OFICIAL",
    -1001811727929: "TVs Original"
}

grupo_destino = -1002682285509
usuario = "@WilliamMaster94"

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=list(grupos_origem.keys())))
async def handler(event):
    try:
        nome_origem = grupos_origem.get(event.chat_id, "Servidor Desconhecido")
        if event.message.media:
            await client.send_file(
                grupo_destino,
                file=event.message.media,
                caption=(event.message.text or "") + f"\n\n📣 {usuario} — Servidor: {nome_origem}"
            )
        else:
            await client.send_message(
                grupo_destino,
                message=event.message.text + f"\n\n📣 {usuario} — Servidor: {nome_origem}"
            )
    except Exception as e:
        print(f"Erro ao encaminhar mensagem: {e}")

print("Bot rodando... Escutando mensagens.")
client.start()
client.run_until_disconnected()