seed=${1:-55}
dataset_name=${2:-"image"}
type=${3:-"adversarial"}
model_path=${4:-"./checkpoints/llava-v1.5-7b"}
cd_alpha=${5:-1}
cd_beta=${6:-0.2}
noise_step=${7:-500}
if [[ $dataset_name == 'image' || $dataset_name == 'aokvqa' ]]; then
  image_folder=../AMBER/image
else
  image_folder=./data/gqa/images
fi

python ./eval/object_hallucination_vqa_llava.py \
--model-path ${model_path} \
--question-file ../AMBER/data/query/query_generative.json \
--image-folder ${image_folder} \
--answers-file ../AMBER/data/output_vcd_cubic.jsonl \
--cd_alpha $cd_alpha \
--cd_beta $cd_beta \
--use_cd \
--noise_step $noise_step \
--seed ${seed}




: << 'EOF'
seed=${1:-55}
dataset_name=${2:-"coco"}
type=${3:-"adversarial"}
model_path=${4:-"./checkpoints/llava-v1.5-7b"}
cd_alpha=${5:-1}
cd_beta=${6:-0.2}
noise_step=${7:-500}
if [[ $dataset_name == 'coco' || $dataset_name == 'aokvqa' ]]; then
  image_folder=./data/coco/val2014
else
  image_folder=./data/gqa/images
fi

python ./eval/object_hallucination_vqa_llava.py \
--model-path ${model_path} \
--question-file ./data/POPE/${dataset_name}/${dataset_name}_pope_${type}.json \
--image-folder ${image_folder} \
--answers-file ./output/llava15_${dataset_name}_pope_${type}_answers_no_cd2_seed${seed}.jsonl \
--cd_alpha $cd_alpha \
--cd_beta $cd_beta \
--noise_step $noise_step \
--seed ${seed}
EOF

