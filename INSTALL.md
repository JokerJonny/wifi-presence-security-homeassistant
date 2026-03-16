# Installation Guide

This guide walks through installing and running the **NeoSHADE WiFi Presence Security System**.

The system can run on:

• Raspberry Pi  
• Home server  
• VPS  
• Docker host  
• any Linux system running Home Assistant

---

# 1. Requirements

Minimum requirements

• Python 3.10+  
• Docker (recommended)  
• Home Assistant  
• WiFi router with connected devices

Optional hardware for room-level tracking

• ESP32 boards

---

# 2. Clone the Repository

```bash
git clone https://github.com/JokerJonny/wifi-presence-security-homeassistant.git
cd wifi-presence-security-homeassistant
```

---

# 3. Configure Environment Variables

Copy the example environment file.

```bash
cp .env.example .env
```

Edit the file with your network settings.

Example:

```
MQTT_BROKER=localhost
MQTT_PORT=1883
HOME_ASSISTANT_URL=http://localhost:8123
```

---

# 4. Install Python Dependencies

Create a virtual environment.

```bash
python -m venv venv
```

Activate the environment.

Linux / macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install required packages.

```bash
pip install -r requirements.txt
```

---

# 5. Start Supporting Services (Docker)

If using Docker, start the Home Assistant stack.

```bash
docker compose up -d
```

This launches the required containers.

---

# 6. Run the WiFi Presence Scanner

Start the scanner script.

```bash
python scripts/wifi_presence_scanner.py
```

The scanner will detect devices on your network and publish presence updates through MQTT.

---

# 7. Connect to Home Assistant

Open the Home Assistant dashboard.

```
http://YOUR_SERVER_IP:8123
```

Then add device tracking integrations.

Navigate to:

```
Settings → Devices & Services → Add Integration
```

Recommended integrations

• Home Assistant Companion App  
• Router Integration (UniFi, ASUS, TP-Link, etc)

---

# 8. Configure Automations

Automations can be found in:

```
automations/presence_announcements.yaml
```

These automations allow Echo devices or speakers to announce presence events.

Example:

```
Welcome home JonnyG.
Security system confirms you are in the living room.
```

---

# 9. Deploy ESP32 Sensors (Optional)

For room-level presence detection, deploy ESP32 nodes.

Example configuration files are located in:

```
esphome/
```

Flash the ESP32 devices using ESPHome.

These nodes report signal strength and improve room-level detection accuracy.

---

# 10. Verify the System

After installation you should see:

• devices appearing in Home Assistant  
• MQTT messages from the scanner  
• automations triggering on presence events  

---

# Troubleshooting

### Scanner not detecting devices

Ensure your system has permission to access the network.

Some routers block ARP scanning.

---

### MQTT not connecting

Check your broker settings in `.env`.

---

### Home Assistant not receiving updates

Verify MQTT integration is enabled inside Home Assistant.

---

# Next Steps

You can extend the system with:

• ESP32 room sensors  
• WiFi CSI motion detection  
• AI behavior analysis  
• smart alarm integrations  

---

NeoSHADE Home Security System  
Privacy-first smart home security.
