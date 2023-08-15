# My lmc microprocessor (still need to name it)

## Overview
My spin on the little man computer will not be fateful to the original design, but more like a extension.
I will use a mix of the base instruction set with a stack added and inspiration from how RISC-V formats instructions on 16-bit boundary's.

## Features
- 8-bit data bus
- 8-bit address bus
- 4-bit instruction size
- 8-bit general-purpose registers
- 4 general-purpose registers


## Hardware
|Item|Description|Size|
|---|---|---|
|`IP`|Instruction Pointer|8-bit|
|`SP`|Stack Pointer|8-bit|
|`CF`|Carry Flag|1-bit|

## Instruction format
The cpu will always read 2 bytes into the decode register. The data in the registers can be interpreted in the following formats.

### formats
- R-type: Register type supports 1 destination register and 2 source registers
- I-type: Immediate-Write type supports 1 destination register and a 8-bit immediate value.
- J-type: Jump type supports 1 source register and a 8-bit value (to jump to).

### The formatting table
<table>
<tbody style="text-align: center;">
    <tr>
        <th rowspan="2">Format</th>
        <th colspan="4">Bit</th>
    </tr>
    <tr>
        <th>15&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12</th>
        <th>11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8</th>
        <th>7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4</th>
        <th>3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0</th>
    </tr>
    <tr>
        <th>R-type</th>
        <th><em>opcode</em></th>
        <th>Rd</th>
        <th>Rs1</th>
        <th>Rs2</th>
    </tr>
    <tr>
        <th>I-type</th>
        <th><em>opcode</em></th>
        <th>Rd</th>
        <th colspan="2"><em>immediate</em></th>
    </tr>
    <tr>
        <th>J-type</th>
        <th><em>opcode</em></th>
        <th>Rs1</th>
        <th colspan="2"><em>address</em></th>
    </tr>
</tbody>
</table>

## instructions
|Instr|Description|Format|Opcode|Operation (pseudo-code)|
|---|---|---|---|---|
|ADD|add|R|0x0|Rd = Rs1 + Rs2|
|SUB|subtract|R|0x1|Rd = Rs1 - Rs2|
|ADDI|add immediate|I|0x2|Rd = Rs1 + immediate|
|SUBI|subtract immediate|I|0x3|Rd = Rs1 - immediate|
|PUT|push|R|0x4|push_stack(Rs1)|
|POP|pop|R|0x5|Rd = pop_stack()|
|LW|Load word|I|0x6|Rd = MEM[immediate]|
|SW|Store word|J|0x7|MEM[address] = Rs1|
|SWR|Store word register|R|0x8|MEM[Rs2] = Rs1|
|JMP|Jump|J|0x9|PC = address|
|BEZ|Branch if equal to zero|J|0xA|PC = (Rs1 == 0 ? extend(address))|
|BNZ|Branch if not equal to zero|J|0xB|PC = (Rs1 != 0 ? extend(address))|
|JR|Jump Register|R|0xC|PC = Rs1|
