# File content is auto-generated. Do not modify.
# pylint: skip-file
from ._internal import NDArrayBase
from ..base import _Null

def gelqf(A=None, out=None, name=None, **kwargs):
    r"""LQ factorization for general matrix.
    Input is a tensor *A* of dimension *n >= 2*.

    If *n=2*, we compute the LQ factorization (LAPACK *gelqf*, followed by *orglq*). *A*
    must have shape *(x, y)* with *x <= y*, and must have full rank *=x*. The LQ
    factorization consists of *L* with shape *(x, x)* and *Q* with shape *(x, y)*, so
    that:

       *A* = *L* \* *Q*

    Here, *L* is lower triangular (upper triangle equal to zero) with nonzero diagonal,
    and *Q* is row-orthonormal, meaning that

       *Q* \* *Q*\ :sup:`T`

    is equal to the identity matrix of shape *(x, x)*.

    If *n>2*, *gelqf* is performed separately on the trailing two dimensions for all
    inputs (batch mode).

    .. note:: The operator supports float32 and float64 data types only.

    Examples::

       // Single LQ factorization
       A = [[1., 2., 3.], [4., 5., 6.]]
       Q, L = gelqf(A)
       Q = [[-0.26726124, -0.53452248, -0.80178373],
            [0.87287156, 0.21821789, -0.43643578]]
       L = [[-3.74165739, 0.],
            [-8.55235974, 1.96396101]]

       // Batch LQ factorization
       A = [[[1., 2., 3.], [4., 5., 6.]],
            [[7., 8., 9.], [10., 11., 12.]]]
       Q, L = gelqf(A)
       Q = [[[-0.26726124, -0.53452248, -0.80178373],
             [0.87287156, 0.21821789, -0.43643578]],
            [[-0.50257071, -0.57436653, -0.64616234],
             [0.7620735, 0.05862104, -0.64483142]]]
       L = [[[-3.74165739, 0.],
             [-8.55235974, 1.96396101]],
            [[-13.92838828, 0.],
             [-19.09768702, 0.52758934]]]


    Defined in src/operator/tensor/la_op.cc:L569

    Parameters
    ----------
    A : NDArray
        Tensor of input matrices to be factorized

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def gemm(A=None, B=None, C=None, transpose_a=_Null, transpose_b=_Null, alpha=_Null, beta=_Null, axis=_Null, out=None, name=None, **kwargs):
    r"""Performs general matrix multiplication and accumulation.
    Input are tensors *A*, *B*, *C*, each of dimension *n >= 2* and having the same shape
    on the leading *n-2* dimensions.

    If *n=2*, the BLAS3 function *gemm* is performed:

       *out* = *alpha* \* *op*\ (*A*) \* *op*\ (*B*) + *beta* \* *C*

    Here, *alpha* and *beta* are scalar parameters, and *op()* is either the identity or
    matrix transposition (depending on *transpose_a*, *transpose_b*).

    If *n>2*, *gemm* is performed separately for a batch of matrices. The column indices of the matrices
    are given by the last dimensions of the tensors, the row indices by the axis specified with the *axis* 
    parameter. By default, the trailing two dimensions will be used for matrix encoding.

    For a non-default axis parameter, the operation performed is equivalent to a series of swapaxes/gemm/swapaxes
    calls. For example let *A*, *B*, *C* be 5 dimensional tensors. Then gemm(*A*, *B*, *C*, axis=1) is equivalent to

        A1 = swapaxes(A, dim1=1, dim2=3)
        B1 = swapaxes(B, dim1=1, dim2=3)
        C = swapaxes(C, dim1=1, dim2=3)
        C = gemm(A1, B1, C)
        C = swapaxis(C, dim1=1, dim2=3)

    without the overhead of the additional swapaxis operations.

    When the input data is of type float32 and the environment variables MXNET_CUDA_ALLOW_TENSOR_CORE
    and MXNET_CUDA_TENSOR_OP_MATH_ALLOW_CONVERSION are set to 1, this operator will try to use
    pseudo-float16 precision (float32 math with float16 I/O) precision in order to use
    Tensor Cores on suitable NVIDIA GPUs. This can sometimes give significant speedups.

    .. note:: The operator supports float32 and float64 data types only.

    Examples::

       // Single matrix multiply-add
       A = [[1.0, 1.0], [1.0, 1.0]]
       B = [[1.0, 1.0], [1.0, 1.0], [1.0, 1.0]]
       C = [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
       gemm(A, B, C, transpose_b=True, alpha=2.0, beta=10.0)
               = [[14.0, 14.0, 14.0], [14.0, 14.0, 14.0]]

       // Batch matrix multiply-add
       A = [[[1.0, 1.0]], [[0.1, 0.1]]]
       B = [[[1.0, 1.0]], [[0.1, 0.1]]]
       C = [[[10.0]], [[0.01]]]
       gemm(A, B, C, transpose_b=True, alpha=2.0 , beta=10.0)
               = [[[104.0]], [[0.14]]]


    Defined in src/operator/tensor/la_op.cc:L87

    Parameters
    ----------
    A : NDArray
        Tensor of input matrices
    B : NDArray
        Tensor of input matrices
    C : NDArray
        Tensor of input matrices
    transpose_a : boolean, optional, default=0
        Multiply with transposed of first input (A).
    transpose_b : boolean, optional, default=0
        Multiply with transposed of second input (B).
    alpha : double, optional, default=1
        Scalar factor multiplied with A*B.
    beta : double, optional, default=1
        Scalar factor multiplied with C.
    axis : int, optional, default='-2'
        Axis corresponding to the matrix rows.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def gemm2(A=None, B=None, transpose_a=_Null, transpose_b=_Null, alpha=_Null, axis=_Null, out=None, name=None, **kwargs):
    r"""Performs general matrix multiplication.
    Input are tensors *A*, *B*, each of dimension *n >= 2* and having the same shape
    on the leading *n-2* dimensions.

    If *n=2*, the BLAS3 function *gemm* is performed:

       *out* = *alpha* \* *op*\ (*A*) \* *op*\ (*B*)

    Here *alpha* is a scalar parameter and *op()* is either the identity or the matrix
    transposition (depending on *transpose_a*, *transpose_b*).

    If *n>2*, *gemm* is performed separately for a batch of matrices. The column indices of the matrices
    are given by the last dimensions of the tensors, the row indices by the axis specified with the *axis* 
    parameter. By default, the trailing two dimensions will be used for matrix encoding.

    For a non-default axis parameter, the operation performed is equivalent to a series of swapaxes/gemm/swapaxes
    calls. For example let *A*, *B* be 5 dimensional tensors. Then gemm(*A*, *B*, axis=1) is equivalent to

        A1 = swapaxes(A, dim1=1, dim2=3)
        B1 = swapaxes(B, dim1=1, dim2=3)
        C = gemm2(A1, B1)
        C = swapaxis(C, dim1=1, dim2=3)

    without the overhead of the additional swapaxis operations.

    When the input data is of type float32 and the environment variables MXNET_CUDA_ALLOW_TENSOR_CORE
    and MXNET_CUDA_TENSOR_OP_MATH_ALLOW_CONVERSION are set to 1, this operator will try to use
    pseudo-float16 precision (float32 math with float16 I/O) precision in order to use
    Tensor Cores on suitable NVIDIA GPUs. This can sometimes give significant speedups.

    .. note:: The operator supports float32 and float64 data types only.

    Examples::

       // Single matrix multiply
       A = [[1.0, 1.0], [1.0, 1.0]]
       B = [[1.0, 1.0], [1.0, 1.0], [1.0, 1.0]]
       gemm2(A, B, transpose_b=True, alpha=2.0)
                = [[4.0, 4.0, 4.0], [4.0, 4.0, 4.0]]

       // Batch matrix multiply
       A = [[[1.0, 1.0]], [[0.1, 0.1]]]
       B = [[[1.0, 1.0]], [[0.1, 0.1]]]
       gemm2(A, B, transpose_b=True, alpha=2.0)
               = [[[4.0]], [[0.04 ]]]


    Defined in src/operator/tensor/la_op.cc:L162

    Parameters
    ----------
    A : NDArray
        Tensor of input matrices
    B : NDArray
        Tensor of input matrices
    transpose_a : boolean, optional, default=0
        Multiply with transposed of first input (A).
    transpose_b : boolean, optional, default=0
        Multiply with transposed of second input (B).
    alpha : double, optional, default=1
        Scalar factor multiplied with A*B.
    axis : int, optional, default='-2'
        Axis corresponding to the matrix row indices.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def potrf(A=None, out=None, name=None, **kwargs):
    r"""Performs Cholesky factorization of a symmetric positive-definite matrix.
    Input is a tensor *A* of dimension *n >= 2*.

    If *n=2*, the Cholesky factor *B* of the symmetric, positive definite matrix *A* is
    computed. *B* is triangular (entries of upper or lower triangle are all zero), has
    positive diagonal entries, and:

      *A* = *B* \* *B*\ :sup:`T`  if *lower* = *true*
      *A* = *B*\ :sup:`T` \* *B*  if *lower* = *false*

    If *n>2*, *potrf* is performed separately on the trailing two dimensions for all inputs
    (batch mode).

    .. note:: The operator supports float32 and float64 data types only.

    Examples::

       // Single matrix factorization
       A = [[4.0, 1.0], [1.0, 4.25]]
       potrf(A) = [[2.0, 0], [0.5, 2.0]]

       // Batch matrix factorization
       A = [[[4.0, 1.0], [1.0, 4.25]], [[16.0, 4.0], [4.0, 17.0]]]
       potrf(A) = [[[2.0, 0], [0.5, 2.0]], [[4.0, 0], [1.0, 4.0]]]


    Defined in src/operator/tensor/la_op.cc:L213

    Parameters
    ----------
    A : NDArray
        Tensor of input matrices to be decomposed

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def potri(A=None, out=None, name=None, **kwargs):
    r"""Performs matrix inversion from a Cholesky factorization.
    Input is a tensor *A* of dimension *n >= 2*.

    If *n=2*, *A* is a triangular matrix (entries of upper or lower triangle are all zero)
    with positive diagonal. We compute:

      *out* = *A*\ :sup:`-T` \* *A*\ :sup:`-1` if *lower* = *true*
      *out* = *A*\ :sup:`-1` \* *A*\ :sup:`-T` if *lower* = *false*

    In other words, if *A* is the Cholesky factor of a symmetric positive definite matrix
    *B* (obtained by *potrf*), then

      *out* = *B*\ :sup:`-1`

    If *n>2*, *potri* is performed separately on the trailing two dimensions for all inputs
    (batch mode).

    .. note:: The operator supports float32 and float64 data types only.

    .. note:: Use this operator only if you are certain you need the inverse of *B*, and
              cannot use the Cholesky factor *A* (*potrf*), together with backsubstitution
              (*trsm*). The latter is numerically much safer, and also cheaper.

    Examples::

       // Single matrix inverse
       A = [[2.0, 0], [0.5, 2.0]]
       potri(A) = [[0.26563, -0.0625], [-0.0625, 0.25]]

       // Batch matrix inverse
       A = [[[2.0, 0], [0.5, 2.0]], [[4.0, 0], [1.0, 4.0]]]
       potri(A) = [[[0.26563, -0.0625], [-0.0625, 0.25]],
                   [[0.06641, -0.01562], [-0.01562, 0,0625]]]


    Defined in src/operator/tensor/la_op.cc:L274

    Parameters
    ----------
    A : NDArray
        Tensor of lower triangular matrices

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def sumlogdiag(A=None, out=None, name=None, **kwargs):
    r"""Computes the sum of the logarithms of the diagonal elements of a square matrix.
    Input is a tensor *A* of dimension *n >= 2*.

    If *n=2*, *A* must be square with positive diagonal entries. We sum the natural
    logarithms of the diagonal elements, the result has shape (1,).

    If *n>2*, *sumlogdiag* is performed separately on the trailing two dimensions for all
    inputs (batch mode).

    .. note:: The operator supports float32 and float64 data types only.

    Examples::

       // Single matrix reduction
       A = [[1.0, 1.0], [1.0, 7.0]]
       sumlogdiag(A) = [1.9459]

       // Batch matrix reduction
       A = [[[1.0, 1.0], [1.0, 7.0]], [[3.0, 0], [0, 17.0]]]
       sumlogdiag(A) = [1.9459, 3.9318]


    Defined in src/operator/tensor/la_op.cc:L445

    Parameters
    ----------
    A : NDArray
        Tensor of square matrices

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def syevd(A=None, out=None, name=None, **kwargs):
    r"""Eigendecomposition for symmetric matrix.
    Input is a tensor *A* of dimension *n >= 2*.

    If *n=2*, *A* must be symmetric, of shape *(x, x)*. We compute the eigendecomposition,
    resulting in the orthonormal matrix *U* of eigenvectors, shape *(x, x)*, and the
    vector *L* of eigenvalues, shape *(x,)*, so that:

       *U* \* *A* = *diag(L)* \* *U*

    Here:

       *U* \* *U*\ :sup:`T` = *U*\ :sup:`T` \* *U* = *I*

    where *I* is the identity matrix. Also, *L(0) <= L(1) <= L(2) <= ...* (ascending order).

    If *n>2*, *syevd* is performed separately on the trailing two dimensions of *A* (batch
    mode). In this case, *U* has *n* dimensions like *A*, and *L* has *n-1* dimensions.

    .. note:: The operator supports float32 and float64 data types only.

    .. note:: Derivatives for this operator are defined only if *A* is such that all its
              eigenvalues are distinct, and the eigengaps are not too small. If you need
              gradients, do not apply this operator to matrices with multiple eigenvalues.

    Examples::

       // Single symmetric eigendecomposition
       A = [[1., 2.], [2., 4.]]
       U, L = syevd(A)
       U = [[0.89442719, -0.4472136],
            [0.4472136, 0.89442719]]
       L = [0., 5.]

       // Batch symmetric eigendecomposition
       A = [[[1., 2.], [2., 4.]],
            [[1., 2.], [2., 5.]]]
       U, L = syevd(A)
       U = [[[0.89442719, -0.4472136],
             [0.4472136, 0.89442719]],
            [[0.92387953, -0.38268343],
             [0.38268343, 0.92387953]]]
       L = [[0., 5.],
            [0.17157288, 5.82842712]]


    Defined in src/operator/tensor/la_op.cc:L638

    Parameters
    ----------
    A : NDArray
        Tensor of input matrices to be factorized

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def syrk(A=None, transpose=_Null, alpha=_Null, out=None, name=None, **kwargs):
    r"""Multiplication of matrix with its transpose.
    Input is a tensor *A* of dimension *n >= 2*.

    If *n=2*, the operator performs the BLAS3 function *syrk*:

      *out* = *alpha* \* *A* \* *A*\ :sup:`T`

    if *transpose=False*, or

      *out* = *alpha* \* *A*\ :sup:`T` \ \* *A*

    if *transpose=True*.

    If *n>2*, *syrk* is performed separately on the trailing two dimensions for all
    inputs (batch mode).

    .. note:: The operator supports float32 and float64 data types only.

    Examples::

       // Single matrix multiply
       A = [[1., 2., 3.], [4., 5., 6.]]
       syrk(A, alpha=1., transpose=False)
                = [[14., 32.],
                   [32., 77.]]
       syrk(A, alpha=1., transpose=True)
                = [[17., 22., 27.],
                   [22., 29., 36.],
                   [27., 36., 45.]]

       // Batch matrix multiply
       A = [[[1., 1.]], [[0.1, 0.1]]]
       syrk(A, alpha=2., transpose=False) = [[[4.]], [[0.04]]]


    Defined in src/operator/tensor/la_op.cc:L501

    Parameters
    ----------
    A : NDArray
        Tensor of input matrices
    transpose : boolean, optional, default=0
        Use transpose of input matrix.
    alpha : double, optional, default=1
        Scalar factor to be applied to the result.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def trmm(A=None, B=None, transpose=_Null, rightside=_Null, lower=_Null, alpha=_Null, out=None, name=None, **kwargs):
    r"""Performs multiplication with a lower triangular matrix.
    Input are tensors *A*, *B*, each of dimension *n >= 2* and having the same shape
    on the leading *n-2* dimensions.

    If *n=2*, *A* must be triangular. The operator performs the BLAS3 function
    *trmm*:

       *out* = *alpha* \* *op*\ (*A*) \* *B*

    if *rightside=False*, or

       *out* = *alpha* \* *B* \* *op*\ (*A*)

    if *rightside=True*. Here, *alpha* is a scalar parameter, and *op()* is either the
    identity or the matrix transposition (depending on *transpose*).

    If *n>2*, *trmm* is performed separately on the trailing two dimensions for all inputs
    (batch mode).

    .. note:: The operator supports float32 and float64 data types only.


    Examples::

       // Single triangular matrix multiply
       A = [[1.0, 0], [1.0, 1.0]]
       B = [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
       trmm(A, B, alpha=2.0) = [[2.0, 2.0, 2.0], [4.0, 4.0, 4.0]]

       // Batch triangular matrix multiply
       A = [[[1.0, 0], [1.0, 1.0]], [[1.0, 0], [1.0, 1.0]]]
       B = [[[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]], [[0.5, 0.5, 0.5], [0.5, 0.5, 0.5]]]
       trmm(A, B, alpha=2.0) = [[[2.0, 2.0, 2.0], [4.0, 4.0, 4.0]],
                                [[1.0, 1.0, 1.0], [2.0, 2.0, 2.0]]]


    Defined in src/operator/tensor/la_op.cc:L333

    Parameters
    ----------
    A : NDArray
        Tensor of lower triangular matrices
    B : NDArray
        Tensor of matrices
    transpose : boolean, optional, default=0
        Use transposed of the triangular matrix
    rightside : boolean, optional, default=0
        Multiply triangular matrix from the right to non-triangular one.
    lower : boolean, optional, default=1
        True if the triangular matrix is lower triangular, false if it is upper triangular.
    alpha : double, optional, default=1
        Scalar factor to be applied to the result.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def trsm(A=None, B=None, transpose=_Null, rightside=_Null, lower=_Null, alpha=_Null, out=None, name=None, **kwargs):
    r"""Solves matrix equation involving a lower triangular matrix.
    Input are tensors *A*, *B*, each of dimension *n >= 2* and having the same shape
    on the leading *n-2* dimensions.

    If *n=2*, *A* must be triangular. The operator performs the BLAS3 function
    *trsm*, solving for *out* in:

       *op*\ (*A*) \* *out* = *alpha* \* *B*

    if *rightside=False*, or

       *out* \* *op*\ (*A*) = *alpha* \* *B*

    if *rightside=True*. Here, *alpha* is a scalar parameter, and *op()* is either the
    identity or the matrix transposition (depending on *transpose*).

    If *n>2*, *trsm* is performed separately on the trailing two dimensions for all inputs
    (batch mode).

    .. note:: The operator supports float32 and float64 data types only.

    Examples::

       // Single matrix solve
       A = [[1.0, 0], [1.0, 1.0]]
       B = [[2.0, 2.0, 2.0], [4.0, 4.0, 4.0]]
       trsm(A, B, alpha=0.5) = [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

       // Batch matrix solve
       A = [[[1.0, 0], [1.0, 1.0]], [[1.0, 0], [1.0, 1.0]]]
       B = [[[2.0, 2.0, 2.0], [4.0, 4.0, 4.0]],
            [[4.0, 4.0, 4.0], [8.0, 8.0, 8.0]]]
       trsm(A, B, alpha=0.5) = [[[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]],
                                [[2.0, 2.0, 2.0], [2.0, 2.0, 2.0]]]


    Defined in src/operator/tensor/la_op.cc:L396

    Parameters
    ----------
    A : NDArray
        Tensor of lower triangular matrices
    B : NDArray
        Tensor of matrices
    transpose : boolean, optional, default=0
        Use transposed of the triangular matrix
    rightside : boolean, optional, default=0
        Multiply triangular matrix from the right to non-triangular one.
    lower : boolean, optional, default=1
        True if the triangular matrix is lower triangular, false if it is upper triangular.
    alpha : double, optional, default=1
        Scalar factor to be applied to the result.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

__all__ = ['gelqf', 'gemm', 'gemm2', 'potrf', 'potri', 'sumlogdiag', 'syevd', 'syrk', 'trmm', 'trsm']