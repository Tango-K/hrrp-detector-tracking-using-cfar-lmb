import numpy as np

def cfarOS(img,N,pro_n,k,pad):
    alpha = N*(pad^(-1*N)-1)
    index = [1+N/2 + pro_n/2 : len(xc)-N/2-pro_n/2]

    xt = np.zeros(len(index))

    for i in index:
        cell_left = img[1,i-N/2-pro_n/2:i-pro_n/2-1]
        cell_right = img[1,i+pro_n/2+1:i+N/2+pro_n/2]

        cell_all = np.hstack([cell_left,cell_right])
        cell_sort = np.sort(cell_all)

        z = cell_sort[1,k]

        xt[1,i-N/2-pro_n/2] = np.dot(z,alpha)

    return xt

if __name__ == "__main__":
    N = 36
    pro_n = 2
    k = 2*N/4
    pad = 1e-3

    index,xt = cfarOS(N,pro_n,k,pad)