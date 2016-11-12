

For this assignment, you will make a simple "game" that does the following:
* accepts a search term on the command line (e.g., a user should be able to run your game with `$ python mygame.py "Harry Potter"`)
* performs a search on wikipedia using the search term
* takes the content of the top 5 pages returned by the search, and determines the most common adjectives across those pages
* draws a "ball" representing each of the top 6 adjectives
* allows the user to "pop" each balls by typing the first letter in the word contained in the ball

For a demo of how the game should work when it's complete, see [the demo video](https://www.youtube.com/watch?v=o7XdEKSpxEM).

Yes, that's a pretty arbitrary game and it's not really all that fun to play. But it's a GREAT exercise to help us find out if 507 would be redundant for you. 

In order to complete this assignment, you will need to quickly figure out how to install and use three Python libraries that you most likely have never used (though if you have, it's pretty likely that 507 is overkill for you): wikipedia, nltk, and pygame. You will aslo need to be reasonably conversant with Python data structures and be able to map a high-level program description into a working (small) program design.

I have provided some starter code that demonstrates how to render stuff using pygame. You will have to add the following functionality:

* accepting command line arguments
* searching wikipedia
* using nltk to parse the contents of wikipedia pages
* drawing balls with the most common adjectives extracted from wikipedia pages
* allowing the user to delete balls using the keyboard
* when all balls are deleted, display game over screen

Some pointers to get you started:
* Use python 3 (I'm using 3.5.1, and I have no idea what you'll run into if you use a different version of python)
* Use the latest NLTK (3.0) (see <http://www.nltk.org>)
* Use the latest wikipedia api for pytyon (1.4.0) (see <https://pypi.python.org/pypi/wikipedia/>)
* Use the latest pygame (1.9.1) (see <http://pygame.org/download.shtml>)
	* Note that on my MacBook Pro I was able to just pip install pygame and had no issues--I didn't need to install any support drivers or anything. Lucky me! I gather that Windows users may have a bit more of a struggle, but rest assured that pygame is popular enough that you ought to be able to find a solution online for your particular configuration. I would definitely recommend not waiting til the last minute on this, though!

Other notes:
* Please don't use any *other* third-party libraries if at all possible (my solution didn't need any others, so I know it should be possible). Keep in mind that I need to be able to run and grade upwards of 60 of these things, and it won't work if I have to install a bunch of other libraries.
* If you already have a python installation on your machine with a bunch of libraries, etc., I strongly recommend you set up a [virtualenv](https://virtualenv.pypa.io/en/stable/) for this assignment to avoid any possible library confilcts. 

How to submit:
* Push all of your changes to the GitHub repository you created for the assignment.
* [Fill out the submissiom form](https://docs.google.com/forms/d/e/1FAIpQLScWlx-pPS0mC7z1YGwRkzsnQvU2WjNPfBaTQbm-Uj2b-u857g/viewform) ONLY after you have completed your assignment and are ready for it to be graded. Your assignment will only be graded if you submit the form, and it can be graded any time after you submit the form.
* Submissions are due Wednesday 11/16 by 11:59pm.
