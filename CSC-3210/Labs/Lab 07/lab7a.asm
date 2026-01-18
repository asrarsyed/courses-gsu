; Lab 7 (Problem 1) - 7(a)

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

.data
	Val1 SWORD 23
	Val2 SWORD -35
	Val3 SDWORD 4

; calculating for EBX = (-Val3 - Val2) + (Val1 * 2)

.code
main proc

	mov ax, Val1	; 16-bit (SWORD)
	mov bx, Val2	; 16-bit (SWORD)
	mov ecx, Val3	; 32-bit (SDWORD)

	neg ecx			; Changing Val1 to a negative number because of the equation
	sub ecx, bx		; (-23 - (-35))

	add ax, Val1	; Since 23 * 2 = 26
	movsx eax, ax
	add eax, ecx
	mov ebx, eax	; Moving the final answer to the EBX register

	; EBX = 0000004D
	invoke ExitProcess, 0

main endp
end main
