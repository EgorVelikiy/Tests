from data import mentors


def unique_names(data):
    all_names_list = []
    for menor_list in data:
        for mentor in menor_list:
            name = mentor.split()
            all_names_list.append(name[0])

    unique_names = list(set(all_names_list))
    return len(unique_names)


def max_course_durations(courses, mentors, durations):
    courses_list = []
    for courses, mentor, dur in zip(courses, mentors, durations):
        course_dict = {"title": courses, "mentors": mentor, "duration": dur}
        courses_list.append(course_dict)
    maxi = max(durations)
    maxes = []
    for index, values in enumerate(durations):
        if values >= maxi:
            maxes.append(index)
    courses_max = []
    for id in maxes:
        courses_max.append(courses_list[id]["title"])
    result = f'Самый длинный курс(ы): {", ".join(courses_max)} - {maxi} месяца(ев)'
    return result


def popular_name(data):
    all_names_list = []
    for menor_list in data:
        for mentor in menor_list:
            name = mentor.split()
            all_names_list.append(name[0])

    unique_names = list(set(all_names_list))
    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])

    popular.sort(key=lambda x: x[1], reverse=True)

    return popular[0][1]

print(popular_name(mentors))