from pathlib import Path

def counts_words(filename):
    """Cuenta el número aproximado de palabras de un archivo."""
    try:
        path = Path(filename)
        contents = path.read_text()
    except FileNotFoundError:
        pass
        #print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['books/alice.txt', 'books/little_women.txt', 'books/moby_dick.txt', 'books/siddhartha.txt']
for filename in filenames:
    counts_words(filename)
    
