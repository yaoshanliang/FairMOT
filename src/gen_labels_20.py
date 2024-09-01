import os.path as osp
import os
import numpy as np


def mkdirs(d):
    if not osp.exists(d):
        os.makedirs(d)


# seq_root = '/gpfs/work/cpt/shanliangyao19/dataset/USVTrack/MCMOT/images/train'
seq_root = '/gpfs/work/cpt/shanliangyao19/dataset/USVTrack/MCMOT/images/test'
# label_root = '/gpfs/work/cpt/shanliangyao19/dataset/USVTrack/MCMOT/labels_with_ids/train'
label_root = '/gpfs/work/cpt/shanliangyao19/dataset/USVTrack/MOT/labels_with_ids/test'
mkdirs(label_root)
seqs = sorted([s for s in os.listdir(seq_root)])

tid_curr = 0
tid_last = -1
for seq in seqs:
    seq_info = open(osp.join(seq_root, seq, 'seqinfo.ini')).read()
    seq_width = int(seq_info[seq_info.find('imWidth=') + 8:seq_info.find('\nimHeight')])
    seq_height = int(seq_info[seq_info.find('imHeight=') + 9:seq_info.find('\nimExt')])

    gt_txt = osp.join(seq_root, seq, 'gt', 'gt.txt')
    gt = np.loadtxt(gt_txt, dtype=np.float64, delimiter=',')

    seq_label_root = osp.join(label_root, seq, 'img1')
    mkdirs(seq_label_root)

    images = sorted(os.listdir(osp.join(seq_root, seq, 'img1')))

    for image in images:
        file_name = image[0:16] + '.txt'
        print(file_name)
        label_fpath = osp.join(seq_label_root, file_name)
        open(label_fpath, 'w')

    # print(images)
    for fid, tid, x, y, w, h, mark, label, _ in gt:
        # if mark == 0 or not label == 1:
        #     print(osp.join(seq_root, seq, 'gt', 'gt.txt'))
        #     print(fid, tid, x, y, w, h, mark, label)
        #     continue
        fid = int(fid)
        tid = int(tid)
        if not tid == tid_last:
            tid_curr += 1
            tid_last = tid
        x += w / 2
        y += h / 2
        # label_fpath = osp.join(seq_label_root, '{:06d}.txt'.format(fid))
        print(seq, fid, images[fid - 1])
        file_name = images[fid - 1][0:16] + '.txt'
        print(file_name)
        label_fpath = osp.join(seq_label_root, file_name)
        # label_str = '0 {:d} {:.6f} {:.6f} {:.6f} {:.6f}\n'.format(
            # tid_curr, x / seq_width, y / seq_height, w / seq_width, h / seq_height)
        
        # For one classes, all labels to 0
        label_str = '{:d} {:d} {:.6f} {:.6f} {:.6f} {:.6f}\n'.format(
            0, tid_curr, x / seq_width, y / seq_height, w / seq_width, h / seq_height)
        print(label_str)
        with open(label_fpath, 'a') as f:
            f.write(label_str)

        # exit()
