; Lab 4 (problem 1)

.386
.model flat,stdcall
.stack 4096

ExitProcess proto,dwExitCode:dword

.code
main proc
  ; Write and run a program to evaluate the following expression:
  ; AL = (AL – DL) + CL - BL
 	mov	AL, 245			
	mov	BL, 41
  mov CL, 11
  mov DL, 215
  sub Al, DL
  add AL, CL
  sub Al, BL

	invoke ExitProcess,0
main endp
end main
