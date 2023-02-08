import time

out_dir = 'out-portugues'
eval_interval = 200
wandb_log = False # feel free to turn on
wandb_project = 'portugues'
wandb_run_name = 'ft-' + str(time.time())
compile = False # takes too little time to finetune, not worth it

# save a nice and overfit checkpoint that
# will only speak portugues and forgets
# everything else about the world #dark
always_save_checkpoint = True

dataset = 'portugues'
init_from = 'gpt2' # 'gpt2-medium' # 'gpt2-xl'
batch_size = 1
block_size = 512

learning_rate = 1e-5
max_iters = 1000
decay_lr = False
