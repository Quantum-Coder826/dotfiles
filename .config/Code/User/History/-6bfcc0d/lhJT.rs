use std::env::args;
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufReader, BufRead};
use std::str::{SplitWhitespace, Chars};


fn init_source_code_list() -> Vec<String>{
    let args: Vec<String> = args().collect();
    let file_name: String = args[1].clone();
    let file: File = File::open(file_name).unwrap();
    let buf: BufReader<File> = BufReader::new(file);
    
    let source: Vec<String> = buf.lines().map(|l: Result<String, std::io::Error>| l.expect("Failed to parse file")).collect();
    if source.len() > 99 {
        panic!("Source code exceeds memory limit, line count is: {} must be less than or equal to 99", source.len());
    } else {
        return source;
    }
}

fn main() {
    let mut source_list: Vec<String> = init_source_code_list().clone(); // contains the source code line by line
    let mut asm_list: Vec<String> = vec![String::new(); 99]; // will contain the rom each address on one line
    let mut label_list: HashMap<String, usize> = HashMap::new(); // The key is a label name and the value is the address it resides

    let mut source_address: usize = 0; // address off the line we are assembling

    for line in source_list {
        let mut iter_line: SplitWhitespace = line.split_whitespace(); // use a iterator to make it easy to find parts of the code

        // check for label
        let start_slice: String = iter_line.next().unwrap().to_string();
        if start_slice.contains(":")  {
            // it's a label create it
            let mut label_name: Chars<'_> = start_slice.chars();
            label_name.next();
            label_list.insert(label_name.as_str().to_string(), source_address);
        }

        // continue decoding instruction
        let operand: String  = match iter_line.next() {
            Some("ADD") => "0".to_string(),
            _ => panic!("Tried to decode unknown instruction '{}' at line: {}", iter_line.next_back().unwrap().to_string(), source_address + 1)
        };
        println!("instruct: {}", operand);
    }
}
