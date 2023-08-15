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
 - |DAT|DATA|A assembler instruction that will 
