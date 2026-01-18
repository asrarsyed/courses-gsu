; Class: CSC 3210
; Assignment #2 (Question 3)
; This program will create an uninitialized array of DWORD elements being updated with various values.

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

.data
	z DWORD 3 DUP (?)		; Creating given DWORD array
	x WORD 10				    ; Initializing x, y, and r with their given values as 16-bit integers
	y WORD 15
  r WORD 4

.code
main proc
	mov eax, 0				  ; Putting zeros in the register values
	mov ebx, 0
	mov ecx, 0
	mov edx, 0				

  ;GOAL; z_0 = x + y + r
	mov eax, x				  ; Load x into EAX
	add eax, y				  ; Add y to EAX
  add eax, r				  ; Add r to EAX
	mov z, eax				  ; Store whatever is in EAX to z_0


  ;GOAL; z_1 = z_0 + (y - r)
	mov ebx, y				  ; Load y into EBX
	sub ebx, r				  ; Sub y to EBX
	add ebx, eax				; Add EBX with z_0
	mov z + 4, ebx      ; Store whatever is in EBX to z_1

  ;GOAL; z_2 = z_0 + (z_1 + y)
	mov ecx, y				  ; Load y into ECX
	add ecx, ebx				; Add ECX with z_1
	add ecx, eax				; Add ECX with z_0
	mov z + 8, ecx			; Store whatever is in ECX to z_2

	invoke ExitProcess, 0
main endp
end main
