(defun getInputAsIntegers ()
  (mapcar (function parse-integer) (getInput)))

(defun getInput ()
  (loop for line = (read-line *standard-input* nil :eof)
     until (eq line :eof)
     collect line))

(defun cyclifyList (l) "turns a list into a cyclic list"
  (setf (cdr (last l)) l))

(defun addUntilRepetition (numbers sum sums)
  (if (member sum sums)
      sum
      (addUntilRepetition (cdr numbers) (+ sum (car numbers)) (cons sum sums))))

(write (addUntilRepetition (cyclifyList (getInputAsIntegers)) 0 ()))
