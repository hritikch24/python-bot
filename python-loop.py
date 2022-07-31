import requests
for i in range(1000):
    res=requests.get("https://www.youtube.com/watch?v=XVPzBIGvWRE")
    print(res)
print("done")
