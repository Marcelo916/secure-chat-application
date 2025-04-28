# Secure Chat Application using TLS and Mininet

## 📁 Project Structure

- `certificate_generation.py` — Generates server certificates.
- `legacy_network.py` — Builds the network in Mininet.
- `tpa4_chat_server.py` — Secure chat server.
- `tpa4_chat_client.py` — Secure chat client.

---

## 🚀 How It Works

1. Certificates are created.
2. Mininet topology is built.
3. Server and clients communicate over TLS.

---

## 🛠 Prerequisites

- Python 3.6+
- Mininet
- OpenSSL
- `python-hosts` library

Install `python-hosts` using:

```bash
pip install python-hosts
sudo -E python3 legacy_network.py
Type your hostname when prompted.
Chat server and clients will automatically open.
To exit the chat, type bye.
