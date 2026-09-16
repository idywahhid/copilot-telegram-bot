![Copilot Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)
![Python](https://img.shields.io/badge/Python-3.9%2B-green)
![aiogram](https://img.shields.io/badge/aiogram-3.9-yellow)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Latest-336791)

# 🤖 Copilot Telegram Bot

GitHub Copilot bilan ishlash uchun yaratilgan Telegram bot. aiogram 3.9 va PostgreSQL bilan ishlaydi.

## 🚀 Imkoniyatlar

- ✅ Telegram bot integratsiyasi
- ✅ PostgreSQL database
- ✅ Foydalanuvchi sessiyalari
- ✅ Xabar tarixi saqlash
- ✅ GitHub Copilot integratsiyasi (qo'shimcha)
- ✅ Asinxron ishlash (async/await)

## 📋 Talablar

- Python 3.9+
- PostgreSQL 12+
- Telegram Bot Token

## 🔧 O'rnatish

### 1. Repository klonlash

```bash
git clone https://github.com/idywahhid/copilot-telegram-bot.git
cd copilot-telegram-bot
```

### 2. Virtual environment yaratish

```bash
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Dependensiyalarni o'rnatish

```bash
pip install -r requirements.txt
```

### 4. .env fayl yaratish

```bash
cp .env.example .env
```

`.env` faylini to'ldiring:

```env
BOT_TOKEN=your_telegram_bot_token
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=copilot_bot
```

### 5. PostgreSQL database yaratish

```bash
createdb copilot_bot
```

## ▶️ Botni ishga tushirish

```bash
python main.py
```

## 📁 Loyiha strukturasi

```
copilot-telegram-bot/
├── main.py              # Asosiy bot fayli
├── config.py            # Konfiguratsiya
├── models.py            # Database modellari
├── requirements.txt     # Python dependensiyalari
├── .env.example         # Environment o'zgaruvchilari
├── database/
│   └── __init__.py      # Database konfiguratsiyasi
├── handlers/
│   ├── __init__.py
│   ├── commands.py      # Komanda handlerlari
│   └── messages.py      # Xabar handlerlari
└── README.md           # Bu fayl
```

## 📝 Komandalar

- `/start` - Botni boshlash
- `/help` - Yordam olish
- `/me` - Profil ma'lumotlari
- `/clear` - Suhbatni o'chirish
- `/status` - Bot holati

## 🗄️ Database struktura

### Users jadvali
- `id` - Primary key
- `telegram_id` - Telegram user ID
- `username` - Telegram username
- `first_name` - Foydalanuvchining ismi
- `last_name` - Foydalanuvchining familyasi
- `is_active` - Faolligi holati
- `created_at` - Yaratilgan vaqti
- `updated_at` - Oxirgi yangilangan vaqti

### Messages jadvali
- `id` - Primary key
- `user_id` - Foydalanuvchi ID
- `telegram_id` - Telegram user ID
- `content` - Xabar matni
- `response` - Bot javobi
- `created_at` - Yaratilgan vaqti

### Sessions jadvali
- `id` - Primary key
- `user_id` - Foydalanuvchi ID
- `telegram_id` - Telegram user ID
- `is_active` - Sessiya holati
- `context` - Sessiya konteksti
- `created_at` - Yaratilgan vaqti
- `updated_at` - Oxirgi yangilangan vaqti

## 🔗 GitHub Copilot Integratsiyasi

GitHub Copilot integratsiyasini qo'shish uchun:

1. GitHub token ni `.env` faylga qo'shing
2. Copilot API chaqiruvlarini handlers fayllariga qo'shing
3. Test uchun botni ishga tushiring

## 🤝 Hissa qo'shish

Hissa qo'shishni xush kelibsiz! Pull request yuboring.

## 📄 Litsenziya

Bu loyiha MIT litsenziyasi bilan himoyalangan.

## 📧 Bog'lanish

Savollaringiz bo'lsa, issue ochib qo'ying yoki meni bog'lang.

---

**Ishlab chiquvchi:** [@idywahhid](https://github.com/idywahhid)

**Yaratildi:** 2026
