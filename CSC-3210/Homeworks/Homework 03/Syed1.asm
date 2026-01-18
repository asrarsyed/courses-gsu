; Class: CSC 3210
; Assignment #3 (Question 1)
; This program will find the sum of the words in the data segment

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword


.data
	; creating given value as DWORD (32-bit integer)
  dVal DWORD 04080102h

.code
main proc
	mov eax, 0								        ; putting zeros in the register values
	mov ebx, 0
	mov ecx, 0
	mov edx, 0

	mov al, BYTE PTR [dVal + 3]				; loading 04h in al
	mov bl, BYTE PTR [dVal + 2]				; loading 08h in bl
	mov cl, BYTE PTR [dVal + 1]				; loading 01h in cl
	mov dl, BYTE PTR [dVal]				  	; loading 02h in dl

	add al, bl								        ; adding up the values of each register into al
	add al, cl
	add al, dl                        ; EAX = 0Fh

	invoke ExitProcess, 0
main endp
end main
