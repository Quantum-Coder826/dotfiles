mod robot;
use robot::brick::Brick;
use robot::motor::Motor;
use robot::sensor::{Sensor, SensorReturn};

fn main() {
    let brick: Brick = Brick::init();

    for i in 1..16 {
        println!("form main {}", i);
    }

    brick.exit();
    B
}