import re

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
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


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