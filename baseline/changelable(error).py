import os

data_dir= "/opt/ml/input/data/train/images"

wrong_folders = ["000020_female_Asian_50", "004418_male_Asian_20", "005227_male_Asian_22"]

file_names = ["incorrect_mask.jpg", "normal.jpg", "temp.jpg"]

for folder in wrong_folders:

    image_dir = os.path.join(data_dir, folder)

    incorrect_file = os.path.join(image_dir, file_names[0])

    normal_file = os.path.join(image_dir, file_names[1])

    temp = os.path.join(image_dir, file_names[2])

    os.rename(incorrect_file, temp)  

    os.rename(normal_file, incorrect_file)

    os.rename(temp, normal_file)

    print("Changed File Names")

