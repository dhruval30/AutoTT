# **HTML to Outlook Calendar**

Ever wanted to turn your HTML timetable into a cool Outlook calendar? No? Well, I did, and I am just weird like that. I get my uni schedules in `.html` formats, so I thought, let's scrape that bad boy and convert it into `.ics` files which can be seamlessly added to your Outlook calendar. Perfect for keeping you organized!

## **How It Works**

1. **Parsing HTML Timetable**  
   We utilize BeautifulSoup to scrape and parse HTML tables containing timetable data. This involves extracting class names, headers, and timetable entries, which are then structured into a dictionary format.

2. **Generating ICS Files**  
   Using the `ics` library, we create `.ics` files that can be imported into Outlook. Each event is detailed with summaries, start and end times, and locations, complete with timezone adjustments for accurate scheduling.

3. **Uploading to Outlook Calendar**  
   Well, I am yet to work on that. I promise I will do that when I get the time to.

**PS.** Please forgive me for the horrendous structuring; I am going through it. I will fix that also. I will also make a proper interface so that people can actually use it, one day.
