import pickle
import numpy as np


def recommendMeMovies(genre, top=5):
	[actionToStore, adventureToStore, childToStore, crimeToStore, docToStore, dramaToStore,
	fanToStore, noirToStore, horrorToStore, musToStore, mystToStore, romToStore, sciToStore, thriToStore, warToStore,
	westToStore, noGToStore] = pickle.load(open('sorted_movies_by_views.pickle', 'rb'))

	#Ugly code :D
	if genre == 'Action' or genre == 0:
		return actionToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)

	elif genre == 'Adventure' or genre == 1:
		return adventureToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)

	elif genre == 'Children' or genre == 2:
		return childToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)

	elif genre == 'Crime' or genre == 3:
		return crimeToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)

	elif genre == 'Documentary' or genre == 4:
		return docToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)

	elif genre == 'Drama' or genre == 5:
		return dramaToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)

	elif genre == 'Fantasy' or genre == 6:
		return fanToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)

	elif genre == 'Film noir' or genre == 7:
		return noirToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)

	elif genre == 'Horror' or genre == 8:
		return horrorToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)

	elif genre == 'Musical' or genre == 9:
		return musToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)

	elif genre == 'Mystery' or genre == 10:
		return mystToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)

	elif genre == 'Romance' or genre == 11:
		return romToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)

	elif genre == 'Sci-fi' or genre == 12:
		return sciToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)

	elif genre == 'Thriller' or genre == 13:
		return thriToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)

	elif genre == 'War' or genre == 14:
		return warToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)

	elif genre == 'Western' or genre == 15:
		return westToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)

	elif genre == 'Not-specified' or genre == 16:
		return noGToStore[['title', 'times_watched']].iloc[:top].to_string(index=False, header=False)


def searchByTitle(search):
	[movieDetailed] = pickle.load(open('full_base_movies.pickle', 'rb'))
	print(movieDetailed[movieDetailed['title'].str.lower().str.contains(search)]['title'].to_string(index=False, header=False))



def recommendationTop(movie):
	[movieDetailed] = pickle.load(open('full_base_movies.pickle', 'rb'))
	list_of_movies = movieDetailed[movieDetailed['title'].str.lower().str.contains(movie)]['title']
	if len(list_of_movies) == 0:
		print("Unfortunately we don't have your movie in the database.")
		print("Would you like to search for movies? There is possibility that you have misspelled the name.")
	else:
		print("We found more titles that may be similar to the movie you requested.")
		list_for_recon = movieDetailed[movieDetailed['title'].str.lower().str.contains(movie)]
		#         print(list_for_recon['title'])
		list_for_recon = list_for_recon.sort_values('times_watched', axis=0, ascending=False)
		list_yo = list_for_recon.iloc[0][3:].tolist()
		index_list = []
		for i in range(len(list_yo)):
			if list_yo[i] == 1.0:
				index_list.append(i)
		lets_rank = []
		for i in range(len(index_list)):
			print(recommendMeMovies(index_list[i], 1))
