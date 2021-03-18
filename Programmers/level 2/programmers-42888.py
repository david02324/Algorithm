def solution(records):
    id_nickname = {}
    log = []
    
    for record in records:
        record = record.split()
        cmd = record[0]
        id = record[1]
        
        if cmd == 'Enter':
            nickname = record[2]
            id_nickname[id] = nickname
            log.append((id,1))
        elif cmd == 'Leave':
            log.append((id,-1))
        elif cmd == 'Change':
            nickname = record[2]
            id_nickname[id] = nickname
    
    for i in range(len(log)):
        id, io = log[i]
        log[i] = id_nickname[id] + '님이 '
        if io == 1:
            log[i] += '들어왔습니다.'
        else:
            log[i] += '나갔습니다.'
            
    return log