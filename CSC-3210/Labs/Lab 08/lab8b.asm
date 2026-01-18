; Lab 8 (Problem 2) - 8(b)

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

.data
	temp DWORD ?

.code
main proc
	mov eax, 0
	mov ecx, 10				; outer loop counter
	L1:
		mov eax, 3
		mov temp, ecx
		mov ecx, 5			; inner loop counter
	L2: 
		add eax, 5
		loop L2				  ; repeat inner loop
		mov ecx, temp
	loop L1					  ; repeat outer loop
	invoke ExitProcess, 0

main endp
end main
