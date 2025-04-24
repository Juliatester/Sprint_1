times = '1h 45m,360s,25m,30m,120s,2h'
cleaned_times = times.replace(' ', '')
time_values = cleaned_times.split(',')
total_minutes = 0

for time in time_values:
    if 'h' in time:
        total_minutes+=int(time.split('h')[0]) * 60
        time = time.split('h')[1]
    if 'm' in time:
        total_minutes+=int(time.split('m')[0])
        time = time.split('m')[1]
    if 's' in time:
        total_minutes+=int(time.split('s')[0])// 60

print(f'Общее количество минут: {total_minutes}')