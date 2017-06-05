bw = imread('unpleasant100.png');
bw = rgb2gray(bw);

bw2 = imcomplement(bw);
subplot(1,2,1),imshow(bw)
subplot(1,2,2),imshow(bw2)

imwrite(bw2,'neg_unpleasant100.png')