; Lab 5 (Problem 3) - 5(c)

.386
.model flat, stdcall
.stack 4096

ExitProcess PROTO, dwExitCode:DWORD

.data

myWord word 4 dup(1,2,3,4,5)

.code
main PROC
	mov eax, 0			; zeoring eax
	mov ax, myWord+0	; sum up the list values
	add ax, myWord+2
	add ax, myWord+4
	add ax, myWord+6
	add ax, myWord+8
	
	INVOKE ExitProcess, 0
main ENDP
END main
