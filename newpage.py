from datetime import datetime
import os
now = datetime.now()
# make a category one of these... 
title = "Something on Prayer"
# 2025-01-01 10:55:10 -0500
now_date = now.strftime("%Y-%m-%d")
now_datetime = now.strftime("%Y-%m-%d %H:%M%S")
file_name = f"{now_date}-{title}.md"
print('make this not something you have to run with python before it')

file_name = f"{now_date}.md"

with open(file_name, 'w') as file:
    file.write("This is some content for the new file.")
print(f"File '{file_name}' created (or overwritten) successfully.")