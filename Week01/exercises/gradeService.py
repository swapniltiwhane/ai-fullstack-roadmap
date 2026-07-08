class GradeService:
    def __init__(self):
        self.rule = [
            {"min": 80, "max": 100, "grade": "A"},
            {"min": 70, "max": 79, "grade": "B"},
            {"min": 60, "max": 69, "grade": "C"},
            {"min": 50, "max": 59, "grade": "D"},
        ]

    def getGrade(self, grade: int) -> str:
        for item in self.rule:
            if item["min"] <= grade <= item["max"]:
                return item["grade"]
        return "YOU ARE FAIL"

    def get_grade(self, grade: int) -> str:
        return self.getGrade(grade)


if __name__ == "__main__":
    grade_service = GradeService()
    marks = int(input("Enter your marks: "))
    print(grade_service.getGrade(marks))
