; Lab 10 (Problem 1) - 10(a)


.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

.data
	array_list DWORD 10, 11, 13, 18, 21, 23, 24, 17, 45			; int array_list[] = {10, 11, 13, 18, 21, 23, 24, 17, 45};
	array_size = LENGTHOF array_list                        ; int array_size = sizeof array_list / sizeof sample;
	index DWORD 0													                  ; int index = 0;
	sum DWORD ?													                    ; int sum = 0;

.code
main proc
	mov ecx, array_size											                ; setting loop counter
	mov esi, index												                  ; putting index in esi

	L1:                                                     ; (for loop) for (current_size = array_size; current_size > 0; current_size--) {
		cmp esi, array_size
		jnle endWhile
		jmp whileLoop

	whileLoop:													                    ; while (index < current_size) {
		test array_list[esi * (TYPE array_list)], 1
		jz ifBlock
		jmp next

	ifBlock:													                      ; if (array_list[index] is even) {
		add eax, array_list[esi * (TYPE array_list)]			    ; sum += array_list[index]; }

	next:		
	endWhile:													                      ; index += 1; } }
		inc esi
		loop L1

	mov sum, eax											                    	; sum = 52 (34h)

	invoke ExitProcess, 0

main endp
end main
