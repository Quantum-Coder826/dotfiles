mod robot;
use robot::brick::brick;
use robot::motor::Motor;
use robot::sensor::{Sensor, SensorReturn};

fn main() {
    brick::init();

    let mut ramp_value: f32 = 0.25;

    let keys_remote: [[i8; 2]; 12] = [[0,0],[75,0],[-75,0],[0,75],[0,-75],[75,75],[75,-75],[-75,75],[-75,-75],[0,0],[0,0],[0,0]];

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
        if !key == 0 || key >= 9 {
            ramp_value = 0.0;
        } else {
            ramp_value = ramp_value + 0.10;
        }

        if ramp_value >= 1.0 {
            ramp_value = 1.0
        }
        println!("{}", ramp_value);

        left_motor.run_duty((keys_remote[key][1] as f32 * ramp_value) as i8);
        right_motor.run_duty((keys_remote[key][0] as f32 * ramp_value) as i8);
        
    }
}