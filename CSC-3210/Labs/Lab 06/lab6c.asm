; Lab 6 (Problem 3) - 6(c)

.386
.model flat, stdcall
.stack 4096

ExitProcess proto dwExitCode:dword

.data
	arrayB WORD 1,2,3,4
	; Change the array to 3,4,2,1

.code
main proc
	mov ax, arrayB 
	xchg ax, [arrayB + 6] ; 1,2,3,1 ax = 4
	xchg ax, [arrayB + 2] ; 1,4,3,1 ax = 2
	xchg ax, [arrayB + 4] ; 1,4,2,1 ax = 3
	mov arrayB, ax

	invoke ExitProcess, 0
main endp
end main

;[arrayB + 0]: Aims to access the 0th element (first element).
;[arrayB + 2]: Aims to access the 1st element (second element).
;[arrayB + 4]: Aims to access the 2nd element (third element).
;[arrayB + 6]: Aims to access the 3rd element (fourth element).
