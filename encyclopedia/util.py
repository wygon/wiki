import re, os, markdown
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(newTitle, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    newFilename = f"entries/{newTitle}.md"
    cleanedContent = "\n".join(
        line.rstrip() for line in content.splitlines() if line.strip() or (line == "" and not content.splitlines()[content.splitlines().index(line)+1].strip())
    )
    if default_storage.exists(newFilename):
        default_storage.delete(newFilename)
    default_storage.save(newFilename, ContentFile(cleanedContent))
    # default_storage.save(newFilename, ContentFile(content))

def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
def delete_entry(title):
     newFilename = f"entries/{title}.md"
     default_storage.delete(newFilename)
def markItDown(content):
    return markdown.markdown(content)
def simmilarList(search):
    """
    Checking if query equals any page existing. If not returning list of simmilar pages.
    """
    simmilarList = []
    for page in list_entries():
        if search.casefold() == page.casefold():
            return page
        elif search.casefold() in page.casefold():
            simmilarList.append(page)
    return simmilarList

def ifExist(title):
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        raise ValueError("Entries with this title exists")