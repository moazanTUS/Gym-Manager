from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gym_gui import Ui_MainWindow
from PyQt5.QtCore import Qt
from typing import Dict

class Exercise:
    def __init__(self, weight, reps):
        self.weight = weight
        self.reps = reps

    def calculate_one_rep_max(self):
        pass

class Squat(Exercise):
    def calculate_one_rep_max(self):
        return round(self.weight * (1 + self.reps / 30))

class Bench(Exercise):
    def calculate_one_rep_max(self):
        return round(self.weight * (1 + self.reps / 30))

class Deadlift(Exercise):
    def calculate_one_rep_max(self):
        return round(self.weight * (1 + self.reps / 31))

class Athlete:
    def __init__(self, name, squat=None, bench=None, deadlift=None, units='LBS', is_powerlifter=False):
        self.name = name
        self.squat = squat
        self.bench = bench
        self.deadlift = deadlift
        self.units = units
        self.is_powerlifter = is_powerlifter

    def add_exercises(self, squat, bench, deadlift):
        self.squat = squat
        self.bench = bench
        self.deadlift = deadlift

    def total(self):
        return sum([self.squat.calculate_one_rep_max(), self.bench.calculate_one_rep_max(), self.deadlift.calculate_one_rep_max()])

class GymManagerApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(GymManagerApp, self).__init__()
        self.setupUi(self)
        self.athletes = []
        self.current_index = -1
        self.populate_fields()

        self.nextbutton.clicked.connect(self.next_athlete)
        self.previousbutton.clicked.connect(self.previous_athlete)
        self.cleardatbtn.clicked.connect(self.clear_data)
        self.insertAthletebtn.clicked.connect(self.insert_athlete)
        self.calctotalbtn.clicked.connect(self.calculate_total)
        self.incSquatbtn.clicked.connect(self.increment_squat)
        self.incbenchbtn.clicked.connect(self.increment_bench)
        self.incdeadliftbtn.clicked.connect(self.increment_deadlift)

    def populate_fields(self):
        if self.current_index >= 0 and self.current_index < len(self.athletes):
            athlete = self.athletes[self.current_index]
            self.lineEditName.setText(athlete.name)
            self.squatweightlineedit.setText(str(athlete.squat.weight))
            self.benchweightlineedit.setText(str(athlete.bench.weight))
            self.deadliftweightlineedit.setText(str(athlete.deadlift.weight))
            self.lineEditTotal.setText(str(athlete.total()))
            index = self.comboBoxunit.findText(athlete.units, Qt.MatchFixedString)
            if index >= 0:
                self.comboBoxunit.setCurrentIndex(index)
            self.checkBoxisapowerlifter.setChecked(athlete.is_powerlifter)
            self.lineEditsquatreps.setText(str(athlete.squat.reps))
            self.lineEditbenchreps.setText(str(athlete.bench.reps))
            self.lineEditdeadliftreps.setText(str(athlete.deadlift.reps))
            self.calculate_one_rep_maxes()

    def next_athlete(self):
        self.current_index += 1
        if self.current_index >= len(self.athletes):
            self.current_index = len(self.athletes) - 1
        self.populate_fields()

    def previous_athlete(self):
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = 0
        self.populate_fields()

    def clear_data(self):
        self.lineEditName.setText("")
        self.squatweightlineedit.setText("")
        self.benchweightlineedit.setText("")
        self.deadliftweightlineedit.setText("")
        self.lineEditTotal.setText("")
        self.comboBoxunit.setCurrentIndex(0)
        self.checkBoxisapowerlifter.setChecked(False)
        self.lineEditsquatreps.setText("")
        self.lineEditbenchreps.setText("")
        self.lineEditdeadliftreps.setText("")
        self.lineEditSquatORM.setText("")
        self.lineEditBenchOrm.setText("")
        self.lineEditDeadliftORM.setText("")

    def insert_athlete(self):
        name = self.lineEditName.text()
        squat_weight = int(self.squatweightlineedit.text())
        bench_weight = int(self.benchweightlineedit.text())
        deadlift_weight = int(self.deadliftweightlineedit.text())
        squat_reps = int(self.lineEditsquatreps.text())
        bench_reps = int(self.lineEditbenchreps.text())
        deadlift_reps = int(self.lineEditdeadliftreps.text())
        squat = Squat(squat_weight, squat_reps)
        bench = Bench(bench_weight, bench_reps)
        deadlift = Deadlift(deadlift_weight, deadlift_reps)
        units = self.comboBoxunit.currentText()
        is_powerlifter = self.checkBoxisapowerlifter.isChecked()
        athlete = Athlete(name, squat, bench, deadlift, units, is_powerlifter)
        self.athletes.append(athlete)
        self.current_index = len(self.athletes) - 1
        self.populate_fields()
        if is_powerlifter:
            self.calculate_one_rep_maxes()
        else:
            self.lineEditSquatORM.setText("")
            self.lineEditBenchOrm.setText("")
            self.lineEditDeadliftORM.setText("")

        self.calculate_total()


    def calculate_total(self):
        try:
            squat_weight = int(self.squatweightlineedit.text())
            squat_reps = int(self.lineEditsquatreps.text())
            bench_weight = int(self.benchweightlineedit.text())
            bench_reps = int(self.lineEditbenchreps.text())
            deadlift_weight = int(self.deadliftweightlineedit.text())
            deadlift_reps = int(self.lineEditdeadliftreps.text())

            total_weight = (squat_weight * squat_reps) + (bench_weight * bench_reps) + (deadlift_weight * deadlift_reps)
            self.lineEditTotal.setText(str(total_weight))
        except ValueError:
            self.lineEditTotal.setText("invalid input")



    def calculate_one_rep_maxes(self):
        if self.current_index >= 0 and self.current_index < len(self.athletes):
            athlete = self.athletes[self.current_index]
            squat_orm = athlete.squat.calculate_one_rep_max()
            bench_orm = athlete.bench.calculate_one_rep_max()
            deadlift_orm = athlete.deadlift.calculate_one_rep_max()
            self.lineEditSquatORM.setText(str(squat_orm))
            self.lineEditBenchOrm.setText(str(bench_orm))
            self.lineEditDeadliftORM.setText(str(deadlift_orm))

    def increment_squat(self):
        squat_weight = int(self.squatweightlineedit.text())
        self.squatweightlineedit.setText(str(squat_weight + 5))
        self.calculate_one_rep_maxes()

    def increment_bench(self):
        bench_weight = int(self.benchweightlineedit.text())
        self.benchweightlineedit.setText(str(bench_weight + 5))
        self.calculate_one_rep_maxes()

    def increment_deadlift(self):
        deadlift_weight = int(self.deadliftweightlineedit.text())
        self.deadliftweightlineedit.setText(str(deadlift_weight + 5))
        self.calculate_one_rep_maxes()

def main():
    app = QApplication(sys.argv)
    window = GymManagerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
