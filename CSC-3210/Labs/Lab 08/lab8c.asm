; Lab 8 (Problem 3) - 8(c)

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

.code
main proc
	mov al, 01101111b
	and al, 00101101b		; a. AL = 2Dh
	mov al, 6Dh
	and al, 4Ah				  ; b. AL = 48h
	mov al, 00001111b
	or al, 61h				  ; c. AL = 6Fh
	mov al, 94h
	xor al, 37h				  ; d. AL = A3h
	invoke ExitProcess, 0

main endp
end main
