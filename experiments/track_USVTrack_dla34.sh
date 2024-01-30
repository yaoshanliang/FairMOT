cd src
python track.py mot --exp_id USVTrack_dla34 --data_cfg src/lib/cfg/USVTrack.json --gpus 0 --load_model exp/mot/USVTrack_dla34/model_last.pth --conf_thres 0.6
cd ..