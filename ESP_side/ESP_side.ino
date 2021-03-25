#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

ESP8266WebServer server;
uint8_t red_led = D2;
uint8_t blue_led = D0;
uint8_t green_led = D1;
const char* ssid = "HOME-C98C";  // Enter SSID here
const char* password = "642362C2EE97C74D";  //Enter Password here

void setup()
{
  pinMode(red_led, OUTPUT);
  pinMode(blue_led, OUTPUT);
  pinMode(green_led, OUTPUT);
  WiFi.begin(ssid,password);
  Serial.begin(115200);
  while(WiFi.status()!=WL_CONNECTED)
  {
    Serial.print(".");
    delay(500);
  }
  Serial.println("");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  server.on("/",[](){server.send(200,"text/plain","Hello World!");});
  server.on("/toggle",toggleLED);
  server.on("/jblink",jBlinkLED);
  server.on("/qblink",qBlinkLED);
  server.begin();
}

void loop()
{
  server.handleClient();
}

void RGB_color(int red_light_value, int green_light_value, int blue_light_value)
 {
  analogWrite(red_led, red_light_value);
  analogWrite(green_led, green_light_value);
  analogWrite(blue_led, blue_light_value);
}

void toggleLED()
{
  //digitalWrite(pin_led,!digitalRead(pin_led));
  server.send(204,"");
}

void jBlinkLED()
{
  String data = server.arg("plain");
  StaticJsonDocument<200> doc;
  // jBuffer.parseObject(data);
  deserializeJson(doc, data);
  JsonObject jObject = doc.as<JsonObject>();
  String red = jObject["r"];
  String blue = jObject["b"];
  String green = jObject["g"];
  
  RGB_color(red.toInt(), green.toInt(), blue.toInt());
  

  server.send(200,"text/plain","GOT THE DATA!"); 
}

void qBlinkLED()
{
  String del = server.arg("pause");
  String n = server.arg("times");
  for (int i=0; i<n.toInt();i++)
  {
   //digitalWrite(pin_led,!digitalRead(pin_led));
   delay(del.toInt()); 
  }
}
