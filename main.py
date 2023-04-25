import os
import re
import requests

# create the COVERS folder if it does not exist
if not os.path.exists("COVERS"):
    os.mkdir("COVERS")

# create the upscaled_covers folder if it does not exist
if not os.path.exists("COVERS/upscaled_covers"):
    os.mkdir("COVERS/upscaled_covers")

# read the LINK.txt file
if not os.path.exists("LINK.txt"):
    with open("LINK.txt", "w") as file:
        file.write("https://www.wattpad.com/story/315053311")
        print("LINK.txt file did not exist. Creating a new one with a sample link.")
else:
    with open("LINK.txt", "r") as file:
        lines = file.readlines()

    # check if the file is empty or has only whitespace
    if not lines or all(line.isspace() for line in lines):
        print("LINK.txt file is empty. Please add Wattpad book links.")
    else:
        # regular expression to match Wattpad book links
        regex = r"https://www\.wattpad\.com/story/(\d+)"
        # read the PROXIES.txt file
        with open("PROXIES.txt", "r") as file:
            proxies = [line.strip() for line in file.readlines()]

        for link in lines:
            # check if the link is a valid Wattpad book link
            match = re.match(regex, link)
            if not match:
                print(f"{link.strip()} is not a valid Wattpad book link.")
            else:
                book_id = match.group(1)
                image_url = f"https://img.wattpad.com/cover/{book_id}-512-k615882.jpg"
                # download the image using a different proxy for each link
                for proxy in proxies:
                    try:
                        response = requests.get(image_url, proxies={"http": proxy, "https": proxy})
                        if response.ok:
                            with open(f"COVERS/{book_id}.png", "wb") as file:
                                file.write(response.content)
                            print(f"Cover image for book {book_id} downloaded successfully.")
                            
                            # upscale the image using waifu2x
                            waifu2x_url = "https://waifu2x.booru.pics/Home/IndexPost"
                            files = {"img": open(f"COVERS/{book_id}.png", "rb")}
                            response = requests.post(waifu2x_url, files=files)
                            if response.ok:
                                with open(f"COVERS/upscaled_covers/{book_id}.png", "wb") as file:
                                    file.write(response.content)
                                print(f"Cover image for book {book_id} upscaled successfully.")
                            else:
                                print(f"Failed to upscale cover image for book {book_id}.")
                            break
                        else:
                            print(f"Failed to download cover image for book {book_id} using proxy {proxy}.")
                    except requests.exceptions.RequestException as e:
                        print(f"An error occurred while downloading cover image for book {book_id} using proxy {proxy}.")
                        print(e)
