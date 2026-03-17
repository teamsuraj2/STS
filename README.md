# String-Session-Bot

Telegram bot to generate **Pyrogram** and **Telethon** string sessions.

> A star ⭐ from you means a lot!

[![ForTheBadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/teamsuraj2)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

---

## ✨ Features

- Generate **Pyrogram** string sessions
- Generate **Telethon** string sessions
- MongoDB-based user database
- Admin tools:
  - `/stats` – total users
  - `/speedtest` – server speed test (admin only)
  - `/broadcast` – broadcast message to all users (admin only)
- Optional force join (`MUST_JOIN`)
- Fully async, Pyrogram 2.x compatible
- No SQL, no Pyromod, no legacy dependencies

---

## 📚 Framework Docs

- Pyrogram: https://docs.kurigram.icu/
- Telethon: https://docs.telethon.dev/

---

## 🚀 Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://www.heroku.com/deploy?template=https://github.com/teamsuraj2/STS)

### Deploy to Heroku (Eco or higher)

Use your own repo:

https://github.com/teamsuraj2/STS

Make sure your `app.json` and `Procfile` are present, then deploy normally from GitHub.

### Local Deploy

1. Clone the repo:
   ```bash
   https://github.com/teamsuraj2/STS
   cd STS
