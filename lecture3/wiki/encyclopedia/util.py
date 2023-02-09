import re
import markdown2
from django.shortcuts import render
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):

    title_lower = title.lower()
    title_capitalized = title.capitalize()
    title_upper = title.upper()
    
    filenames = [f"entries/{title_lower}.md", f"entries/{title_capitalized}.md", f"entries/{title_upper}.md"]
 
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    
    for filename in filenames:
        if default_storage.exists(filename):
            raise ValueError("The Entry Title Already exists!")
            #default_storage.delete(filename)
            break
    else:
        if title == title.lower():
            title = title.capitalize()
        elif title == title.upper():
            title = title.upper()
        else:
            title = title.capitalize()
            
        fileTitle = f'entries/{title}.md'
        content = f'# {title} \n\n {content}'
        default_storage.save(fileTitle, ContentFile(content.encode("utf-8")))


def get_entry(title):

    title_lower = title.lower()
    title_capitalized = title.capitalize()
    title_upper = title.upper()
    
    filenames = [f"entries/{title_lower}.md", f"entries/{title_capitalized}.md", f"entries/{title_upper}.md"]
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    for filename in filenames:
        try:
            f = default_storage.open(filename)
            return f.read().decode("utf-8")
        except FileNotFoundError:
            pass
    
    return None


def save_edit_entry(title, content):
    title_lower = title.lower()
    title_capitalized = title.capitalize()
    title_upper = title.upper()
    
    filenames = [f"entries/{title_lower}.md", f"entries/{title_capitalized}.md", f"entries/{title_upper}.md"]
    
    for filename in filenames:
        if default_storage.exists(filename):
            default_storage.delete(filename)
            break

    title = f'entries/{title}.md'
    edit_content = f'{content}'

    default_storage.save(title, ContentFile(markdown2.markdown(edit_content)))

def get_edit_entry(title):
    title_lower = title.lower()
    title_capitalized = title.capitalize()
    title_upper = title.upper()
    
    filenames = [f"entries/{title_lower}.md", f"entries/{title_capitalized}.md", f"entries/{title_upper}.md"]
    
    for filename in filenames:
        try:
            f = default_storage.open(filename)
            content = f.read().decode('utf-8')
            return content
        except FileNotFoundError:
            pass
    
    return None