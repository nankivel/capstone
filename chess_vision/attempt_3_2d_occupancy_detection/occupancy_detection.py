import os
from src.occupancy import detect_occupancy

if __name__ == "__main__":
    directory = "data/raw/"
    for filename in os.listdir(directory):
        if filename.endswith('.jpeg'):
            path_image = os.path.join(directory, filename)
            detect_occupancy(path_image,
                             threshold=15.0
                             )
