; Class: CSC 3210
; Assignment #2 (Question 2)
; This program will compute -(val3 - val1) + (-val4 + val2) + 3 for the ECX register.

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

.data
	val1 SWORD 12d		  ; initializing variable as signed 16-bit integer
	val2 SDWORD 9d			; initializing variable as signed 32-bit integer
	val3 SBYTE  2d			; initializing variable as signed 8-bit integer
	val4 SBYTE 20d			; initializing variable as signed 8-bit integer

.code
main proc
	mov eax, 0h					; Putting zeros in the register values
	mov ebx, 0h
	mov ecx, 0h
	mov edx, 0h

  movsx eax, val3     ; This moves the value of val3 into the EAX register, sign-extending it to a 32-bit value.
  movzs ebx, val1     ; This moves the value of val1 into the EBX register, sign-extending it to a 32-bit value.
  sub eax, ebx        ; Subtracts the value in EBX from the value in EAX.
  neg eax             ; Negate EAX

  mov ecx, eax        ; This moves the value in EAX to ECX.
  movsx eax, val4     ; This moves the value of val4 into the EAX register, sign-extending it to a 32-bit value.
  neg eax             ; Negate EAX
  add eax, val2       ; This adds the value of val2 to the value in EAX.

	add ecx, edx				; Computing (total of val3 and val1) + (total of val4 and val2)
	add ecx, 3d					; Adding 3 to ECX register

	invoke ExitProcess, 0
main endp
end main
