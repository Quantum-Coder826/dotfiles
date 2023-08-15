use std::env::args;
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufReader, BufRead};

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
    let mut asm_list: Vec<u16> = vec![0; 99]; // will contain the rom each address on one line
    let mut lable_list: HashMap<String, usize> = HashMap::new(); // The key is a label name and the value is the address it resides

    let mut source_address: usize = 0; // address off the line we are assembling

    for line in source_list {
        if line[0..1] == ":".to_string() { 
            // line starts with label
            let label_name = line.split(" ");
        }
    }
}
