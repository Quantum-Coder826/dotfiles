use std::env;
use std::fs::File;
use std::io::{BufReader, BufRead};

fn main() {

    // get the rom
    let args: Vec<String> = env::args().collect();
    let path_to_rom: String = args[1].clone();

    let file: File = match File::open(path_to_rom) {
         Err(err) => panic!("couldn't open: {}", err),
         Ok(file) => file,
    };
    let reader: BufReader<File> = BufReader::new(file);
    let lines: Vec<_> = reader.lines().collect();


    // iterate trough each line of the rom to populate memory
    let mut memory: Vec<String> = Vec::new();
    memory.resize(99, "000".to_string());

    let mut index: usize = 0;
    for l in lines {
        memory[index] = l.unwrap();
        index += 1;
    }

    // create all registers and flags
    let mut accumulator: i16 = 000;
    let mut program_counter: usize = 000;
    
    let mut overflow: bool = false;
    let mut underflow: bool = false;

    let mut instruction_register: String = String::new();
    let mut address_register: String = String::new();

    // enter the main loop
    loop {
        // fetch the instruction and opcode
        let fetch_data: String = memory[program_counter].clone();
        instruction_register = fetch_data[..1].to_owned(); // first digit is instruction
        address_register = fetch_data[1..3].to_owned(); // last two digits are address

        // increment program counter
        program_counter += 1;

        // decode the instruction
        match instruction_register.parse::<u8>().unwrap() {
            1 => {
                // ADD
                let number = (memory[address_register.parse::<usize>().unwrap()]) as u16;
            }
            _ => {panic!("failed to decode instruction: {} at PC: {}", fetch_data, program_counter);}
        }

    }
}
