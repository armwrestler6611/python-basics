duration = int(input('Enter all the time in seconds:'))
year = duration // 31556926
months = duration // 2629743
weeks = duration // 86400 // 7
days = duration // 3600 // 24
hours = duration // 3600 - days * 24
minutes = duration // 60 % 60
seconds = duration % 60
print('year:', year, ',' 'months:', months, ',' 'weeks:', weeks, ',' 'days:', days, ',' 
      'hours:', hours, ',', 'minutes:', minutes, ',', 'seconds:', seconds, ',', sep='')
