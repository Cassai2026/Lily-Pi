#include "esp_camera.h"
#include <WiFi.h>
#include <WiFiUdp.h>

const char* ssid = "SOVEREIGN_MESH";
const char* password = "THE_29TH_NODE";
WiFiUDP udp;
const char* pi_ip = "192.168.1.100"; 

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) { delay(500); }
}

void loop() {
  camera_fb_t * fb = esp_camera_fb_get();
  if (fb) {
    udp.beginPacket(pi_ip, 5005);
    udp.write(fb->buf, fb->len);
    udp.endPacket();
    esp_camera_fb_return(fb);
  }
}
