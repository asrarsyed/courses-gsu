; Lab 6 (Problem 1) - 6(a)

.386
.model flat, stdcall
.stack 4096
ExitProcess proto dwExitCode:dword

.data
myByte1 BYTE 9Bh 
.code

main proc
	mov bx, 0A69Bh
	movzx eax, bx		; EAX = 0000A69B

	movzx eax, myByte1	; EAX = 0000009B

	mov bx, 0A69Bh
	movsx eax, bx		; EAX = FFFFA69B

	invoke ExitProcess, 0
main endp
end main
