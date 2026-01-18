; Lab 8 (Problem 1) - 8(a)
; Summing an Array (SumArray.asm)

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

.data
	intarray DWORD 10000h, 20000h, 30000h, 40000h

.code
main proc
	mov edi, OFFSET intarray			  ; 1: EDI = address of intarray
	mov ecx, LENGTHOF intarray			; 2: initialize loop counter
	mov eax, 0							        ; 3: sum = 0
	L1:									            ; 4: mark beginning of loop
	add eax, [edi]					  	    ; 5: add an integer
	add edi, TYPE intarray				  ; 6: point to next element
	loop L1								          ; 7: repeat until EXC = 0
	invoke ExitProcess, 0

main endp
end main
