; Lab 6 (Problem 2) - 6(b)

.386
.model flat, stdcall
.stack 4096
ExitProcess proto dwExitCode:dword

.data

arrayD DWORD 10000h, 20000h, 30000h

.code
main proc

; Direct-Offset Addressing (doubleword array):
	mov eax, arrayD				  ; EAX = 00010000
	mov ebx, [arrayD + 4]		; EBX = 00020000
	mov edx, [arrayD + 8]		; EDX = 00030000
	
	invoke ExitProcess, 0
main endp
end main
