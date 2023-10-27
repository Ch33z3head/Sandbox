Call func
.string "Hello World\n"

func:
 
 ; Open/Create file
mov eax, 5                      ; SYS_OPEN
mov ebx,"hello.txt",0
mov ecx, 65                     ; O_WRONLY|O_CREAT
mov edx, 0644o                  ; mode
int 0x80                        ; system call interrupt

; Write to the file
push eax
mov ecx, eax
mov eax, 4                      ; SYS_WRITE 
mov ecx, 1                      ; address of the string we want to print
mov edx,13                      ; number of characters to write
int 0x80                        ; system call interrupt

; Close 
mov eax, 6                      ; SYS_COSE
pop ebx
int 0x80                        ; system call interrupt

; Exit
mov eax, 1                      ; Exit
mov ebx, 0                      ; error code
int 0x80                        ; system call interrupt
