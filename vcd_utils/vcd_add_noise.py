import torch
import torchvision
from torchvision.transforms import functional as F

def add_diffusion_noise(image_tensor, noise_step):
    num_steps = 1000  # Number of diffusion steps

    # decide beta in each step
    betas = torch.linspace(-6,6,num_steps)
    betas = torch.sigmoid(betas) * (0.5e-2 - 1e-5) + 1e-5

    # decide alphas in each step
    alphas = 1 - betas
    alphas_prod = torch.cumprod(alphas, dim=0)
    alphas_prod_p = torch.cat([torch.tensor([1]).float(), alphas_prod[:-1]],0) # p for previous
    alphas_bar_sqrt = torch.sqrt(alphas_prod)
    one_minus_alphas_bar_log = torch.log(1 - alphas_prod)
    one_minus_alphas_bar_sqrt = torch.sqrt(1 - alphas_prod)

    def q_x(x_0,t):
        noise = torch.randn_like(x_0)
        alphas_t = alphas_bar_sqrt[t]
        alphas_1_m_t = one_minus_alphas_bar_sqrt[t]
        return (alphas_t*x_0 + alphas_1_m_t*noise)

    noise_delta = int(noise_step) # from 0-999
    noisy_image = image_tensor.clone()
    image_tensor_cd = q_x(noisy_image,noise_step) 

    return image_tensor_cd

def add_blurred_objects_noise(image_tensor, kernel_size=15, threshold=0.9):
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    model.eval()
    with torch.no_grad():
        predictions = model([image_tensor])
    boxes = predictions[0]['boxes']
    scores = predictions[0]['scores']
    filtered_boxes = boxes[scores > threshold].cpu().tolist()

    channels, height, width = image_tensor.shape
    blurred_image = image_tensor.clone()
    
    # Define a Gaussian blur kernel
    def gaussian_kernel(size, sigma=1.0):
        coords = torch.arange(size) - size // 2
        kernel_1d = torch.exp(-(coords**2) / (2 * sigma**2))
        kernel_2d = kernel_1d[:, None] * kernel_1d[None, :]
        return kernel_2d / kernel_2d.sum()

    kernel = gaussian_kernel(kernel_size, sigma=kernel_size / 6).unsqueeze(0).unsqueeze(0)

    for (x1, y1, x2, y2) in filtered_boxes:  # Use filtered_boxes for valid ROIs
        x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])  # Ensure coordinates are integers

        # Extract the region of interest (ROI)
        region = blurred_image[:, y1:y2, x1:x2]

        # Ensure region dimensions are compatible
        if region.shape[1] < kernel_size or region.shape[2] < kernel_size:
            continue  # Skip if region is smaller than the kernel size
        
        # Apply Gaussian blur to the region
        for c in range(channels):
            region_slice = region[c:c+1].unsqueeze(0)  # Add batch dimension
            blurred_region = torch.nn.functional.conv2d(
                region_slice, kernel, padding=kernel_size // 2
            ).squeeze(0)  # Remove batch dimension
            region[c:c+1] = blurred_region
        
        # Replace the blurred region back into the image
        blurred_image[:, y1:y2, x1:x2] = region

    return blurred_image

