class QueryObject:
    def __init__(self, name=None, left=None, right=None):
        if not left:
            self.type = "obj"
            self.name = name
        else:
            self.type = "tree"
            self.name = name
            self.left = left
            self.right = right

    def __lt__(self, other):
        return QueryObject("<", self, other)

    def __gt__(self, other):
        return QueryObject(">", self, other)

    def __le__(self, other):
        return QueryObject("<=", self, other)

    def __ge__(self, other):
        return QueryObject(">=", self, other)

    def __eq__(self, other):
        return QueryObject("==", self, other)

    def __ne__(self, other):
        return QueryObject("!=", self, other)

    def __repr__(self):
        if self.type == "obj":
            return self.name
        else:
            return "({} {} {})".format(self.left, self.name, self.right)

    def eval(self, data):
        def eval_impl(obj, data_):
            if isinstance(obj, QueryObject):
                if obj.type == "obj":
                    return data_[obj.name]
                else:
                    return {
                        "and": lambda a, b: a and b,
                        "or": lambda a, b: a or b,
                        "<": lambda a, b: a < b,
                        ">": lambda a, b: a > b,
                        "<=": lambda a, b: a <= b,
                        ">=": lambda a, b: a >= b,
                        "==": lambda a, b: a == b,
                        "!=": lambda a, b: a != b
                    }[obj.name](eval_impl(obj.left, data_), eval_impl(obj.right, data_))
            else:
                return obj
        return eval_impl(self, data)


def generate_query(str):
    def AND(*args):
        if len(args) <= 2:
            return QueryObject("and", args[0], args[1])
        else:
            return QueryObject("and", AND(*args[:-1]), args[-1])

    def OR(*args):
        if len(args) <= 2:
            return QueryObject("or", args[0], args[1])
        else:
            return QueryObject("or", OR(*args[:-1]), args[-1])

    courseID = QueryObject(name="courseID")
    grade = QueryObject(name="grade")
    point = QueryObject(name="point")
    credit = QueryObject(name="credit")
    schoolYear = QueryObject(name="schoolYear")
    completionDate = QueryObject(name="completionDate")
    courseName = QueryObject(name="courseName")

    return eval(str)
