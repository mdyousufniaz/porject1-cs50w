from manage import main
from encyclopedia.util import get_entry
from markdown2 import markdown

main()
print(markdown(get_entry("CSS")))
