/*
 * 🏺 LILIETH PI: Sensory Eye Node (ESP32-S3 Cam)
 * Mandate: Zero-Latency Video/Audio Relay via 9CU Graphene Antenna.
 */

#include "esp_camera.h"
#include <WiFi.h>
#include <WiFiUdp.h>

const char* ssid = "SOVEREIGN_MESH";
const char* password = "THE_29TH_NODE";
WiFiUDP udp;
const char* pi_ip = "192.168.1.100"; // Pi 5 IP

void setup() {
  Serial.begin(115200);
  
  // 94. 9CU Graphene Antenna Handshake
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("[ANTENNA] Tuning 9CU Graphene Frequency...");
  }
  Serial.println("[LINK] OAKLEY EYE SYNCED TO GRID.");
}

void loop() {
  camera_fb_t * fb = esp_camera_fb_get();
  if (fb) {
    // 95. UDP 'Scream' Protocol (Zero-Lag Transmission)
    udp.beginPacket(pi_ip, 5005);
    udp.write(fb->buf, fb->len);
    udp.endPacket();
    esp_camera_fb_return(fb);
  }
}
