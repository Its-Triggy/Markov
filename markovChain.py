import numpy as np

#Removes certain special characters from a string
def strip_string(str):
	clean_str = str.replace("'", "")
	clean_str = clean_str.replace("’", "")
	clean_str = clean_str.replace("“", "")
	clean_str = clean_str.replace("”", "")
	clean_str = clean_str.replace("  ", " ")
	clean_str = clean_str.replace('"', "")
	clean_str = clean_str.replace("(", "")
	clean_str = clean_str.replace(")", "")
	clean_str = clean_str.replace(".", " .")
	clean_str = clean_str.replace("&", "")
	#clean_str = clean_str.replace("-", "")
	clean_str = clean_str.replace("_", "")
	clean_str = clean_str.replace("—", ", ")
	clean_str = clean_str.replace(",", " ,")
	
	return clean_str

#Prints a bunch of new lines
def newPage():
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	
#Copy the text from a text-document into a variable called "text"	
text = open("trumpTweets.txt", "r").read().lower()
#text = open("samHarris.txt", "r").read().lower()
#text = open("bush.txt", "r").read().lower()
#text = open("obama.txt", "r").read().lower()
#text = open("huckfin.txt", "r").read().lower()
#text = open("bible.txt", "r").read().lower()
#text = open("triggy.txt", "r").read().lower()
#text = open("rj.txt", "r").read().lower()


#Strip away any unwanted characters
text =  strip_string(text)

#Split the text into a list of words
text_list = text.split(" ")

#Create a list of unique words
unique_words = []
for word in text_list:
    if word not in unique_words:
    	unique_words.append(word)

#Create a dictionary which assigns a number to each unique word
unique_words_dict = { word : i for i, word in enumerate(unique_words) }
unique_words_dict2 = { i : word for i, word in enumerate(unique_words) }

#Create and empty matrix which will track how often word i is followed by word j
frequency_matrix = np.zeros((len(unique_words), len(unique_words)))

#Scan through the text and fill in the frequency_matrix
for i in range(len(text_list)-1):
	current_word = 	text_list[i]
	next_word = 	text_list[i+1]
	frequency_matrix[unique_words_dict[current_word], unique_words_dict[next_word]] += 1	
	#frequency_matrix[unique_words_dict[text_list[i]], unique_words_dict[text_list[i+1]]] += 1

#Convert the frequency_matrix into a likelihood_matrix by dividing each value by the row-sum
likelihood_matrix = frequency_matrix.copy()
for row in range(frequency_matrix.shape[0]):
    if np.sum(frequency_matrix[row]) != 0:
    	likelihood_matrix[row] /= np.sum(frequency_matrix[row])
 
   
M = likelihood_matrix

#next = np.random.randint(len(likelihood_matrix))
next= unique_words_dict["."]

response = "\n"
while response[-1] != "." and response[-1] != "!" and response[-1] != "?":
	next = np.random.choice(len(M[next]), 1, p=M[next])[0]
	if unique_words_dict2[next] == "." or unique_words_dict2[next] == ",":
		response = response + unique_words_dict2[next]
	else:
		response = response + " " + unique_words_dict2[next]

newPage()
print("Your unique Trump tweet is:")
print(response)
print("\n\n\n\n")