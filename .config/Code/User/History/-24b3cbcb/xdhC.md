# sensor.rs
All methods in these files could theoreicaly read data form all available sensors for the lego mindstorms. It is recocmende to check [this](https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/sensor_data.html) page on the ev3dev site to understand where a sensor sends it's data, how to read it and wich available mode there are.

## the mehods
### ```attatch(port: &str) -> Sensor```
This metod is reqired to 