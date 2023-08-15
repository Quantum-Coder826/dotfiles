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
|`SP`|Stack Pointer|4-bit|
|`CF`|Carry Flag|1-bit|
|`HLT`|Halt bit|1-bit|

The register will map to the bytes in this way. `0x4` to `0xC` are unused. 
The one bit registers will be read like `0b0000000x` where x is the 1-bit value contained in the register. 
|value|register|
|---|---|
|0x0|general-purpose 0|
|0x1|general-purpose 1|
|0x2|general-purpose 2|
|0x3|general-purpose 3|
|0xD|SP|
|0xE|CF|
|0xF|HLT|




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
        <th colspan="16">Bit</th>
    </tr>
    <tr>
        <th>15</th>
        <th>14</th>        
        <th>13</th>
        <th>12</th>
        <th>11</th>
        <th>10</th>
        <th>9</th>
        <th>8</th>
        <th>7</th>
        <th>6</th>
        <th>5</th>
        <th>4</th>
        <th>3</th>
        <th>2</th>
        <th>1</th>
        <th>0</th>        
    </tr>
    <tr>
        <th>R-type</th>
        <th colspan="4"><em>opcode</em></th>
        <th colspan="4">Rd</th>
        <th colspan="4">Rs1</th>
        <th colspan="4">Rs2</th>
    </tr>
    <tr>
        <th>I-type</th>
        <th colspan="4"><em>opcode</em></th>
        <th colspan="4">Rd</th>
        <th colspan="8"><em>immediate</em></th>
    </tr>
    <tr>
        <th>J-type</th>
        <th colspan="4"><em>opcode</em></th>
        <th colspan="4">Rs1</th>
        <th colspan="8"><em>address</em></th>
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
|AND|bitwise and|R|0xD|Rd = Rs1 & Rs2|
|OR|bitwise or|R|0xE|Rd = Rs1 \| Rs2|
|NOT|bitwise not|R|0xF|Rd = Rs1 ! Rs2|