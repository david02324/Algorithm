def solution(s):
    piece = 1
    min_len = len(s)
    
    while piece < len(s):
        l = piece
        count = 0
        zip_count = 1
        cur = s[:piece]
        ptr = piece
        while ptr + piece <= len(s):
            next = s[ptr:ptr+piece]
            if cur != next:
                cur = next
                if zip_count >= 2:
                    count += len(str(zip_count))
                    zip_count = 1
                l += piece
            else:
                zip_count += 1
            ptr += piece
        
        if zip_count >= 2:
            count += len(str(zip_count))
        l += count + len(s) - ptr
        
        min_len = min(min_len,l)
        piece += 1
        
    return min_len