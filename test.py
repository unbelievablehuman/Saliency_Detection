from torch.utils.data import DataLoader

import data_loader



root='data/HKU-IS'
second_root='imgs'
batch_size = 4

test_data = data_loader.Mydata(root,second_root)
print(len(test_data))
test_dataloader = DataLoader(dataset=test_data, batch_size=batch_size, shuffle=True)