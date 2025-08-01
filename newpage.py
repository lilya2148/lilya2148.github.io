from datetime import datetime
import os
import argparse

parser = argparse.ArgumentParser(description="Make a new post (if it has spaces, make sure to use double quotes!!)")
parser.add_argument('--cat', type=str, help="What're you writing about?")
parser.add_argument('--title', type=str, help="What's the name of the thing you are writing?")
args = parser.parse_args()

# GET TITLE, CATEGORY, DATETIME
now = datetime.now()
now_date = now.strftime("%Y-%m-%d")
now_datetime = now.strftime("%Y-%m-%d %H:%M%:%S")

page_contents = f"""---
layout: page
title: {args.title}
date: {now_datetime}
category: [{args.cat}]
---
Yes, and at last, we begin to write something pretty sweet. As we always do. By reciting: Oh the wonders of the great earth..."
"""

# WRITE THE FILE
post_path = os.path.join(f"./{args.cat}/_posts/{now_date}-{args.title}.md")
print(f"Creating (or overwriting in 5..4..)'{post_path}'")
with open(post_path, 'w') as file:
    file.write(page_contents)

# REPORT SUCCESS
print(f"File '{post_path}' created (or overwritten) successfully.")
print("""
      HEY! NEXT TIME YOU CODE, 
      MAKE THIS THING MAKE THE CATEGORY TOO! 
      WHAT SHOULD THE TOOL BE CALLED?? 
      DBT? NO BUT IT SHOULD BE 3 LETTERS!
      """
)