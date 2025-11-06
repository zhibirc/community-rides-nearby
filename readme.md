> [!WARNING]  
> Boilerplate Project.
> This repository is a starter template, not a fully functional application.
> It provides structure, interfaces, and example handlers, but key logic and storage implementation are intentionally incomplete.
> You need to fork/clone and implement unfinished parts before deployment.

# Community Rides Nearby

<p align="center">
Enable local community members to share their spare car seats with neighbors. We aim to reduce empty trips, strengthen mutual support, and promote a more eco-friendly lifestyle.
</p>

---

## 🚗 What is Community Rides Nearby?

**Community Rides Nearby** is a simple Telegram-based ride-sharing helper designed for local communities.  
Drivers can publish available rides through a Telegram bot, and all rides are automatically posted to a public Telegram channel where passengers can respond.

No registrations, no separate apps, no personal data harvesting — just a lightweight tool to connect people going in the same direction.

---

## Key Features

✅ **Drivers-only bot**
  - Submit available rides via conversation wizard
  - Parameters include: start, destination, free seats, time range, optional comment
  - Review, adjust and delete existing rides

✅ **Automatic channel posting**
  - Newly created rides appear in a public Telegram channel
  - Passengers reply via comments or via private messaging

✅ **Persistent storage**
  - Rides are stored in a database (MongoDB recommended, but storage is pluggable)
  - Schema-light: easy to evolve as the project grows

✅ **Minimal operational cost**
  - Single-process architecture (bot + storage)
  - Runs on a tiny VM
  - No extra backend API required

✅ **Privacy-friendly**
  - No user registration
  - No tracking
  - No phone-number exposure beyond Telegram

## Bot Commands

| Command   | Description                             |
| --------- | --------------------------------------- |
| /start    | Welcome text + help                     |
| /create   | Create a new ride (wizard)              |
| /update   | Update an existing ride                 |
| /list     | List active rides                       |
| /list_all | List all rides (history)                |
| /delete   | Remove/cancel a previously created ride |
| /cancel   | Cancel current wizard                   |

## 🛡️ Security

- Only Telegram `user_id` is stored, no sensitive data.
- No authentication required beyond Telegram.
- No cookies, phone, or email needed.
- Communication user-driver happens directly in Telegram.
- Data is not shared anywhere else.

## 🤝 Contributing

PRs and issues are welcome.

## 📄 License

MIT

---

<p align="center">Made with ❤️ in Romania.</p>
