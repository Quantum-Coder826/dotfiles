mod robot;
use robot::brick::brick;
use robot::motor::Motor;
use robot::sensor::{Sensor, SensorReturn};

fn main() {
    brick::init();

    let mut speed_sp: f32 = 0.25;

    let mut left_motor: Motor = Motor::attatch("ev3-ports:outA");
    let mut right_motor: Motor = Motor::attatch("ev3-ports:outD");
    left_motor.set_pol_normal();
    right_motor.set_pol_normal();
    
    let mut ir: Sensor = Sensor::attatch("ev3-ports:in4");
    ir.set_mode("IR-REMOTE");

    loop {
        let key: usize = match ir.get_value(0) {
            SensorReturn::Int(key) => key as usize,
            SensorReturn::Float(_) => 0// eg do nothig
        };
        

        left_motor.run_duty((100.0 * speed) as i8);
        right_motor.run_duty((-100.0 * speed) as i8);
        
    }
}