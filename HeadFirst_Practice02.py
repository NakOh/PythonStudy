movies = ["THe Holy Grail", "The Life of Brian",["Fall in love", "Wind"], "The Meaning of LIfe"]
for each_item in movies:
	if isinstance(each_item, list): #list일 경우 진입~
		for	nested_item in each_item: #list일경우에도 출력.
			print(nested_item)#하나씩 개행되면서 출력됨.
	else: #list아니면 for문으로 출력.
		print(each_item)

print(movies) #그냥 print하면 [] 까지 그냥 싹다 출력됨