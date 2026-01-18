; Class: CSC 3210
; Assignment #2 (Question 1)
; This program will compute (val3 + val4) - (val1 - val2) - ((30 * 4) / 8) for the EDX register.

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

.data
	val1 SWORD 134h				; Initializing variables as signed 16-bit integers
	val2 SWORD 139h
	val3 SWORD 67h
	val4 SWORD 47h

.code
main proc
	mov eax, 0h						; Putting zeros in the register values
	mov ebx, 0h
	mov ecx, 0h
	mov edx, 0h

	mov dx, val3					; Computing (val3 + val4) in DX register
	add dx, val4          ; DX = (val3 + val4)

	mov cx, val1					; Computing (val1 - val2) in CX register and then subtracting it to DX register
	sub cx, val2          ; CX = (val1 - val2)
	
	neg cx							  ; Since minus w/ minus happens it turns into a positive
	add dx, cx						; The operation changes because of the last line - computing (total of val3 and val4) + (total of val1 and val2)

	sub edx, ((30d * 4d) / 8d)		; Computing ((30 * 4) / 8) and then subtracting it to EDX register

	invoke ExitProcess, 0
main endp
end main
