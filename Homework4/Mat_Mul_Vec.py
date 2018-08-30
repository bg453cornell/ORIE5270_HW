import sys



def Mat_Mul_Vec(Mat, Vec):

    from pyspark import SparkContext

    sc = SparkContext('local[2]', 'hw4_exercise')

    A = sc.textFile(Mat)
    v = sc.textFile(Vec)

    A = A.map(lambda l: (l.split(',')))
    A = A.map(lambda l: (int(l[0]), tuple(map(float, l[1:]))))

    def add_col_index(l):
        for idx, val in enumerate(l):
            yield (idx, val)

    A = A.map(lambda l: (l[0], tuple(enumerate(l[1]))))

    v = v.map(lambda l: tuple(map(float, l.split(','))))
    v = v.map(lambda l: tuple(enumerate(l)))
    v = v.flatMap(lambda l: l)

    def combine(idx, t):
        for tup in t:
            yield (idx, tup)

    flat_A = A.flatMap(lambda l: tuple(combine(l[0], l[1])))
    flat_A = flat_A.map(lambda l: tuple((l[1][0], (l[0], l[1][1]))))

    joined = flat_A.join(v)

    joined_ = joined.map(lambda l: (l[0], (l[1][0][0], l[1][0][1]*l[1][1])))

    joined_ = joined_.map(lambda l: (l[1][0], l[1][1]))

    sum_ = joined_.reduceByKey(lambda n1, n2: n1+n2)

    output = sum_.map(lambda l: l[1])

    print(output.collect())

    return output


if __name__ == "__main__":
    Mat_Mul_Vec(sys.argv[1], sys.argv[2])
