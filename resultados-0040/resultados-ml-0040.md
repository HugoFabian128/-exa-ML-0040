# Reporte de Análisis de Datos - Pandas

`Hugo Fabian Machine Learning pandas, NC 0040`

## 1. DataFrame Convertido
```text
  Instrumento  Cuerdas_teclas  Precio
0    Guitarra               6    3500
1       Piano              88   15000
2      Violín               4    8000
3     Batería               0   12000
4      Flauta               0    1200
5    Trompeta               0    5500
```

## 2.1 Primeras Filas (head)
```text
  Instrumento  Cuerdas_teclas  Precio
0    Guitarra               6    3500
1       Piano              88   15000
```

## 2.2 Últimas Filas (tail)
```text
  Instrumento  Cuerdas_teclas  Precio
4      Flauta               0    1200
5    Trompeta               0    5500
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Instrumento         str
Cuerdas_teclas    int64
Precio            int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   Instrumento     6 non-null      str  
 1   Cuerdas_teclas  6 non-null      int64
 2   Precio          6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Precio'
```text
count        6.000000
mean      7533.333333
std       5223.664104
min       1200.000000
25%       4000.000000
50%       6750.000000
75%      11000.000000
max      15000.000000
Name: Precio, dtype: float64
```

## 4. Ordenar Ascendente por Precio
```text
  Instrumento  Cuerdas_teclas  Precio
4      Flauta               0    1200
0    Guitarra               6    3500
5    Trompeta               0    5500
2      Violín               4    8000
3     Batería               0   12000
1       Piano              88   15000
```

## 5. Ordenar Descendente por Cuerdas_teclas
```text
  Instrumento  Cuerdas_teclas  Precio
1       Piano              88   15000
0    Guitarra               6    3500
2      Violín               4    8000
3     Batería               0   12000
4      Flauta               0    1200
5    Trompeta               0    5500
```

`Hugo Fabian Machine Learning pandas, NC 0040`