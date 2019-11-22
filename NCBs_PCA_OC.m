A = csvread('fullDataset_051819_CGDRJ.csv');
[coeff,score,latent,tsquared,explained,mu] = pca(A);