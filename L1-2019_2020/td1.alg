IMPORTED FROM LAST YEAR:

function: empty(val[], next[]: Array, bv, be, length: integer)
copied parameter: length
changed parameter: bv, be, val, next
local variable: x: integer

begin
    be <- 1
    bv <- 0
    for i<-1 to length do:
        next[i] <- i+1
    end for
    next[length] <- 0
end


CETTE ANNÉE, LE COURS EST EN FRANÇAIS, ATTENTION AU NOUVEAU MÉTALANGAGE.

CHABCHOUB Kamel - chabchoub.efrei@gmail.com

Matrix

begin
if (mat1 == nil or mat2 == nil)
    matf = (mat1 ? mat2 : mat2 = nil)
else if (dim(mat1) != dim(mat2))
    print("Error on the matrix dimensions")
else
    matf = add_op(mat1, mat2)
end



ATTENTION, VOICI LE NOUVEAU MÉTALANGAGE

Algorithme RechercheMin(tab: tableau 1D d'entiers): entier
    Début
        min: entier, valeur minimale du tableau
        i: entier, compteur
        min = tab[0]
        Pour i allant de 1 jusqu'à taille(tab)-1 faire
            Si tab[i] < min
                min = tab[i]
            Fin si
        Fin pour
        Retourner min
    Fin




DERNIER TD
EXO1

fonction sommeM(mat1, mat2: matrices): matrice
variable locale : mat3[100][100]: matrice
    Début
        Si taille(mat1) != taille(mat2):
            retourner (-1) // ou mat1
        Sinon si mat1 = ø ou mat2 = ø:
            retourner (-1) // ou mat1
        Sinon si taille(mat1[0]) != (mat2[0]):
            retourner (-1) // ou mat1
        Sinon:
            Pour i allant de 0 à taille(mat1) faire:
                pour s allant de 0 à taille(mat1[0]) faire:
                    mat3[i][s] <- mat2[i][s] + mat1[i][s]
            retourner mat3

EXO2

fonction prodM(mat1, mat2: matrices): matrice
variable locale : mat3[100][100]: matrice
    Début
        Si taille(mat1) != taille(mat2):
            retourner (-1) // ou mat1
        Sinon si mat1 = ø ou mat2 = ø:
            retourner (-1) // ou mat1
        Sinon si taille(mat1[0]) != (mat2[0]):
            retourner (-1) // ou mat1
        Sinon:
            Pour i allant de 0 à taille(mat1) faire:
                pour s allant de 0 à taille(mat1[0]) faire:
                    mat3[i][s] <- mat2[i][s] * mat1[i][s]
            retourner mat3


EXO 3

fonction RIM()
