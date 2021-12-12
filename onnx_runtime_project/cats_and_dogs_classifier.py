from torchvision.datasets import ImageFolder
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from torchvision import transforms

"""
Cats dogs Classifier build
what kind of data dp the neural network need for training?
    -Data -> Prediction
    -Prediction compare with label -> Loss
    -Back propagation

Pytorch:
Convert matrix to tensor (datatype in pytorch)

torch.Size([3,200,200]),0)
3 channels: RGB,200: width,200: height, 0: label
"""
# Image Loader
dataset_path = "cats_and_dogs/dataset/training_set"
dataset = ImageFolder(dataset_path)
train_Data, test_Data, train_Label, test_Lable = train_test_split(dataset.imgs,dataset.targets,test_size=0.2,random_state=0)

# Conver datatype to tensor
transform = transforms.Compose([
    transforms.Resize((200, 200)),
    transforms.ToTensor(),
    transforms.Normalize([0.5]*3,[0.5]*3)
])


class ImageLoader(Dataset):
    def __init__(self,dataset,transform=None):
        self.dataset = self.check_Channel(dataset)
        self.transform = transform
    """
    Check whether the image has 3 channels or just grayscale
    if it is RGB, then add it to the List
    """
    def check_Channel(selfself,dataset):
        datasetRGB = []
        for index in range(len(dataset)):
            if Image.open(dataset[index][0]).getbands() == ('R','G','B'):
                datasetRGB.append(dataset[index])
        return datasetRGB

    """
    make each Image n*n size, by "fill the blank space"
    then return it
    """
    def getResizedImage(self,item):
        image = Image.open(self.dataset[item][0])
        _,_,width,height = image.getbbox()

        factor = (0, 0, width, width) if width > height else (0, 0, height, height)

        img_resize = image.crop(factor)
        return image.crop(factor)

    def __getitem__(self, item):
        image = self.getResizedImage(item)
        if transform is not None:
            return self.transform(image), self.dataset[item][1] #Label
        return image, self.dataset[item][1] #Label


    def __len__(self):
        return len(self.dataset)

imageLoader = ImageLoader(train_Data,transform)
print(imageLoader[0][0].size())

dataLoader = DataLoader(imageLoader, batch_size=10, shuffle=True)

data = iter(dataLoader)

d = next(data)

print(d[0].size())

