import requests

url = "http://127.0.0.1:5000"
pos = {
    "text": "this is the best product!!"
}
neg = {
    "text": "this is the worst product!!"
}



response1 = requests.post(url + "/analyse", json=pos)
response2 = requests.post(url + "/analyse", json=neg)

print("======================================")
print("Response 1: ", response1.json())
print("======================================")
print("Response 2: ", response2.json())
print("======================================")
