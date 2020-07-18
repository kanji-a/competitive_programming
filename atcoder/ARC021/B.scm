(use gauche.collection)

; 入力の読込
(define L (read))
(define B (let loop ((l L))
  (if (zero? l)
    '() (cons (read) (loop (- l 1))))))

; 答えを表示
(define (print-ans An B)
  (if (< An 0) (print An)
    (if (not (null? B))
      (begin (print An)
        (print-ans (logxor An (car B)) (cdr B))))))

; 解く
(if (zero? (fold logxor 0 B))
  (print-ans 0 B) (print -1))
