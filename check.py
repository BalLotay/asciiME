import re 
def final():
    """final project details"""
    text = open("README.md").read().lower()
    if len(text) < 2500:
        print("Description is not long enough.")
    else:
        print(len(text))
       
    urls = re.findall('https?:\/\/[\w/\-?=%.]+\.[\w/\-?=%.]+', text)
    if not urls:
        print("Video URL is missing.")
    else: 
        print(urls)

final()