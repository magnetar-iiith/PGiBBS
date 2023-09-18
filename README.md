# Differentially Private Multi-Agent Constraint Optimization

Authors: Sankarshan Damle, Aleksei Triastcyn, Boi Faltings and Sujit Gujar

# TL;DR
We introduce P-Gibbs, the first differentially private DCOP algorithm that preserves constraint privacy. P-Gibbs builds on SD-Gibbs (Nguyen et al., 2019) and preserves constraint privacy using a novel sampling procedure. The sampling procedure combines sub-sampling, randomization through softmax and adds calibrated Gaussian noise to agent utilities.

# Sampling in P-Gibbs

![Alt text](P-Gibbs-Sampling.png?raw=true "P-Gibbs Sampling Procedure")

# Code Usage
We extend the [pyDCOP](https://github.com/Orange-OpenSource/pyDcop) solver to create P-Gibbs. To try the algorithm, run the following commands:

```
python3 -m venv ~/pydcop_env
source ~/pydcop_env/bin/activate
git clone https://github.com/Orange-OpenSource/pyDcop.git
git clone https://github.com/magnetar-iiith/PGiBBS.git
cp PGiBBS/pgibbs.py pyDcop/pydcop/algorithms/
cd pyDcop
pip install -e .[test]
```

To run P-Gibbs, use the following command 
```
pydcop solve --algo pgibbs --algo_param number_of_iterations:50 <your-dcop-instance>
```


## Citation

If you find our work useful, please cite the paper as:

```
@inproceedings{DTFG21,
  author    = {Sankarshan Damle and
               Aleksei Triastcyn and
               Boi Faltings and
               Sujit Gujar},
  title     = {Differentially Private Multi-Agent Constraint Optimization},
  booktitle = {{IEEE/WIC/ACM} WI-IAT},
  pages     = {422--429},
  year      = {2021},
}
```
