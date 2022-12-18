/*
Lora ARNia
*/
//https://www.rapidtables.com/convert/number/hex-to-ascii.html

#include <MKRWAN.h>

LoRaModem modem;

// Uncomment if using the Murata chip as a module
// LoRaModem modem(Serial1);

String appEui;
String appKey;
String devAddr;
String nwkSKey;
String appSKey;

void setup() {
  // put your setup code here, to run once:
  //Serial.begin(115200);
  //while (!Serial);
  //Serial.println("Welcome to MKR WAN 1300/1310 first configuration sketch");
  //Serial.println("Register to your favourite LoRa network and we are ready to go!");
  // change this to your regional band (eg. US915, AS923, ...)
  if (!modem.begin(EU868)) {
    //Serial.println("Failed to start module");
    while (1) {}
  };
  //Serial.print("Your module version is: ");
  //Serial.println(modem.version());
  //if (modem.version() != ARDUINO_FW_VERSION) {
  //  Serial.println("Please make sure that the latest modem firmware is installed.");
  //  Serial.println("To update the firmware upload the 'MKRWANFWUpdate_standalone.ino' sketch.");
  //}
  //Serial.print("Your device EUI is: ");
  //Serial.println(modem.deviceEUI());

  int mode = 1;
  int connected=false;
  while (!connected) {
    
  
    appEui = xxx
    appKey = yyy

    appKey.trim();
    appEui.trim();

    connected = modem.joinOTAA(appEui, appKey);


    if (!connected) {
  //    Serial.println("not connected - retry");
      delay(60*1000);
    }
  }
  
}

void loop() {
  int err;
  int number;
  number = rand() % 100;
  //Serial.println(number);
  modem.setPort(1);
  modem.beginPacket();
  modem.print(number);
  err = modem.endPacket(true);
  if (err > 0) {
  //  Serial.println("Message sent correctly!");
  } else {
  //  Serial.println("Error sending message :(");
  }
  delay(20*60*1000);
}