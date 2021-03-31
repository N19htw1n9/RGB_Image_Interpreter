#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

ESP8266WebServer server;
//this is private anyways, but don't forget to obscure this if the code ever goes public
const char* ssid = "HOME-C98C";  // Enter SSID here
const char* password = "642362C2EE97C74D";  //Enter Password here

void setup()
{
  WiFi.begin(ssid,password);
  Serial.begin(115200);
  //because Serial gets occupied with the USB (needed to know the wi-fi address), use Serial2 to communicate with UNO
 // Serial2.begin(115200);
  while(WiFi.status()!=WL_CONNECTED)
  {
    Serial.print(".");
    delay(500);
  }
  //Serial.println("");
  //Serial.print("IP Address: ");
  //Serial.println(WiFi.localIP());
  //add a new action to the server as a specific command is requested
  server.on("/",[](){server.send(200,"text/plain","Hello World!");});
  server.on("/jblink",jBlinkLED);
  server.begin();
}

void loop()
{
  //let the server handle connections
  server.handleClient();
}


void jBlinkLED()
{
  //get date from the wi-fi connection
  String data = server.arg("plain");
  //send it to the UNO via the serial
  Serial.println(data);
  //tell the server that the data was received
  server.send(200,"text/plain","GOT THE DATA!"); 
  delay(1000);
}
