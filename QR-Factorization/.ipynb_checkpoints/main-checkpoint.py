import scipy.io as sio
import numpy as np
from _cffi_backend import callback
from numpy.testing import assert_equal

np.set_printoptions(precision=4)


def qrstep(A):
    Q, R = np.linalg.qr(A)
    An = np.matmul(R, Q)
    A = An
    return A


def factorization(A, eps, iter_num = 10):
    def sum_sq():
        loss = 0.0
        for x in diagonals(A):
            loss += x * x
        return loss
    ei_sum_0 = sum_sq()

    for it in range(100):
        qrstep(A)
        ei_sum_1 = sum_sq()
        error = ei_sum_1 - ei_sum_0
        ei_sum_0 = ei_sum_1


def householder_reflection(A):

    (num_rows, num_cols) = np.shape(A)

    Q = np.identity(num_rows)
    R = np.copy(A)

    for cnt in range(num_rows - 1):
        x = R[cnt:, cnt]

        e = np.zeros_like(x)
        e[0] = np.copysign(np.linalg.norm(x), -A[cnt, cnt])
        u = x + e
        v = u / np.linalg.norm(u)

        Q_cnt = np.identity(num_rows)
        Q_cnt[cnt:, cnt:] -= 2.0 * np.outer(v, v)

        R = np.dot(Q_cnt, R)
        Q = np.dot(Q, Q_cnt.T)

        E = np.diag(np.dot(R, Q), -1)
        E = np.reshape(E, (9, ))
        e = E.max()

    return Q, R, e


def diagonals(A):
    eis = []
    for idx in range(0, A.shape[0]):
        eis.append(A[idx, idx])
    return eis


data = sio.loadmat("matrix.mat")
mtx = data['A']
N = 0
while True:
    Q, R, err = householder_reflection(mtx)
    mtx = np.matmul(R, Q)
    N = N+1
    if err<1e-8: break


print(err, N)
print(mtx)














