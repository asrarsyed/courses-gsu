; Class: CSC 3210
; Assignment #3 (Question 2)
; This program is a translation of a if-else statement code to masm

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword


.data
	var1 DWORD 10
	var2 DWORD 11
	var3 DWORD 12

.code
main proc   
    mov eax, var1      ; Load variables into EAX/EBX/ECX
    mov ebx, var2
    mov ecx, var3

    cmp eax, ebx       ; Compare var1 and var2 (var1 > var2)
    ja L1

    cmp ebx, ecx       ; Compare var2 and var3 (var2 > var3)
    ja next

L1:
    add eax, ebx       ; var1 = var1 + var2
    add eax, ecx       ; var1 = var1 + var3
    inc ebx            ; var2++
    inc ecx            ; var3++
    jmp end_if_else    ; Jump to the end of the if-else block

next:
    dec eax            ; var1--
    dec ebx            ; var2--
    dec ecx            ; var3--

end_if_else:
    invoke ExitProcess, 0
main endp
end main
