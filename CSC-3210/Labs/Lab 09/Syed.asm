; Lab 9 (Problem 1) - 9(a)

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

.data
	Array WORD 10, 2, 23, 45, 21, 11		; given values
	MAXIMUM WORD ?

.code
main proc
	mov eax, 0								; putting zeros in register values
	mov ebx, 0

	mov ax, Array							; moving values into register
	mov MAXIMUM, ax	
	mov ecx, LENGTHOF Array

	L1:										    ; loop
		mov ax, [Array + bx]
		add ebx, TYPE Array

		cmp MAXIMUM, ax					; comparing elements in ax
		jle IF_BLOCK						; jumping if max < ax value
		jmp next

		IF_BLOCK:							  ; if statement
			mov MAXIMUM, ax
		next:
		loop L1
	invoke ExitProcess, 0

main endp
end main
