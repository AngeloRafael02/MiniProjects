MOV [0000], 5789h   ; put first value in [0000]
MOV [0002], 1456h   ; put second value in [0002]
MOV [0004], 302Bh   ; put third value in [0004]

MOV BX, [0000]      ; first number to compare
MOV CX, [0002]      ; second number to compare
MOV DX, [0004]      ; third number to compare

MOV AX, BX          ; set first value first on AX
CMP CX, BX          ; compare second value with first value
JG set_largest      ; jump if second valueis greater
CMP DX, BX          ; compare third value with first value
JG set_largest      ; jump if third value is greater
jmp done

set_largest:
MOV AX, CX          ; set second value to AX
CMP DX, CX          ; compare third value with second value
JG set_largest2     ; jump if third value is greater
jmp done

set_largest2:
MOV AX, DX          ; set third value to AX

done: 
MOV [0040], AX      ; move largest value (whatever is in AX) to [0040]
HLT 
