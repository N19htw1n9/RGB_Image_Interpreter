#include <ArduinoJson.h>
#include <LiquidCrystal.h>
#define speed8266 115200 // This is the speed that worked with my ESP8266

uint8_t red_led = 11;
uint8_t blue_led = 6;
uint8_t green_led = 10;
//bool isButtonA = false, isButtonB = false;
const int debounce = 250; //this is a huge delay, but it seems to fix my debounce
unsigned long pressTimeA = 0;
unsigned long pressTimeB = 0;
int button_ahead = 3, button_back = 2;
const int rs = 7, en = 8, d4 = 5, d5 = 4, d6 = 9, d7 = 12;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
int colorCount = 0;
int curColor = 0;

//store all the received colors in an array
struct color{
  int red;
  int blue;
  int green;
} colorArr[5];



//display the next color. If the last color is reached, go back to the first one
void skipAhead(){
  if (millis() - pressTimeA > debounce)
  {
    curColor++;
    if (curColor == colorCount) curColor = 0;
    lcd_color_print(colorArr[curColor].red, colorArr[curColor].green, colorArr[curColor].blue);
    RGB_color(colorArr[curColor].red, colorArr[curColor].green, colorArr[curColor].blue);
    pressTimeA = millis();
  }
}

//display the previous color. If the first color is reached, go back to the last one
void skipBack(){
  if (millis() - pressTimeB > debounce)
  {
    curColor--;
    if (curColor < 0) curColor = colorCount - 1;
    lcd_color_print(colorArr[curColor].red, colorArr[curColor].green, colorArr[curColor].blue);
    RGB_color(colorArr[curColor].red, colorArr[curColor].green, colorArr[curColor].blue);
    pressTimeB = millis();
  }
}

void setup() {
  // put your setup code here, to run once:
  //initialize serial
  Serial.begin(speed8266);
  //initialize RGB LED's pins
  pinMode(red_led, OUTPUT);
  pinMode(blue_led, OUTPUT);
  pinMode(green_led, OUTPUT);
  //iitialize LCD
  lcd.begin(16, 2);
  //set up button interrupts
  attachInterrupt(digitalPinToInterrupt(button_back), skipBack, RISING);
  attachInterrupt(digitalPinToInterrupt(button_ahead), skipAhead, RISING);
}



//set the RGB LED's color
void RGB_color(int red_light_value, int green_light_value, int blue_light_value)
 {
  analogWrite(red_led, red_light_value);
  analogWrite(green_led, green_light_value);
  analogWrite(blue_led, blue_light_value);
}

//add a new color to the array
void addColor(int red_light_value, int green_light_value, int blue_light_value)
 {
  //if the maximum number of colors is already stored, overwrite old values starting with the first one
  if (colorCount == 5) colorCount = 0;
  colorArr[colorCount].red = red_light_value;
  colorArr[colorCount].green = green_light_value;
  colorArr[colorCount].blue = blue_light_value;
  colorCount++;
 }

//print the color's RGB values on screen
void lcd_color_print(int red_light_value, int green_light_value, int blue_light_value){
    lcd.clear();
    lcd.print("R: " + String(red_light_value) + " G: " + String(green_light_value)); //the name is always the same
    lcd.setCursor(0, 1);
    lcd.print("B: " + String(blue_light_value));
}

void loop() {
  // put your main code here, to run repeatedly:
   if (Serial.available()){
      String data = Serial.readString();  
      Serial.println(data);
      StaticJsonDocument<200> doc;
      deserializeJson(doc, data);
      JsonObject jObject = doc.as<JsonObject>();
      if (jObject.isNull()) return;
      String red = jObject["r"];
      String blue = jObject["b"];
      String green = jObject["g"];
      addColor(red.toInt(), green.toInt(), blue.toInt());
      curColor = colorCount-1;
      lcd_color_print(colorArr[curColor].red, colorArr[curColor].green, colorArr[curColor].blue);
      RGB_color(colorArr[curColor].red, colorArr[curColor].green, colorArr[curColor].blue);
   }
   
}
