#![allow(non_snake_case)]
#![allow(non_camel_case_types)]
use std::env;
use std::fs::File;
use std::io::{Error, Read, BufReader};
use std::process::exit;

fn init_memory(path_to_rom: String) -> Vec<u8> {    
    // open the rom file
    let file_result: Result<File, Error> = File::open(&path_to_rom);
    let file:File = match  file_result {
        Ok(file) => file,
        Err(error) => panic!("Failed to read file: {:?}, Error: {:?}", &path_to_rom, error)
    };
    let mut reader: BufReader<File> = BufReader::new(file);
    // read the rom file into memory
    let mut buffer:Vec<u8> = Vec::new();
    reader.read_to_end(&mut buffer).unwrap();
    // create the address_space vector with a 2^16 elements all containing a zero
    let mut address_space: Vec<u8> = Vec::new();
    address_space.resize(0xFFFF, 0x00);
    
    // loop though the given rom and put all values in the the address space from 0x8000 and onwards.
    let mut index: usize = 0x8000;
    for byte in buffer {
        address_space[index] = byte;
        index += 0x0001;
    };

    // debug print the full address space
    //println!("The address space is: ");
    //println!("{:X?}", address_space);
    return address_space;
}

// helper functions
fn get_register(register_num: usize, memory: &Vec<u8>) -> u16 {
    let address: usize = match register_num {
        0x0 => 0x0000,
        0x1 => 0x0002,
        0x2 => 0x0004,
        0x3 => 0x0006,
        0x4 => 0x0008,
        0x5 => 0x000A,
        0x6 => 0x000C,
        0x7 => 0x000E,
        _=>panic!("Unknown register: {:02X?}", register_num),
    };
    let register_value: u16 = ((memory[address] as u16) << 8) | memory[address + 0x0001] as u16;
    return register_value;
}

fn set_register(register_num: usize, value:u16, memory: &mut Vec<u8>) {
    let address: usize = match register_num {
        0x0 => 0x0000,
        0x1 => 0x0002,
        0x2 => 0x0004,
        0x3 => 0x0006,
        0x4 => 0x0008,
        0x5 => 0x000A,
        0x6 => 0x000C,
        0x7 => 0x000E,
        _=>panic!("Unknown register: {:02X?}", value),
    };
    let word: [u8; 2] = value.to_be_bytes(); // split in high and low words
    memory[address] = word[0] as u8;
    memory[address + 0x0001] = word[1] as u8;
}


fn main() {
    // initialize emulated computer
    let args: Vec<String> = env::args().collect();
    let path_to_rom: String = args[1].clone();
    
    let mut memory: Vec<u8> = init_memory(path_to_rom);

    // innit important microprocessor related vars
    // special registers
    let mut PC: usize = 0x8000; // default to the reset vector
    let mut SP: usize = 0x0020; // default to first stack item
    let mut OF: bool = false;

    memory[0x0012] = 0x00; // set the upper byte of the flag table to zero
    memory[0x0013] = 0xFE; // set the lower byte of the flag table to the bit pattern 0b11111110

    memory[0x001E] = 0x00; // set the default stack pointer
    memory[0x001F] = 0x20;

    // enter run loop
    loop {
        // get the instruction and split the byte into its nibbles
        let instruction: u8 = memory[PC];
        let high_nibble: u8 = instruction & 0xF0;
        let low_nibble: u8 = instruction & 0x0F;

        // match on the high nibble to the instruction call the correct function and pass the low nibble 
        if high_nibble == 0x00 {
            exit(0);

        } else if high_nibble == 0x01 {// ADD Rx, Rx
            let first_register: usize = low_nibble as usize;

            // get second register
            PC += 0x0001;
            let high_word: u8 = memory[PC]; // contains second register
            let second_register: usize = high_word as usize;
            
            // get the values from the registers
            let first_value: u16 = get_register(first_register, &memory);
            let second_value: u16 = get_register(second_register, &memory);
            
            // add the values and send them to the appropriate register
            let added_values: u16 = first_value + second_value;
            set_register(first_register, added_values, &mut memory);
            
        } else if high_nibble == 0x02 {
            
        } else if high_nibble == 0x03 {
            
        } else if high_nibble == 0x04 {
            
        } else if high_nibble == 0x05 {
            
        } else if high_nibble == 0x06 {
            
        } else if high_nibble == 0x07 {
            
        } else if high_nibble == 0x08 {
            
        } else if high_nibble == 0x09 {
            
        } else if high_nibble == 0x0A {

        } else if high_nibble == 0x0B {
            
        } else if high_nibble == 0x0C {
            
        } else if high_nibble == 0x0D {
            
        } else if high_nibble == 0x0E {
            
        } else if high_nibble == 0x0F {
            
        };
        PC += 0x0001; // increment program counter for the next instruction.
    }

    // this block of functions is responsible for running the instructions
    fn instruction_HLT(low_nibble: u8, PC: usize) {
        println!("PC: {:02X?}: HLT, {:02X?}", PC, low_nibble);
        exit(0);
    }

    // ADD Rx, Rx
    //let first_register: usize = low_nibble as usize;
    //println!("reg1: {:02X?}", first_register);
    //// get second register
    //PC += 0x0001;
    //let high_word: u8 = memory.memory[PC]; // contains second register
    //let second_register: usize = high_word as usize;
    //
    //println!("reg2: {:02X?}", second_register);
    //// get the values from the registers
    //let first_value: u16 = get_register(first_register, memory.memory);
    //println!("val1: {:02X?}", first_value);
    //
    //let second_value: u16 = get_register(second_register, memory.memory);
    //println!("val2: {:02X?}", second_value);
    //let calculated_value: u16 = first_value + second_value;
    //println!("{:02X?}",calculated_value);
    //set_register(first_register, calculated_value, memory.memory);
}