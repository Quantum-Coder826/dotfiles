# Assembler
The assembler will take a .txt file tach contains the instructions and assemble it into a rom file.

## language
The language must be written in this style:
```
:START INP
ADD :TWO
:TWO DAT 2
BRA START
# comment
```
labels are defined by adding

## rom
The rom will be stored as a .lmc file that contains a 100 lines representing the address space, all addresses must be filled so when your program is only needs 7 addressees the 93 remaining spaces will be filled with `000` numbers.

## assembly
Needed for assembly are 3 lists:
|name|desc|
|---|---|
|source-code|Each entry in the list contains the source code that will be assembled to the corresponding memory address|
|assembled-instructions|Basically the memory that the computer will contain to run the program|
|label-list|contains reference to the labels used in the source code and the address that label corresponds to|

This state diagram will contain the assembly process.
```mermaid
---
title: assembly state machine
---
stateDiagram-v2
    [*]-->init
    init-->read

    read-->assemble: No a label
    state assemble {
        [*]-->get_opcode
        get_opcode-->get_address
        get_address-->write_instruction
        write_instruction-->[*]
    }

    read-->create_label: Contains a label
    state create_label {
        [*]-->get_name
        get_name-->update_table
        update_table-->[*]
    }

    create_label-->assemble
    assemble-->next
    
    next-->read: The counter is <= 99
    next-->[*]: The counter is > 99

    init: Set the counter to line 0
    read: Get the line the counter is pointing at
    next: Increment the counter to the next line

```