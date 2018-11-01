from termcolor import colored
import datetime

actual_day = datetime.date.today()
weekday = datetime.date.weekday(actual_day)
polish_weekdays = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
text_day = f'Dzisiaj jest {polish_weekdays[weekday]}, {actual_day}.'
print(colored(text_day, color='cyan'))
christmas_day = datetime.date(2018, 12, 25)
delta = christmas_day - actual_day
text = f'Zostało {delta.days} dni do Bożego Narodzenia.'

if delta.days == 1:
    text = f'Został {delta.days} dzień do Bożego Narodzenia.'
    print(colored(text, color='red'))
elif delta.days < 7:
    print(colored(text, color='red'))
else:
    print(colored(text, color='yellow'))
