#include <ADS1299.h>
#include <BLEDevice.h>

ADS1299 eegSensor;
BLEServer *neuroServer;

void setup() {
  Serial.begin(115200);
  eegSensor.begin(ADS1299_CS_PIN, ADS1299_START_PIN);
  BLEDevice::init("Neurofluid-EEG");
  neuroServer = BLEDevice::createServer();
  // ... código completo de inicialização
}

void loop() {
  float eegData[8];
  eegSensor.readData(eegData);
  // ... processamento e transmissão
}
