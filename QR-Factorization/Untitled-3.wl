(* ::Package:: *)

(* ::VerificationTest:: *)
(*	*)


(* ::Input:: *)
(*h=q-2*w*)
(*h=MatrixFunction[f,h]*)
(*h^-1=Inverse[h]*)
(*EVs=DiagonalMatrix[EVs]*)
(*Subscript[E, vs]=h.EVs.h^-1*)
(*Export["/Users/glebsokolov/lab_4/matrix1.mat",Subscript[E,vs]=h.EVs.h^-1]*)
(*Cds=Sort[SingularValueList[Subscript[E,vs]]]*)
(*Cds[[10]]/Cds[[1]]*)
(*E0 = SingularValueDecomposition[EVs]*)
(**)
(**)


Subscript[E, vs] = RandomReal[10,{3,3}]
E1 = QRDecomposition[Subscript[E, vs]]
E1 = QRDecomposition[Subscript[E, vs]]


En = E1n[[2]] . E1n[[1]]
En1 = QRDecomposition[En + 1]





w=RandomInteger[{-10,10},{10,10}]]
w[[8;;9,1;;3]]=x; w
MatrixForm[%]
SingularValueList[w.Inverse[w]]



s = SparseArray[{Band[{4,2}]->x,Band[{1,3}]->y},{10,10}
s1 = Inverse[s]
s.s1





EVs=RandomReal[RandomReal[5]]+RandomReal[{-3^1,3^1}, 10]
q=IdentityMatrix[{10,10}]
EVm = Max[EVs]
EVm = 0.1
EVs[[1]]=EVm
