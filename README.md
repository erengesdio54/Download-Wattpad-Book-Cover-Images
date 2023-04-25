Download Wattpad Book Cover Images
This script downloads the cover images of Wattpad books using their book links. It reads the book links from a LINK.txt file and downloads the cover images to a COVERS folder. If the COVERS folder does not exist, it will be created. It also uses proxies from a PROXIES.txt file to download the images.

Prerequisites
Python 3.x
The requests module (pip install requests)
Usage
Add Wattpad book links to the LINK.txt file. Each link should be on a separate line. A sample link is provided in the file.
(Optional) Add proxies to the PROXIES.txt file. Each proxy should be on a separate line.
Run the script using python download_wattpad_book_covers.py. The script will download the cover images to the COVERS folder.
Note: If the LINK.txt file is empty or has only whitespace, the script will not download any cover images.

Credits
This script was created by erengesdio54.
