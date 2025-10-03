# 🛡 Protec‑Server

A lightweight REST API server for reporting device status, managing security modes, and monitoring health.


## 🚀 About

- **Status API** — `/status` endpoint, accessible without authorization  
- **Mode management** — `normal` / `lockdown` / `shutdown`  
- **Token-based authorization** — changing mode requires `Authorization: Bearer <token>` header  
- **Health monitoring** — collecting and reporting device/module status  
- **Simple database** — SQLite local storage
- **Easy configuration** — via `config.yaml` file

---

## 🗂 Project Structure

- **🟢 Core Files**  
  The files responsible for the program's functionality are located in the `core/` folder.  
  The main entry point of the application is `main.py`.  

- **🟡 Local Files**  
  All instance-specific files, such as configuration files, databases, or other user-specific data, are stored in the `local/` folder.  
  
This separation helps prevent accidental changes that could break the program.  

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

