import os
from dotenv import load_dotenv

load_dotenv()

# Токен бота от @BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN", "ВАШ_ТОКЕН_БОТА")

# ID супергруппы администрации (с включенными форумами/топиками)
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID", "-1001234567890"))

# ID канала для публикации постов
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1009876543210"))

# Список Telegram ID администраторов
ADMIN_IDS = [
    int(x.strip())
    for x in os.getenv("ADMIN_IDS", "123456789").split(",")
    if x.strip().lstrip("-").isdigit()
]

# Автоматическая подпись под постом в формате HTML
DEFAULT_FOOTER = (
    "предложить пост : @Freakcrimeabot\n\n"
    "удалить / узнать пост: @Freakcrimeabot\n\n"
    '📢 <a href="https://t.me/Freakcrimea">Фрики Крыма</a>'
)

POST_FOOTER = os.getenv("POST_FOOTER", DEFAULT_FOOTER).replace("\\n", "\n")