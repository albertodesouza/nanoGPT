https://pytorch.org/get-started/pytorch-2.0/
pip3 install numpy --pre torch==2.0.0.dev20230204+cu117 torchvision==0.15.0.dev20230204+cu117 torchaudio==2.0.0.dev20230204+cu117 --force-reinstall --index-url https://download.pytorch.org/whl/nightly/cu117

python3 train.py config/train_alberto_gpt2.py --compile=True
stdbuf -o0 nohup python3 train.py config/train_alberto_gpt2_big.py --compile=True
