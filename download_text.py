
import requests

# URL of the text content
text_url = "https://www.hplovecraft.com/writings/texts/fiction/cc.aspx"

# Request the content from the URL
response = requests.get(text_url)

# Check if the request was successful
if response.status_code == 200:
    # Extract text content
    text_content = response.text
    
    # Save the text content to a .txt file
    with open("text_content.txt", "w", encoding="utf-8") as file:
        file.write(text_content)
    
    print("Text content successfully saved to text_content.txt")
else:
    print(f"Failed to retrieve text content. Status code: {response.status_code}")
