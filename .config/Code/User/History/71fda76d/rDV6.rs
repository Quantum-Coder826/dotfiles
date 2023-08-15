mod robot;
use robot::brick::brick;
use robot::motor::Motor;
use robot::sensor::{Sensor, SensorReturn};

fn main() {
    brick::init();

    for i in 1..16 {
        print!("form main {}", i);
    }

    brick::exit();
}