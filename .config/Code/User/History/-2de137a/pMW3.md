# motor.rs
All methods in the motor.rs file are used to contorl the following motors:
- LEGO White Mindstorms EV3 Large Motor (95658)
- LEGO Medium Stone Gray Mindstorms EV3 Medium Motor (99455)

More information can be foun ton the ev3dev [site](https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/motors.html#tacho-motor-subsystem) that gives more context about everything that is happening in the backgound.

## the methods
### ```attatch(port: &str) -> Motor```
This method is required to interact wich a motor, it retuns the struct Motor what will contain all the information all other metods need to work. The port variable sould look someting like `ev3-ports:out<X>`
Where X is the letter the phisical device is connecte to.

### ```run_forever(&self, speed_sp: i16)```
This command will command the motor to run continuously at the given `speed_sp` until another command is issued.

### ```run_abs_pos(&self, angle_sp: i16, speed_sp: i16)```
The motor will run to the specifided angel with the specified speed and stop using the stop action that is set.

### ```run_rel_pos(&self, angle_sp: i16, speed_sp: i16)```
Same as `run_abs_pos` but the new postion will be the current position + `angel_sp`.

### ```run_rot_count(&self, count: u8, speed_sp: i16)```
Make the motor turn for a specified amount of full rotations and stops the motor using the specified stop action.

### ```run_timed(&self, time_sp: u64, speed_sp: i16)```
Runs the motor for a amount of seconds specified in `time_sp`.

### ```run_duty(&self, duty_sp: i8)```
Run the motor on a set duty cycle, the value in `duty_sp` ranges form -100 to 100.

### ```stop(&self)```
stops the motor using the set stop action.

### ```