# importing requests package 
import requests	 

def trndnews(): 
	
	# BBC news api 
	main_url = " http://newsapi.org/v2/top-headlines?country=in&apiKey=59ff055b7c754a10a1f8afb4583ef1ab"

	# fetching data in json format 
	page = requests.get(main_url).json() 

	# getting all articles in a string article 
	article = page["articles"] 

	# empty list which will 
	# contain all trending news 
	results = [] 
	
	for ar in article: 
		results.append(ar["title"]) 
		
	for i in range(len(results)): 
		
		# printing all trending news
		print(i + 1, results[i]) 	
trndnews() 
