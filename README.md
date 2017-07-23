# Movie Recommendation system

The movie recommender is using pandas as back-end. When you have watched a movie, it takes into consideration genres the watched movie belongs to. Therefore, it recommends you the top movie, based on user's watch counter, from each genre the movie was in.

## Dataset

The dataset used for this project is MovieLens, you can download it [here]( https://grouplens.org/datasets/movielens/).

## Install

### &nbsp;&nbsp;&nbsp; Supported Python version
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Python version used in this project: 3.5+

### &nbsp;&nbsp;&nbsp; Libraries used

> *  [Pandas](http://pandas.pydata.org) 0.18.0
> *  [Numpy](http://www.numpy.org) 1.10.4
> *  [Pickle](https://docs.python.org/3/library/pickle.html)

## Code

To find out how data is pickled, or you want to pickle your own data examine file: **createPickleMovies.py**.

After you have preprocessed and pickled your data go to file **recommender_methods.py**. In this file you will find all functionality that my recommender can do for now. (recommend, search, recommend_by_genre).

BONUS code: you will find file called **results_of_recommender.ipynb** run this file to see how it performs.

## Run

To run this project you will need some software, like Anaconda, which provides support for running .ipynb files (Jupyter Notebook).

After making sure you have that, you can run from a terminal or cmd next lines:

`ipython notebook results_of_recommender.ipynb`

or

`jupyter notebook results_of_recommender.ipynb`

To run a file with recommendation methods execute this line in your console:

`python recommender_methods.py`

## Bugs

You will find that some movies will give weird results, this recommender can be improved and for now it is not perfect.
Another wierd thing is that when you search for a movie, you should search with all lower caps because of the backend setup.

### Ways to improve

You can improve this recommender by using the Autoencoder or the RBF.


## License

MIT License

Copyright (c) 2017 Luka Anicin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
