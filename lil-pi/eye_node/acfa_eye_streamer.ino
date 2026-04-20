#include <WiFi.h>
#include <WiFiUdp.h>

const char* ssid = "SOVEREIGN_MESH";
const char* password = "THE_29TH_NODE";
const char* pi_ip = "192.168.1.100"; // Update to your Pi 5 IP
const int port = 5005;

WiFiUDP udp;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) { delay(500); }
  Serial.println("[ACFA] EYE NODE ONLINE. 9CU ANTENNA ACTIVE.");
}

void loop() {
  // Capture the 42-Pulse Baseline & Environmental Static
  int current_hr = analogRead(34); // Heart Rate Sensor Pin
  int noise_level = analogRead(35); // MEMS Mic Pin
  
  // Pack data into a Sovereign Pulse
  int16_t data[2] = {(int16_t)current_hr, (int16_t)noise_level};
  
  udp.beginPacket(pi_ip, port);
  udp.write((uint8_t*)data, sizeof(data));
  udp.endPacket();
  
  delay(100); // 10Hz Sync
}
