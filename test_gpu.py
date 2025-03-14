import torch
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"GPU count: {torch.cuda.device_count()}")
if torch.cuda.is_available():
    print(f"GPU device: {torch.cuda.get_device_name(0)}")
else:
    print("Checking CUDA installation details...")
    import os
    print(f"CUDA_VISIBLE_DEVICES: {os.environ.get('CUDA_VISIBLE_DEVICES', 'Not set')}")
    print(f"NVIDIA_VISIBLE_DEVICES: {os.environ.get('NVIDIA_VISIBLE_DEVICES', 'Not set')}")
    
    # Try importing CUDA directly
    try:
        import torch.cuda
        if hasattr(torch.cuda, '_check_capability'):
            torch.cuda._check_capability()
        print("CUDA import successful")
    except Exception as e:
        print(f"CUDA import error: {e}")
