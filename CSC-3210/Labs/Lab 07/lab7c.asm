; Lab 7 (Problem 3) - 7(c)

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

.data
  varB BYTE  65h,31h,02h,05h
  varW WORD  6543h,1202h
  varD DWORD 12345678h

.code
main proc

  mov ax, WORD PTR [varB+2] ; a.
  mov bl, BYTE PTR  varD ; b.
  mov bl, BYTE PTR [varW+2] ; c.
  mov ax, WORD PTR [varD+2] ; d.
  mov eax, DWORD PTR varW ; e.

	invoke ExitProcess, 0

main endp
end main
