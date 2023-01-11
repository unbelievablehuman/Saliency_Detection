import os
from PIL import Image
from torch.utils.data import Dataset

class Mydata(Dataset):
    def __init__(self,root_dir, second_dir):
        self.root_dir = root_dir
        self.second_dir = second_dir
        self.path = os.path.join(self.root_dir,self.second_dir)
        self.img_path = os.listdir(self.path)

    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        img_item_path = os.path.join(self.root_dir,self.second_dir, img_name)
        img = Image.open(img_item_path)
        #label = self.second_dir
        return img, img_name

    def __len__(self):
        return len(self.img_path)
