# Word-Ladder

This is about a programming project called "word ladder" that involves implementing a game where the user is prompted with a source word and a target word, and they have to provide a sequence of words that form a ladder from the source word to the target word. ​

The project is divided into three phases, each with specific tasks and requirements. ​ 

Phase 1 involves reading a list of 5-letter words from a file, building a word network, and computing various properties of the network. ​ 
Phase 2 focuses on traversing the word network and finding shortest paths. ​ 
Phase 3 involves writing a word ladder game program with preprocessing, word choice, and user interaction tasks. ​


Determining easy and hard words in Phase 3:

In Phase 3, the distinction between "easy" and "hard" words is determined based on their frequency of usage. ​ The program reads from six text files downloaded from Project Gutenberg. ​The frequency of each word in the list of 5,757 words is computed in these texts. ​
To determine the "easy" words, a parameter called "p" is used. ​This parameter is a percentage value between 0 and 100, specified in the file "parameters.txt". ​The program takes "p%" of the most frequently used words from the list and designates them as "easy" words. ​ The remaining words are considered "hard" words. ​
For example, if "p" is set to 30, then 30% of the most frequently used words (approximately 1348 words) will be classified as "easy" words, while the rest will be classified as "hard" words. ​
The goal is to select source and target words that are connected by a word ladder primarily composed of "easy" words in the "easy" version of the game. ​ In the "hard" version, there is no distinction between "easy" and "hard" words, and any word can be chosen as the source and target. 


Definition of weighted word network:
A weighted word network is a type of network where each node (word) is assigned a weight or value. ​ The weight represents the importance or significance of the node within the network. In the context of the word ladder game, a weighted word network is used to prioritize certain words over others based on their weight. ​
In the word ladder game, the weight of a word is typically used to indicate its difficulty or level of challenge. ​ For example, in the "easy" version of the game, "hard" words are assigned a higher weight compared to "easy" words. ​ This means that paths in the network that include "hard" words will have a longer distance or higher cost. ​
When finding a path or traversing the weighted word network, the distance between two nodes is calculated by summing the number of edges in the path and the weights of the nodes along the path. ​ This allows the program to prioritize paths that contain fewer "hard" words and favor paths with lower overall weight.
By incorporating weights into the word network, the program can guide the selection of source and target words in a way that aligns with the desired level of difficulty for the game. 


​​​List of all files necessary for the project:

Phase 2 and Phase 3:

words.txt: List of words used in the game.

parameters.txt: Contains game parameters.

gameInformation.txt: Contains preprocessed game information.

Project Gutenberg text files:

pg1342.txt

pg2641.txt

pg2701.txt

pg37106.txt

pg64317.txt

pg84.txt
