; Lab 12 (Problem 1) - 12(a)

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

.data
  array DWORD 10h, 20h, 30h, 40h, 50h
  sample DWORD 50h

.code
main proc
  mov ebx, sample          ; Load the item we want to search for into EBX
  lea esi, [array]         ; Load the address of the first item in the array into ESI
  mov ecx, LENGTHOF array  ; Load the number of items in the array into ECX
  mov edx, 4               ; Load the size of each item in the array into EDX
  
  call search              ; Search Procedure
  nop

  invoke ExitProcess, 0
main endp

; Search Function
search PROC

  ; Initialize counter and result
  xor eax, eax            ; Clear EAX (result) to 0
  mov edi, ebx            ; Move the item we are searching for into EDI

search_loop:
  cmp ecx, 0              ; Check if ECX (counter) has reached 0
  je search_done          ; If ECX is 0, we have searched the entire array
  
  ; Compare the current item with the item we are searching for
  mov eax, [esi]          ; Load the current item into EAX
  cmp eax, edi            ; Compare with the item we are searching for
  je item_found           ; If equal, jump to item_found
  
  ; Move to the next item in the array
  add esi, edx            ; Move to the next DWORD in the array
  dec ecx                 ; Decrement the counter
  jmp search_loop         ; Repeat the loop
  
item_found:
  mov eax, edi            ; If the item is found, return it in EAX
  jmp search_end

search_done:
  mov eax, -1             ; If the item is not found, return -1 in EAX

search_end:
  ret

search ENDP
END main
