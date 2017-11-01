
void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}
uint8_t data[5] = {100, 111, 255, 123, 233};

String data_ =  {"100,123,1,  22,180"};
String data_2 = {"129,123,160,194,92"};
String data_3 = {"130,23, 15, 204,132"};
String data_4 = {"200,13, 255,224,142"};
String data_5 = {"234,233,145,0,122"};
String data_6=  {"245,50, 45, 101,142"};
String data_7 = {"40,99,  245,187,222"};

unsigned long long timer = 0;

void loop()
{
  if (millis() - timer > 3000)
  {
    
      Serial.println(data_);
      Serial.println(data_2);
      Serial.println(data_3);
      Serial.println(data_4);
      Serial.println(data_5);
      Serial.println(data_6);
      Serial.println(data_7);
      
    timer = millis();

    }
   
while(Serial.available())
{
  char c = Serial.read(); 
  if (c == 'd')
  {
    digitalWrite(13, HIGH);
    delay(100);
    digitalWrite(13, LOW);
    delay(100);
  }
  
  else
  {
    digitalWrite(13, LOW);
  }
 }
}




