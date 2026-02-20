import torch
import torchvision
from torchvision import models
import torchvision.transforms as transforms
from torch.optim import lr_scheduler
import torch.nn as nn
import os
import time
import torch.optim as optim
from tempfile import TemporaryDirectory

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])


batch_size = 16

dataloader = { }

train_transform = transforms.Compose([
    transforms.RandomResizedCrop(224, scale=(0.8, 1.0)),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(degrees=15),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=(0.485, 0.456, 0.406),
        std=(0.229, 0.224, 0.225)
    )
])

trainset = torchvision.datasets.ImageFolder(root='D:\VS CODE\pycharm\projs\CropClassifier\Dataset\Train', transform= train_transform )
dataloader['Train'] = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
                                          shuffle=True, num_workers=2)

testset = torchvision.datasets.ImageFolder(root='D:\VS CODE\pycharm\projs\CropClassifier\Dataset\Test', transform=transform)
dataloader['Test'] = torch.utils.data.DataLoader(testset, batch_size=batch_size,
                                         shuffle=False, num_workers=2)

validateset  = torchvision.datasets.ImageFolder(root='D:\VS CODE\pycharm\projs\CropClassifier\Dataset\Validate', transform=transform)
dataloader['Validate'] = torch.utils.data.DataLoader(validateset, batch_size=batch_size,
                                         shuffle=False, num_workers=2)

dataset_sizes = {"Train" : len(trainset) , "Test"  : len(testset) ,  "Validate" : len(validateset)}


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def train_model(model, criterion , optimizer , scheduler , num_epoch = 2) :
    since = time.time()


    with TemporaryDirectory() as tempdir:
        best_model_params_path = os.path.join(tempdir, 'best_model_params.pt')

        torch.save(model.state_dict(), best_model_params_path)
        best_acc = 0.0

        for epoch in range(num_epoch) :
            print(f"Epoch {epoch}/{num_epoch - 1}")
            print('-' * 10)

            for phase in ['Train' , 'Validate']:
                if phase == 'Train' :
                    model.train()

                else:
                    model.eval()

                running_loss = 0.0
                running_corrects = 0

                for inputs, labels in dataloader[phase]:
                    inputs = inputs.to(device)
                    labels = labels.to(device)

                    optimizer.zero_grad()

                    with torch.set_grad_enabled(phase == 'Train'):
                        outputs = model(inputs)
                        _, preds = torch.max(outputs, 1)
                        loss = criterion(outputs, labels)

                        if phase == 'Train':
                            loss.backward()
                            optimizer.step()

                    running_loss += loss.item() * inputs.size(0)
                    running_corrects += torch.sum(preds == labels.data)

                epoch_loss = running_loss / dataset_sizes[phase]
                epoch_acc = running_corrects.double() / dataset_sizes[phase]

                print(f'{phase} Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f}')


                if phase == 'Validate' and epoch_acc > best_acc:
                    best_acc = epoch_acc
                    torch.save(model.state_dict(), best_model_params_path)

            scheduler.step()
            print()

        time_elapsed = time.time() - since
        print(f'Training complete in {time_elapsed // 60:.0f}m {time_elapsed % 60:.0f}s')
        print(f'Best val Acc: {best_acc:4f}')


        model.load_state_dict(torch.load(best_model_params_path, weights_only=True))
    return model


def test_model(model, criterion) :
    model.eval()

    running_loss = 0.0
    running_corrects = 0

    with torch.no_grad():
        for inputs, labels in dataloader['Test']:
            inputs = inputs.to(device)
            labels = labels.to(device)

            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)
            loss = criterion(outputs, labels)

            running_loss += loss.item() * inputs.size(0)
            running_corrects += torch.sum(preds == labels)

    test_loss = running_loss /dataset_sizes['Test']
    test_acc = running_corrects.double() / dataset_sizes['Test']

    print(f"Test loss: {test_loss:.4f} Test acc: {test_acc:.4f}")

if __name__ == "__main__":
    print(f"Using {device} device")

    model_ft = models.mobilenet_v3_large(weights='IMAGENET1K_V1')

    for param in model_ft.features.parameters():
        param.requires_grad = False

    num_ftrs = model_ft.classifier[-1].in_features
    model_ft.classifier[-1] = nn.Linear(num_ftrs, 4)

    model_ft = model_ft.to(device)

    criterion = nn.CrossEntropyLoss()

    optimizer_ft = optim.SGD(
        model_ft.classifier.parameters(),
        lr=0.001,
        momentum=0.9
    )
    exp_lr_scheduler = lr_scheduler.StepLR(optimizer_ft, step_size=7, gamma=0.1)

    model_ft = train_model(model_ft, criterion, optimizer_ft, exp_lr_scheduler,
                           num_epoch=10)
    test_model(model_ft, criterion)
    torch.save(model_ft.state_dict(), "D:\VS CODE\pycharm\projs\CropClassifier\models/soil_classifier_model.pt")
    print("Model saved as soil_classifier_model.pt")