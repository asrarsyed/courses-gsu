; Lab 7 (Problem 4) - 7(d)

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

.data
  dVal DWORD ?

.code
main proc

  mov dVal,12345678h
  mov ax,WORD PTR dVal+2
  add ax,3
  mov WORD PTR dVal,ax                   ; dVal=
  mov eax,dVal                           ; EAX=

	invoke ExitProcess, 0

main endp
end main
