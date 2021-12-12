import onnx
import numpy as np
import onnxruntime as ort
import torch
from PIL import Image
import torchvision.transforms as transforms

"""
ONNX will load the model
ONNX-runtime will run the model
PIL Image will load the Image
"""

# Load ONNX Model
model_path = '/home/huairui/Code/ROS2_Computer_Vision/onnx_runtime_project/densenet_P1_shapes_3000_dataset.onnx'
onnx_model = onnx.load(model_path)

"""
# Check the model
try:
    onnx.checker.check_model(onnx_model)
except onnx.checker.ValidationError as e:
    print('The model is invalid: %s' % e)
else:
    print('The model is valid!')
"""

"""
the thing fed to the model is TENSOR
"""

# Load the image and convert it
img = Image.open('square-train-7.png')
# resize = transforms.Resize([224,224])
# img = resize(img)

# Convert the Image
img_ycbcr = img.convert('YCbCr')
img_y, img_cb, img_cr = img_ycbcr.split()

"""
The greyscale image(Y) is more sensitive to the human eye,
we are interested in this component which we will be transforming -> tensor
"""

# Convert to tensor
to_tensor = transforms.ToTensor()
img_y = to_tensor(img_y)
img_y.unsqueeze_(0)

# Create inference session
test_sess = ort.InferenceSession(model_path)

def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

ort_inputs = {test_sess.get_inputs()[0].name: to_numpy(img_y)}
print(ort_inputs)
ort_outs = test_sess.run(None,ort_inputs)
# img_out_y = ort_outs[0]