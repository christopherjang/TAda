class Course:
    def __init__(self, name):
        self.name = name
        self.positions = []


class Position:
    def __init__(self, name, weighting):
        self.name = name
        self.weighting = weighting


class CourseDirector:
    def __init__(self, name):
        self.name = name
        self.requests = []
        self.avoid = []


class GradStudent:
    def __init__(self, name):
        self.name = name
        self.requests = []
        self.avoid = []
        self.experience = []