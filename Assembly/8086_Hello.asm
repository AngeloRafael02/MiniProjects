                                 
; The easiest way to print out "Hello, World!"
name "8086_Hello" ;filename

org 100h

jmp start       ; jump over data declaration

message:    db      "Hello, World!", 0Dh,0Ah, 24h ; 0dh = carraige return | 0ah = line feed | 24h = end of string
message2: db    "Hello Again!", 0Dh,0Ah, 24h

start:  
mov     dx, message  ; load offset of message into dx.
mov     ah, 09h      ; print function is 9. often comboed with "int 21h" to execute 
int     21h          ; do it!   
mov     dx, message2
mov     ah, 09h
int     21h
        
mov     ah, 0 
int     16h      ; wait for any key....
        
ret ; return to operating system.