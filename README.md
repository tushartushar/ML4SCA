# Machine Learning for Source Code Analysis (ML4SCA)

It is a live survey of studies that use machine learning techniques for source code analysis. We intend to add new studies as they emerge and invite pull requests from the SE comunity to help us keep this live survey updated and current. 

The [website](https://tusharma.in/ML4SCA) renders the data in this repository directly. 

## How to add a new study
- **Before, you add a new study**, please ensure that the study that you would like to add is not present in the collection already.
- Add your paper metadata in the ``ML4SCA/assets/JSON/paperdata.json`` file in the following format.
```
{
	 "py/object": "data.DataClassPaper",
	 "Title": "",
	 "year": YYYY,
	 "ML_Techniques": "",
	 "Category": "",
	 "Sub_category": "",
	 "Venue": "",
	 "Link": "",
	 "bibtex": "",
	 "abstract": ""
}
```
- Create a new pull request with your edits.
- Do not change the value of "py/object" key. 
- Value for "ML_Techniques" can take one of the following values: AB, AE, AIS, ANFIS, ANN, ARM, B, BERT, Bi-GRU, Bi-LSTM, Bi-RNN, BiNN, BMN, BN, BP-ANN, BR, BTE, CART, CC, CCN, CNN, COBWEB, Code2Vec, CoForest-RF, CSC, DBN, DDQN, DNN, Doc2Vec, DR, DS, DT, ELM, EM, EN-DE, FIS, FL, FR-CNN, GAN, GB, GBDT, GBM, GBT, GD, GED, GEP, GGNN, GINN, Glove, GNB, GNN, GPT-C, GRASSHOPER, GRU, HAN, HC, HMM, Inst2Vec, KM, KNN, KS, Lasso, LB, LC, LCM, LDA, LLR, LMSR, LOG, LR, LSTM, MLP, MMR, MNB, MNN, MTN, MVE, NB, NLM, NMT, NN, NNC, NND, Node2Vec, OCC, OR, PN, PNN, POLY, PR, PSO, ReNN, ResNet, RF, RGNN, Ripper, RL, RNN, RT, SA, Seq2Seq, SLP, SMO, SMT, SOM, SVE, SVLR, SVM, SVR, TF, TNB, V, VSL, Word2Vec.
- Multiple values are allowed separated with a comma. The full form of the above ML techniques can be found in ``assets/ML.csv`` file in this repository. If your ML technique is not in the above list, you may add a new entry to ``ML.csv`` file and use the technique in the paper metadata.
- Values for "Category" and "Sub_category" should have one of the following values: Code completion, Code representation, Code review, Code search, Dataset mining, General, Program comprehension (sub categories: Program classification, Change analysis, Entity identification/recommendation, Code summarization), Program synthesis (sub categories: Program repair, Refactoring, Program translation), Testing (sub categories: Defect prediction, Test data/case generation, Effort prediction), Quality assessment (sub categories: Code smell detection, Clone detection, Quality prediction, Technical debt identification), Refactoring, Vulnerability analysis.

An example of above template is given below.

```
{
    "py/object": "data.DataClassPaper",
    "Title": "On Learning Meaningful Code Changes Via Neural Machine Translation",
    "year": 2019,
    "ML_Techniques": "EN-DE",
    "Category": "Program comprehension",
    "Sub_category": "Change analysis",
    "Venue": "ICSE",
    "Link": "https://ieeexplore.ieee.org/abstract/document/8811910",
    "bibtex": "INPROCEEDINGS{Tufano2019_390,\n author = \"{Tufano}, M. and {Pantiuchina}, J. and {Watson}, C. and {Bavota}, G. and {Poshyvanyk}, D.\",\n booktitle = \"2019 IEEE/ACM 41st International Conference on Software Engineering (ICSE)\",\n title = \"On Learning Meaningful Code Changes Via Neural Machine Translation\",\n year = \"2019\",\n volume = \"\",\n number = \"\",\n pages = \"25-36\",\n doi = \"10.1109/ICSE.2019.00021\"\n}\n\n",
    "abstract": "Recent years have seen the rise of Deep Learning (DL) techniques applied to source code. Researchers have exploited DL to automate several development and maintenance tasks, such as writing commit messages, generating comments and detecting vulnerabilities among others. One of the long lasting dreams of applying DL to source code is the possibility to automate non-trivial coding activities. While some steps in this direction have been taken (e.g., learning how to fix bugs), there is still a glaring lack of empirical evidence on the types of code changes that can be learned and automatically applied by DL.\n\nOur goal is to make this first important step by quantitatively and qualitatively investigating the ability of a Neural Machine Translation (NMT) model to learn how to automatically apply code changes implemented by developers during pull requests. We train and experiment with the NMT model on a set of 236k pairs of code components before and after the implementation of the changes provided in the pull requests. We show that, when applied in a narrow enough context (i.e., small/medium-sized pairs of methods before/after the pull request changes), NMT can automatically replicate the changes implemented by developers during pull requests in up to 36% of the cases. Moreover, our qualitative analysis shows that the model is capable of learning and replicating a wide variety of meaningful code changes, especially refactorings and bug-fixing activities. Our results pave the way for novel research in the area of DL on code, such as the automatic learning and applications of refactoring."
},
```


## Acknowledgements
This work is authored by [Tushar Sharma](http://www.tusharma.in), Maria Kechagia, Stefanos Georgiou, Rohit Tiwari, Indira Vats, Hadi Moazen, and Federica Sarro.
