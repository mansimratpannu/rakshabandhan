import urllib.request

url = "https://raw.githubusercontent.com/mansimratpannu/rakshabandhan/main/assets/img_4901.jpg"
try:
    req = urllib.request.Request(url, method='HEAD')
    with urllib.request.urlopen(req) as resp:
        print("HTTP Status Code:", resp.status)
        print("Headers:", resp.headers)
except Exception as e:
    print("Failed to fetch raw image URL:", e)
