#![allow(dead_code)]
use crate::robot::files;
use std::fs::read_dir;

// these function will handel the ev3 brick hardware
#[allow(dead_code)]
static  LED_PATHS:[&str; 4] = ["/sys/class/leds/led0:green:brick-status/brightness", "/sys/class/leds/led0:red:brick-status/brightness", "/sys/class/leds/led1:green:brick-status/brightness", "/sys/class/leds/led1:red:brick-status/brightness"];

// these structs contain port definitions
#[allow(non_snake_case)]
pub struct Ports {
    pub in1: String,
    pub in2: String,
    pub in3: String,
    pub in4: String,

    pub outA: String,
    pub outB: String,
    pub outC: String,
    pub outD: String
}

impl Default for Ports {
    fn default() -> Ports {
        Ports { 
                in1: "ev3-ports:in1".to_string(),
                in2: "ev3-ports:in2".to_string(),
                in3: "ev3-ports:in3".to_string(),
                in4: "ev3-ports:in4".to_string(),
                
                outA: "ev3-ports:outA".to_string(),
                outB: "ev3-ports:outB".to_string(),
                outC: "ev3-ports:outC".to_string(),
                outD: "ev3-ports:outD".to_string() 
            }
    }
}

// function for resetting the brick
pub fn init() {
    clear_led();
    set_led(0, 255);
    set_led(2, 255);
    
    let paths = read_dir("/sys/class/tacho-motor/").unwrap();

    for path in paths {
        let path: String = path.as_ref().unwrap().path().display().to_string() + "/command";
        files::write_str(&path, "reset");
    }
    // ? maby add a hasmap in a struct and use it to autodetect available ports, or just hande standard ev3brick hardware.

}

// TODO: add functions to read buttons

// functions for controlling the LED's
pub fn clear_led() {
    for led in LED_PATHS {
        files::write_int(led, &0);
    }
}

pub fn set_led(led: usize, value: u8) {
    let address: &str = LED_PATHS[led];
    files::write_int(address, &(value as i64));
}

// function for getting information from the battery
pub fn current_battery() -> f64 {
    let current_now_micro: i64 = files::read_int("/sys/class/power_supply/lego-ev3-battery/current_now");
    let current_now:f64 = current_now_micro as f64 / 1000000 as f64;
    return current_now;
}

#[allow(non_snake_case)]
pub fn is_LiIon() -> bool {
    if files::read_str("/sys/class/power_supply/lego-ev3-battery/technology").trim() == "Li-ion" {
        return true;
    } else {
        return false;
    }
}

pub fn max_voltage_battery() -> f64{
    let max_voltage_micro: i64 = files::read_int("/sys/class/power_supply/lego-ev3-battery/voltage_max_design");
    let max_voltage:f64 = max_voltage_micro as f64 / 10000000 as f64;
    return max_voltage;
}

pub fn min_voltage_battery() -> f64{
    let min_voltage_micro: i64 = files::read_int("/sys/class/power_supply/lego-ev3-battery/voltage_min_design");
    let min_voltage:f64 = min_voltage_micro as f64 / 10000000 as f64;
    return min_voltage;
}

pub fn voltage_battery() -> f64 {
    let voltage_now_micro: i64 = files::read_int("/sys/class/power_supply/lego-ev3-battery/voltage_now");
    let voltage_now:f64 = voltage_now_micro as f64 / 1000000 as f64;
    return voltage_now;
}
