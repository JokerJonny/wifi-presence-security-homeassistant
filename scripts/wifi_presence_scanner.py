import subprocess
import time
import json
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "neoshade/presence"

KNOWN_DEVICES = {
    "AA:BB:CC:DD:EE:FF": "JonnyG",
    "11:22:33:44:55:66": "Family"
}

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT)


def scan_network():
    try:
        result = subprocess.check_output(["arp", "-a"]).decode()
        lines = result.split("\n")

        detected = []

        for line in lines:
            for mac in KNOWN_DEVICES:
                if mac.lower() in line.lower():
                    detected.append(KNOWN_DEVICES[mac])

        return detected

    except Exception as e:
        print("Scan error:", e)
        return []


def publish_presence(people):
    payload = json.dumps({
        "people": people,
        "count": len(people)
    })

    client.publish(MQTT_TOPIC, payload)


def main():
    while True:
        people = scan_network()

        if people:
            print("Detected:", people)
        else:
            print("No known devices")

        publish_presence(people)

        time.sleep(10)


if __name__ == "__main__":
    main()
