import torch

def calculate_brightness(img) -> float:
    rowlengths = [len(row) for row in img]

    if len(set(rowlengths)) > 1:
        return -1

    tensor1 = torch.tensor(img, dtype=torch.float32)

    if tensor1.numel() == 0:
        return -1

    if ((tensor1 < 0) | (tensor1 > 255)).any():
        return -1

    return round(tensor1.mean().item(), 2)