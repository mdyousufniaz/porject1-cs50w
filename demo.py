# Now you can safely import and use Django components
from manage import main
from encyclopedia.util import get_entry

main()
print(get_entry("CSS"))
