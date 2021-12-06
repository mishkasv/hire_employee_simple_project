import datetime


def count_total_experience(workexperiences):
    t_experience = {'month': 0, 'year': 0}
    start = datetime.datetime.strptime(workexperiences[0]['start'], '%b %Y')
    end = datetime.datetime.strptime(workexperiences[0]['end'], '%b %Y')
    for i in range(1, len(workexperiences[1:]) + 1):
        if datetime.datetime.strptime(workexperiences[i]['start'], '%b %Y') > end:
            t_experience['year'] += end.year - start.year
            t_experience['month'] += end.month - start.month
            start = datetime.datetime.strptime(workexperiences[i]['start'], '%b %Y')
        if end <= datetime.datetime.strptime(workexperiences[i]['end'], '%b %Y'):
            end = datetime.datetime.strptime(workexperiences[i]['end'], '%b %Y')
        if i == len(workexperiences[1:]) and datetime.datetime.strptime(workexperiences[i]['start'], '%b %Y') < end:
            t_experience['year'] += end.year - start.year
            t_experience['month'] += end.month - start.month
    year = t_experience['year'] + t_experience['month'] // 12
    if t_experience['month'] >= 0:
        month_year = t_experience['month'] // 12
        month = t_experience['month'] % 12
    else:
        month_year = -(abs(t_experience['month']) // 12)
        correct = 0 if abs(t_experience['month']) // 12 == 0 else -1
        month_year += correct
        month = 12 - abs(t_experience['month']) % 12
    return year + month_year, month
