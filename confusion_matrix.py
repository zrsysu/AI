{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import LabelEncoder\n",
    "from sklearn.cross_validation import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.svm import SVC\n",
    "from sklearn.metrics import confusion_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "from sklearn.metrics import precision_score, recall_score, f1_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "file = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data',header=None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df.loc[:, 2:].values\n",
    "y = df.loc[:, 1].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "le = LabelEncoder()\n",
    "y = le.fit_transform(y)  #类标整数化"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 划分训练集合测试集合\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pipeline(memory=None,\n",
       "     steps=[('scl', StandardScaler(copy=True, with_mean=True, with_std=True)), ('clf', SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,\n",
       "  decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',\n",
       "  max_iter=-1, probability=False, random_state=1, shrinking=True,\n",
       "  tol=0.001, verbose=False))])"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 建立pipeline\n",
    "pipe_svc = Pipeline([('scl', StandardScaler()), ('clf', SVC(random_state=1))])\n",
    "pipe_svc.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred = pipe_svc.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "confmat = confusion_matrix(y_true=y_test, y_pred=y_pred) # 输出混淆矩阵"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 180x180 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots(figsize=(2.5, 2.5))\n",
    "ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)\n",
    "for i in range(confmat.shape[0]):\n",
    "    for j in range(confmat.shape[1]):\n",
    "        ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')\n",
    "plt.xlabel('predicted label')\n",
    "plt.ylabel('true label')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "precision:0.976\n",
      "recall:0.952\n",
      "F1:0.964\n"
     ]
    }
   ],
   "source": [
    "# 召回率、准确率、F1\n",
    "print('precision:%.3f' % precision_score(y_true=y_test, y_pred=y_pred))\n",
    "print('recall:%.3f' % recall_score(y_true=y_test, y_pred=y_pred))\n",
    "print('F1:%.3f' % f1_score(y_true=y_test, y_pred=y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
