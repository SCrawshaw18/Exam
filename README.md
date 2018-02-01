# Project Outline
In my exam project, I compare a variety of different learning algorithms on a game of flappy bird. These algorithms recieve the game image as input, and recieve a reward of +1 for getting a point and -5 for dying. I collected data on the learning curve, average scores, and max scores of all 4 of my algorithms (Deep-Q Learning, Linear Regression with Processed Image, Linear Regression with Raw Image, and Weighted Random). I also compared this to human data in order to contrast human learning curves to program learning curves.

# How to Run Neural Network
In order to run the Nerual Network, which I took from https://yanpanlau.github.io/2016/07/10/FlappyBird-Keras.html, navigate to the Neural Network folder and execute the command 'python3 qlearn.py -m "Run"'. If you would like to train the network from scratch, delete model.h5 and run 'python3 qlearn.py -m "Train"'. I've modified the inital network in order to incorperate scorekeeping, so you should see a scoresheet text file created shortly after you begin running the model.

# How to Run the Linear Regression Algorithms
In order to run the Linear Regression Algorithms, which I modified from Ms. Pries, simply navigate to FlappyBirdPrograms and execute the command "python3 FlappyLinearProcessed.py" or "python3 FlappyLinearRaw.py". The processed version provides the algorithm with a preprocessed image, whereas the the raw version simply provides the normal, colored version of the image. Scoresheets should also be created when you run either of these programs.

# How to Run the Random Version
To run the random player, simply navigate to FlappyBirdPrograms and execute the command "python3 FlappyBirdAdjustedRandom.py" or "python3 FlappyBirdTrueRandom.py". The adjusted random version chooses to flap 20% of the time, whereas the true random version chooses to flap 50% of the time. A scoresheet should be created once you begin running either program.

# How to Play Yourself
To play the game youself, navigate to FlappyBirdHuman and execute the command "python3 flappy.py". Everytime you play, your scores get sent to a php file at flappybird.ma1geek.org. This php file stores your username and score in a database. In order to see past scores, open up your browser and navigate to http://flappybird.ma1geek.org/getScores.php.

# Final Report
My final report can be found at https://docs.google.com/document/d/13GKHVz9j458I85XWg0uC3kVrZpZG3XfHeW3U6BObec8/edit?usp=sharing
