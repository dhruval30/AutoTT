import re

with open('final_folder/timetable.txt', 'r') as file:
    text = file.read()


pattern = re.compile(
    r'^Unknown Class \d+:.*\n?|^\s*\d{1,2}:\d{2} to \d{1,2}:\d{2}: (-x-|---).*\n?',
    re.MULTILINE
)

# Remove matching lines
cleaned_text = re.sub(pattern, '', text)


with open('final_folder/without_free_periods.txt', 'w') as file:
    file.write(cleaned_text)
