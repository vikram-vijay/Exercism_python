class Garden:
    default_students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph',
                        'Kincaid', 'Larry']
    plant = {"V": "Violets", "C": "Clover", "R": "Radishes", "G": "Grass"}
    # m = no_of_plants_per_student_per_row
    m = 2

    def __init__(self, diagram,
                 students=default_students):
        self.students = sorted(students)
        self.diagram = diagram

    def plants(self, name):
        n = self.m * self.students.index(name)
        return [self.plant[j[i]] for j in self.diagram.split() for i in range(n, n + self.m)]
