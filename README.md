## Quick Start

Clone the repository:

# wifi-presence-security-homeassistant
This project combines WiFi-based presence detection (via router scanning, ESPHome on ESP32 for room-level accuracy, or CSI if advanced), Home Assistant as the central hub (running on a VPS or local machine), and Amazon Alexa/Echo for voice announcements/talk-back in occupied rooms.
<div align="center">

<img src="https://neo-shade.com/wp-content/uploads/2026/03/neoSHADE-home-security-banner.jpg" width="100%" />

# NeoSHADE Home Security System

### WiFi Presence Detection • Smart Home Security • Home Assistant Integration

AI-powered home security that detects **who is in your home and which room they are in** using WiFi presence detection and communicates through **Amazon Echo devices**.

Built on **Home Assistant + ESP32 + local network intelligence**.

<br>

![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge)
![Home Assistant](https://img.shields.io/badge/homeassistant-supported-green?style=for-the-badge)
![Security](https://img.shields.io/badge/security-network-orange?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-purple?style=for-the-badge)

</div>

---

# Overview

The **NeoSHADE Home Security System** is a privacy-first smart home security platform that uses **WiFi network awareness** instead of cameras to determine who is present in your home.

It continuously scans your network and detects:

• Who is home  
• Which room they are in  
• When unknown devices appear  
• When the house is empty  

The system can then automatically communicate through **Amazon Echo devices**.

Example messages:


"Welcome home JonnyG. Security system confirms you are in the living room."

"Alert. Unknown device detected in the bedroom."


Everything runs **locally on your network**.

No cloud tracking required.

---

# Core Features

### WiFi Presence Detection
Detects phones, laptops, and smart devices connected to your WiFi network.

### Room-Level Positioning
Uses signal strength from ESP32 sensors or multiple WiFi access points.

### Alexa Voice Announcements
Echo devices speak messages when someone enters a room.

### Unknown Device Detection
Alerts when an unrecognized device joins the network.

### Continuous Monitoring
System scans every few seconds to maintain real-time presence awareness.

### Local-First Security
Runs entirely on **Home Assistant + your own hardware**.

---

# System Architecture


Phones / Devices
│
▼
WiFi Network
│
▼
Router + ESP32 Presence Sensors
│
▼
Home Assistant Server
(VPS / Raspberry Pi)
│
├── Presence Detection
├── Automation Engine
└── Security Logic
│
▼
Amazon Echo Devices
(Room announcements)


---

# Hardware Requirements

Minimum setup:

• Home Assistant server (VPS or Raspberry Pi)  
• WiFi router  
• Smartphones or devices to track  
• Amazon Echo devices  

Recommended for room accuracy:

• ESP32 boards (1 per room)

Estimated cost:


ESP32 boards: $5 each
Home Assistant: free
Total system cost: ~$10–30


---

# Quick Start

## Install Home Assistant


docker run -d
--name homeassistant
--restart=unless-stopped
-v /config:/config
-e TZ=America/New_York
--network=host
ghcr.io/home-assistant/home-assistant:stable


Open the dashboard:


http://YOUR_SERVER_IP:8123


---

# Add Device Tracking

Inside Home Assistant:


Settings → Devices & Services → Add Integration


Add either:

• **Home Assistant Companion App**  
or  
• **Router integration** (ASUS, UniFi, TP-Link, etc)

Link devices to **Persons** in Home Assistant.

---

# Alexa Integration

Install **Alexa Media Player** using HACS.

Your Echo devices will appear as:


media_player.echo_living_room
media_player.echo_kitchen
media_player.echo_bedroom


Example automation:


service: tts.amazon_polly
data:
message: "Welcome home JonnyG. Security system confirms you are in the living room."
target: media_player.echo_living_room


---

# Room-Level Detection (ESPHome)

For more accurate room presence detection, deploy ESP32 nodes.

Example ESPHome configuration:


esphome:
name: livingroom-presence

wifi:
ssid: !secret wifi_ssid
password: !secret wifi_password

sensor:

platform: wifi_signal
name: "Living Room WiFi RSSI"
update_interval: 5s


These nodes allow Home Assistant to determine **exact room location**.

---

# Security Capabilities

The system can detect:

• Unknown devices joining the network  
• Presence when house should be empty  
• Device movement between rooms  
• Entry and exit timestamps  

Optional integrations:

• smart locks  
• alarm systems  
• security lighting  
• camera triggers  

---

# Repository Structure


wifi-presence-security-homeassistant
│
├── README.md
├── LICENSE
│
├── esphome
│ ├── kitchen.yaml
│ ├── livingroom.yaml
│ └── bedroom.yaml
│
├── automations
│ └── presence_announcements.yaml
│
├── docker
│ └── docker-compose.yml
│
└── docs
└── architecture.md


---

# Future Development

Planned improvements:

• WiFi CSI motion sensing  
• AI behavior recognition  
• multi-home dashboards  
• NeoSHADE mobile interface  
• visual positioning integration

---

# Philosophy

Most smart home security platforms rely heavily on cloud services.

NeoSHADE proves you can build a powerful security system **locally** using open tools.

Goals:


Privacy
Transparency
Control
Security


---

# License

MIT License

---

<div align="center">

### NeoSHADE AI

Building intelligent systems that protect and empower modern homes.

</div>
