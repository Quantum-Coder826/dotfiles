
# architecture
## registers
- accumulator: can preform math is 3 digits wide
- INBOX: used for input is 3 digits wide.
- OUTBOX: used for output is 3 digits wide.
- program counter: points to the address off we are currently executing from is 2 digits wide.

## Memory
Thier are 

## instructions
|Hex|Mnemonic code|Instruction|Description|
|---|---|---|---|
0xx|ADD|ADD|Add the value currently stored in address xx to the accumulator.
1xx|SUB|SUBTRACT|Subtract the value currently stored in address xx to the accumulator.
2xx|STA|STORE|Store the contents of the accumulator in address xx.
3xx|LDA|LOAD|Load the value from address ii into the accumulator.
4xx|BRA|BRANCH (unconditional)|Set the programcounter to the given address.
5xx|BRZ|BRANCH IF ZERO (conditional)|If the accumulator is 000 then set the program counter to the given address. Otherwise, do nothing.
6xx|BRP|BRANCH IF POSITIVE (conditional)|If the accumulator is not 000 then set the program counter to the given address. Otherwise, do nothing.
700|INP|INPUT|Store the value in the **inbox** into the accumulator.
800|OUT|OUTPUT|Store the value in the accumulator into the **outbox**.
900|HLT|HALT|End the program.
 \- |DAT|DATA|This is an assembler instruction which simply loads the value into the next available mailbox. DAT can also be used in conjunction with labels to declare variables.



