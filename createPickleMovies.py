import pandas as pd
import pickle
import numpy as np

def createIt():


	#Using 2 datasets for movies and their ratings
	movies = pd.read_csv('movies.csv')
	rating = pd.read_csv('rating.csv')

	#Creating totally new dataframe for moviespopularity
	movie_popularity = rating.iloc[:, 1].values

	unique, counter = np.unique(movie_popularity, return_counts=True)

	votes_perMovie = {'movieId': unique , 'times_watched': counter}
	popularityTable = pd.DataFrame(data=votes_perMovie)

	#Mergin in popularity dataframe with movies dataframe
	movieTable = movies
	movieTable = movieTable.merge(popularityTable, left_on='movieId', right_on='movieId', how='outer')
	#filling nan data with 0
	movieTable['times_watched'].fillna(0, axis=0, inplace=True)
	#creating copy of the colum for movies genres
	genre = movieTable[[2]].copy()
	#spliting each item to list of genres
	t = genre.iloc[:, 0].str.split('|')

	oneHotEncoding = oneHotEncoder_movies(t)
	listUniques = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Wester','(no genres listed)']

	#creating new dataset for oneHotEncoding matrix
	moviesDetailed = pd.DataFrame(data=oneHotEncoding, columns=listUniques)
	moviesDetailed['movieId'] = movieTable['movieId']
	#droping genres colum and mergin movies dataframe with onehot dataframe
	movieDetailed = movieTable.drop('genres', axis=1)
	movieDetailed = movieDetailed.merge(moviesDetailed, left_on='movieId', right_on='movieId', how='outer')

	with open('full_base_movies.pickle', 'wb') as f:
			pickle.dump([movieDetailed], f)

	print("Pickle for all movies have been created.")


	creating_pickle_for_every_genre(movieDetailed)


#creating one hot encoding for future table
def oneHotEncoder_movies(t):
	listUniques = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Wester','(no genres listed)']
	oneHotEncoding = []
	for i in range(len(t)):
		row = np.zeros(len(listUniques))
		for k in range(len(t[i])):
			for j in range(len(listUniques)):
				if(t[i][k] == listUniques[j]):
					row[j] = 1
		oneHotEncoding.append(row)

	return oneHotEncoding

def creating_pickle_for_every_genre(movieDetailed):
	
	#For action
	action = movieDetailed.loc[movieDetailed['Action'] == 1.0]
	actionToStore = action.loc[:, :'times_watched']
	actionToStore = actionToStore.sort_values('times_watched', axis=0, ascending=False)

	#For Adventure
	adventure = movieDetailed.loc[movieDetailed['Adventure'] == 1.0]
	adventureToStore = adventure.loc[:, :'times_watched']
	adventureToStore = adventureToStore.sort_values('times_watched', axis=0, ascending=False)

	#Animation
	animation = movieDetailed.loc[movieDetailed['Animation'] == 1.0]
	animationToStore = animation.loc[:, :'times_watched']
	animationToStore = animationToStore.sort_values('times_watched', axis=0, ascending=False)

	#Children
	child = movieDetailed.loc[movieDetailed['Children'] == 1.0]
	childToStore = child.loc[:, :'times_watched']
	childToStore = childToStore.sort_values('times_watched', axis=0, ascending=False)

	#Comedy
	comedy = movieDetailed.loc[movieDetailed['Comedy'] == 1.0]
	comedyToStore = comedy.loc[:, :'times_watched']
	comedyToStore = comedyToStore.sort_values('times_watched', axis=0, ascending=False)

	#Crime
	crime = movieDetailed.loc[movieDetailed['Crime'] == 1.0]
	crimeToStore = crime.loc[:, :'times_watched']
	crimeToStore = crimeToStore.sort_values('times_watched', axis=0, ascending=False)

	#Documentary
	Documentary = movieDetailed.loc[movieDetailed['Documentary'] == 1.0]
	docToStore = Documentary.loc[:, :'times_watched']
	docToStore = docToStore.sort_values('times_watched', axis=0, ascending=False)

	#Drama
	Drama = movieDetailed.loc[movieDetailed['Drama'] == 1.0]
	dramaToStore = Drama.loc[:, :'times_watched']
	dramaToStore = dramaToStore.sort_values('times_watched', axis=0, ascending=False)

	#Fantasy
	Fantasy = movieDetailed.loc[movieDetailed['Fantasy'] == 1.0]
	fanToStore = Fantasy.loc[:, :'times_watched']
	fanToStore = fanToStore.sort_values('times_watched', axis=0, ascending=False)

	#Film-Noir
	noir = movieDetailed.loc[movieDetailed['Film-Noir'] == 1.0]
	noirToStore = noir.loc[:, :'times_watched']
	noirToStore = noirToStore.sort_values('times_watched', axis=0, ascending=False)

	#Horror
	Horror = movieDetailed.loc[movieDetailed['Horror'] == 1.0]
	horrorToStore = Horror.loc[:, :'times_watched']
	horrorToStore = horrorToStore.sort_values('times_watched', axis=0, ascending=False)

	#Musical
	Musical = movieDetailed.loc[movieDetailed['Musical'] == 1.0]
	musToStore = Musical.loc[:, :'times_watched']
	musToStore = musToStore.sort_values('times_watched', axis=0, ascending=False)

	#Mystery
	Mystery = movieDetailed.loc[movieDetailed['Mystery'] == 1.0]
	mystToStore = Mystery.loc[:, :'times_watched']
	mystToStore = mystToStore.sort_values('times_watched', axis=0, ascending=False)

	#Romance
	Romance = movieDetailed.loc[movieDetailed['Romance'] == 1.0]
	romToStore = Romance.loc[:, :'times_watched']
	romToStore = romToStore.sort_values('times_watched', axis=0, ascending=False)

	#Sci-Fi
	sci = movieDetailed.loc[movieDetailed['Sci-Fi'] == 1.0]
	sciToStore = sci.loc[:, :'times_watched']
	sciToStore = sciToStore.sort_values('times_watched', axis=0, ascending=False)

	#Thriller
	Thriller = movieDetailed.loc[movieDetailed['Thriller'] == 1.0]
	thriToStore = Thriller.loc[:, :'times_watched']
	thriToStore = thriToStore.sort_values('times_watched', axis=0, ascending=False)

	#War
	War = movieDetailed.loc[movieDetailed['War'] == 1.0]
	warToStore = War.loc[:, :'times_watched']
	warToStore = warToStore.sort_values('times_watched', axis=0, ascending=False)

	#Wester
	Wester = movieDetailed.loc[movieDetailed['Wester'] == 1.0]
	westToStore = Wester.loc[:, :'times_watched']
	westToStore = westToStore.sort_values('times_watched', axis=0, ascending=False)

	#(no genres listed) 
	noGan = movieDetailed.loc[movieDetailed['(no genres listed)'] == 1.0]
	noGToStore = noGan.loc[:, :'times_watched']
	noGToStore = noGToStore.sort_values('times_watched', axis=0, ascending=False)

	with open('sorted_movies_by_views.pickle', 'wb') as f:
	    pickle.dump([actionToStore, adventureToStore, childToStore, crimeToStore, docToStore, dramaToStore,
	                fanToStore, noirToStore, horrorToStore, musToStore, mystToStore, romToStore, sciToStore, thriToStore, warToStore,
	                westToStore, noGToStore], f)

	print("Pickle for all geners have been created.")