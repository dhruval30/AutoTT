from bs4 import BeautifulSoup

def parse_timetable(html):
    soup = BeautifulSoup(html, 'lxml')
    timetable = {}
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    tables = soup.find_all('table')
    print(f"Found {len(tables)} tables.")

    for idx, table in enumerate(tables):
        class_name_tag = table.find('th', colspan='9')
        class_name = class_name_tag.get_text(strip=True) if class_name_tag else f'Unknown Class {idx + 1}'
        print(f"Class name: {class_name}")

        timetable[class_name] = {}

        headers = [header.get_text(strip=True) for header in table.find_all('th', class_='xAxis')]
        print(f"Headers: {headers}")

        tbody = table.find('tbody')
        if not tbody:
            print(f"No 'tbody' element found in table {idx + 1}")
            continue

        rows = tbody.find_all('tr')
        print(f"Found {len(rows)} rows in the table.")

        for row_idx, row in enumerate(rows):
            day_cell = row.find('th', class_='yAxis')
            if day_cell:
                day = day_cell.get_text(strip=True)
                if day in days:
                    timetable[class_name].setdefault(day, {})

                    periods = row.find_all('td')
                    period_index = 0

                    for period in periods:
                        colspan = int(period.get('colspan', 1))
                        period_time = headers[period_index] if period_index < len(headers) else f'Period {period_index+1}'
                        period_content = period.get_text(strip=True).replace('\n', ' ').replace('  ', ' ')

                        if colspan > 1:
                            for _ in range(colspan):
                                if period_index < len(headers):
                                    timetable[class_name][day][headers[period_index]] = period_content
                                    period_index += 1
                        else:
                            if period_index < len(headers):
                                timetable[class_name][day][period_time] = period_content
                                period_index += 1

                    for extra_period in range(period_index, len(headers)):
                        period_time = headers[extra_period]
                        timetable[class_name][day][period_time] = '---'
                        print(f"Parsed {day} {period_time}: ---")
            else:
                print(f"No 'th' element with class 'yAxis' found in row {row_idx + 1}")

    return timetable

def main():
    with open('final_folder/19thAug.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    timetable = parse_timetable(html_content)
    
    with open('final_folder/timetable.txt', 'w', encoding='utf-8') as file:
        for class_name, class_schedule in timetable.items():
            file.write(f"{class_name}:\n")
            for day, schedule in class_schedule.items():
                file.write(f"  {day}:\n")
                for time, subject in schedule.items():
                    file.write(f"    {time}: {subject}\n")
                file.write("\n")

if __name__ == "__main__":
    main()
