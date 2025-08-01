from datetime import datetime
import os

# GET TITLE, CATEGORY, DATETIME
now = datetime.now()
category = "The Making of this Blog"
now_date = now.strftime("%Y-%m-%d")
now_datetime = now.strftime("%Y-%m-%d %H:%M%S")

title = "Something on Prayer"
post_path = os.path.join(f"./{category}/_posts/{now_date}-{title}.md")

# WRITE THE FILE
with open(post_path, 'w') as file:
    file.write("This is some content for the new file.")

# REPORT SUCCESS
print(f"File '{post_path}' created (or overwritten) successfully.")
print("HEY! NEXT TIME YOU CODE, MAKE THIS THING MAKE THE CATEGORY TOO! WHAT SHOULD THE TOOL BE CALLED?? DBT?")