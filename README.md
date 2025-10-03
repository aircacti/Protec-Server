# 🛡 Protec‑Server

A lightweight REST API server for reporting device status, managing security modes, and monitoring health.

---

## 🚀 Features

- **Status API** — `/status` endpoint, accessible without authorization  
- **Mode management** — `normal` / `lockdown` / `shutdown`  
- **Token-based authorization** — changing mode requires `Authorization: Bearer <token>` header  
- **Health monitoring** — collecting and reporting device/module status  
- **Simple database** — SQLite or other lightweight storage for states  
- **Easy configuration** — via `config.yaml` file

---


## 🔐 Testing

- **GET** `/status`  
  Check if the server is running, no auth required.

  ```bash
  curl http://127.0.0.1:2016/status/
  ```

- **GET** `/mode/current`  
  Requires header:

  ```
  Authorization: Bearer supersecrettoken123
  ```

  Example:

  ```bash
  curl -H "Authorization: Bearer supersecrettoken123" http://127.0.0.1:2016/mode/current
  ```

---

## 👍 Why use it?

- Simple and minimalistic
- Lightweight and easy to deploy
- Easy integration via REST

