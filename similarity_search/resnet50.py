from PIL import Image
import torch
from torchvision import transforms as T
from torchvision.models import resnet50, ResNet50_Weights

resnet50 = resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
model = torch.nn.Sequential(*list(resnet50.children())[:-1])
model.eval()


def embedding(image_path):
    resize = T.Resize((256, 256))
    crop = T.CenterCrop((224, 224))
    tensor = T.ToTensor()

    image = Image.open(image_path).convert("RGB")
    tensor_image = tensor(crop(resize(image)))

    with torch.no_grad():
        embedding = model(tensor_image.unsqueeze(0))
        embedding = embedding.view(embedding.size(0), -1)
    return embedding.detach().numpy()
