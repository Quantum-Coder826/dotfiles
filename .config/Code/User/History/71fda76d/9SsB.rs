mod robot;
use robot::brick::Brick;
use robot::motor::Motor;
use robot::sensor::{Sensor, SensorReturn};

fn main() {
    Brick::init();

    for i in 1..16 {
        print!("form main {}", i);
    }

    Brick::exit();
}