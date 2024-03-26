Alpha Vision +
==============================

Chess board state detection and move recommendation system

Project Summary
------------
Our capstone project aims to create an end-to-end comprehensive chess analysis tool that integrates digital insights into over the board play in chess. The project's primary objective is to utilize Computer Vision (CV) technology to interpret 3-D images of chess boards, converting these into 2-D board states using Forsyth–Edwards Notation (FEN). 

Subsequently, we will process the position and provide the user with chess insights to better help them navigate the position as they are playing or analyzing. We plan to build two types of chess engine systems. 

The primary focus of the first system will be matching scanned board states with similar positions from a database of master games. The second system will be reinforcement learning based using AlphaZero algorithm. The project intends to bridge the gap between offline chess and online analysis resources, providing users with gameplan inspiration through recognition of chess positions and advanced game analysis, offering a powerful resource for both enthusiasts and serious chess players.

Datasets
------------
Chess Games

- [http://caissabase.co.uk/](http://caissabase.co.uk/)
- [https://theweekinchess.com/twic](https://theweekinchess.com/twic)
- [https://database.lichess.org/](https://theweekinchess.com/twic)

Computer Vision

- [https://www.kaggle.com/datasets/thefamousrat/synthetic-chess-board-images/data](https://theweekinchess.com/twic)
- [https://doi.org/10.4121/99b5c721-280b-450b-b058-b2900b69a90f.v2](https://theweekinchess.com/twic)
- [https://public.roboflow.com/object-detection/chess-full](https://theweekinchess.com/twic)
- [https://paperswithcode.com/dataset/dataset-of-rendered-chess-game-state-images](https://theweekinchess.com/twic)


Computer Vision
---------------
This project extends the work of Georg Wölflein and Patrick Lindemann and their [chesscog](https://github.com/georg-wolflein/chesscog) project. In order to more easily get started we are using an older version of python to maintain the compatibility of the libraries used in that original project. In addition rather than using their setup method we have created a requirements.txt that can be used to install the necessary libraries and versions in your python 3.10 environment. Using venv from the root dir:

```
# create environment using python 3.10 (install if you don't have it already)
python3.10 -m venv .venv

source .venv/bin/activate

# validate the correct version of python
✗ python --version        
Python 3.10.13

# install dependencies
pip install -r requirements.txt
```
