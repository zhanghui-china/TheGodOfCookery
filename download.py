
import os
from modelscope import snapshot_download
import whisper

# download  shishen model
finetuned = True
if finetuned:
   if not os.path.exists(os.environ.get('HOME') + "/zhanghuiATchina/zhangxiaobai_shishen2_full"):
       model_dir = snapshot_download('zhanghuiATchina/zhangxiaobai_shishen2_full', cache_dir=os.environ.get('HOME')+'/models')
       
else:
    if not os.path.exists(os.environ.get('HOME') + "/Shanghai_AI_Laboratory/internlm2-chat-7b"):
        model_dir = snapshot_download('Shanghai_AI_Laboratory/internlm2-chat-7b', cache_dir=os.environ.get('HOME')+'/models')

os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

# download m3e model
if not os.path.exists(os.environ.get('HOME') + '/models/m3e-base'):
    command_str = 'huggingface-cli download --resume-download moka-ai/m3e-base --local-dir-use-symlinks False --local-dir '+ os.environ.get('HOME') + '/models/m3e-base'
    os.system(command_str)

# download whisper models
scales = ["tiny", "base", "small", "medium", "large"]
for scale in scales:
    whisper.load_model(scale)

# download SD model
if not os.path.exists(os.environ.get('HOME') +  '/models/Taiyi-Stable-Diffusion-1B-Chinese-v0.1'):
    command_str = 'huggingface-cli download --resume-download IDEA-CCNL/Taiyi-Stable-Diffusion-1B-Chinese-v0.1 --local-dir-use-symlinks False --local-dir '+ os.environ.get('HOME') + '/models/Taiyi-Stable-Diffusion-1B-Chinese-v0.1'
    os.system(command_str)
