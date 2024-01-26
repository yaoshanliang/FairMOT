cd src
python train.py mot --exp_id USVTrack_dla34 --data_cfg '../src/lib/cfg/USVTrack.json' --gpus 1,2,3 --batch_size 64
cd ..