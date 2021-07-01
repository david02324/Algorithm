def parse_time(time_str):
    time_li = time_str.split(':')
    h = int(time_li[0])
    m = int(time_li[1])
    
    return (h - 9) * 60 + m

def rev_parse_time(minute):
    h = 9 + minute // 60
    m = minute % 60
    
    if m < 0:
        h -= 1
        m += 60
        
    h = str(h)
    m = str(m)
    
    if len(h) < 2:
        h = '0'+h
    if len(m) < 2:
        m = '0'+m
        
    return h+':'+m

def solution(n, t, m, timetable):
    timetable = sorted(list(map(parse_time,timetable)),reverse=True)

    for shuttle_time in range(0,n*t,t):
        passengers_time = []
        while len(passengers_time) < m and timetable and timetable[-1] <= shuttle_time:
            passengers_time.append(timetable.pop())
        if len(passengers_time) < m:
            latest = shuttle_time
        else:
            latest = max(passengers_time) - 1

    return rev_parse_time(latest)