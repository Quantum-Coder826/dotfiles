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
Same as `urn