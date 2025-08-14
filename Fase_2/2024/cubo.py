N = int(input())
numCubos = N * N * N

cubosZeroFaces = 0
cubosUmaFace = 0
cubosDuasFaces = 0

cubosTresFaces = 8
numCubos -= 8

if numCubos > 0:
    cubosDuasFaces = (N - 2) * 12
    numCubos -= cubosDuasFaces
if numCubos > 0:
    cubosUmaFace = (N - 2) * (N - 2) * 6
    numCubos -= cubosUmaFace
if numCubos > 0:
    cubosZeroFaces = numCubos

print(cubosZeroFaces)
print(cubosUmaFace)
print(cubosDuasFaces)
print(cubosTresFaces)
