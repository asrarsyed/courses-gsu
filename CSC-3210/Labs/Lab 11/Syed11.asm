; Lab 11 (Problem 1) - 11(a)

.386 
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

; var4 = (var1 * var2) / (var3 * 5)

.data
	var1 DWORD 100
  var2 DWORD 200
  var3 DWORD 50
  var4 DWORD ?

.code
main proc
    mov eax, var1          ; eax = var1
    imul eax, var2         ; eax = var1 * var2 (signed multiplication)
    mov ecx, var3          ; ecx = var3
    mov ebx, 5             ; ebx = 5
    imul ecx, ebx          ; ecx = var3 * 5 (signed multiplication)
    cdq                    ; Sign extend eax into edx:eax
    idiv ecx               ; Perform (var1 * var2) / (var3 * 5) and store the result in eax
    mov var4, eax          ; Store the result in var4

    invoke ExitProcess, 0 ; Exit

main endp
end main
