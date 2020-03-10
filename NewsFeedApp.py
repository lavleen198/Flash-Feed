import requests
class NewsFeedApp:
    def shownews(): 
        main_url = " https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=9031443668e745a3ad04cfc1f0296c63"
        res = requests.get(main_url).json() 
        article = res["articles"] 
        results=[]
        
        for ar in article: 
            results.append({'title':ar["title"],'url':ar['url'],'author':ar['author']})   
        
        return results    
        
    def shownewsCat(category): 
        main_url = "http://newsapi.org/v2/top-headlines?country=in&category="+category+"&apiKey=9031443668e745a3ad04cfc1f0296c63"      
        res = requests.get(main_url).json() 
        article = res["articles"]      
        results=[]

        for ar in article: 
            results.append({'title':ar["title"],'url':ar['url'],'author':ar['author']})   
        
        return results    

               
      
if __name__=="__main__":
    NewsFeedApp.shownews()
