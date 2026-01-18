; Lab 7 (Problem 2) - 7(b)

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

.data
  myBytes   BYTE 10h,20h,30h,40h
  myWords   WORD 8Ah,3Bh,72h,44h,66h
  myDoubles DWORD 1,2,3,4,5

.code
main proc

  mov esi, OFFSET myBytes
  mov ax, [esi] ; a. AX =
  mov eax, DWORD PTR myWords ; b. EAX =
  mov esi, OFFSET myWords
  mov ax, [esi+2] ; c. AX =
  mov ax, [esi+6] ; d. AX =
  mov ax, [esi-4] ; e. AX =

	invoke ExitProcess, 0

main endp
end main
