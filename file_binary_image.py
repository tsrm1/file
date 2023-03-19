import requests

response = requests.get('https://assets.reedpopcdn.com/cyberpunk_hacker_A3GLQcj.jpg/BROK/resize/1920x1920%3E/format/jpg/quality/80/cyberpunk_hacker_A3GLQcj.jpg')

with open(file='cyberpunk.jpg', mode='wb') as file:
    file.write(response.content)
