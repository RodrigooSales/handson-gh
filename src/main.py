def slugufy(title):
    title = title.strip()
    title = title.replace(' ', '-')
    title = title.lower()
    
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '~', '`']
    
    for special_character in special_characters:
        title = title.replace(special_character, '')
    
    while '--' in title:
        title = title.replace('--', '-')
    return title

title = '   This Is        My Title!  '
print(slugufy(title))