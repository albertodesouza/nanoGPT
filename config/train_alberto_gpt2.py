# config for training GPT-2 (124M) down to very nice loss of ~2.85 on 1 node of 8X A100 40GB
# launch as the following (e.g. in a screen session) and wait ~5 days:
# $ torchrun --standalone --nproc_per_node=8 train.py config/train_gpt2.py

# wandb_log = True
wandb_project = 'owt'
wandb_run_name='gpt2'

# these make the total batch size be ~0.5M
# 12 batch size * 1024 block size * 5 gradaccum * 8 GPUs = 491,520
batch_size = 2
block_size = 512
gradient_accumulation_steps = 5

# this makes total number of tokens be 300B
learning_rate = 9e-4 # 6e-4 # 9e-4 # 6e-4 # max learning rate
min_lr = 6e-05 # minimum learning rate, should be ~= learning_rate/10 per Chinchilla
max_iters = 6000
lr_decay_iters = 5000 # 3000
warmup_iters = 500 # how many steps to warm up for

# eval stuff
eval_interval = 500
eval_iters = 200
log_interval = 10

# weight decay
weight_decay = 1e-1
