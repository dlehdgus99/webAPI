'''
Taobao의 상품ID를 검색했을 때 해당 페이지의 할인된 상품가격, 상품명, 옵션,옵션이미지 등을 반환하는 API, test code
'''


import requests
from bs4 import BeautifulSoup
import urllib.request



def getData(productId):
    url="https://item.taobao.com/item.htm?id="+str(productId)
    sourceCode=requests.get(url)
    plainText=sourceCode.text
    soup = BeautifulSoup(plainText,'html.parser')
    print("\n")


    #Product name
    productName=soup.find(id="J_Title").get_text().strip()
    print("Product Name: "+productName+"\n")


    #Promotion price
    productPrice=soup.find(id="J_StrPrice").get_text().strip()
    print("Promotion Price: "+productPrice+"\n")


    #Options
    print("Options:")
    for option in soup.find_all("li"):
        if option.string is not None:
            print(option.string)

    print("\n")



    #Image
    image=soup.find(id="J_ImgBooth")
    imageLink=image.get('src')
    imageLink="http:"+imageLink


    #print image link
    print(imageLink)



    #download image
    urllib.request.urlretrieve(imageLink,productName)










#Test Code
getData(617822524032)
getData(617822524031)


