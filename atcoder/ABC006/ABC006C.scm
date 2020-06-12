; 入力の受付
(define N (read))
(define M (read))

(define (solve infant)
  (if (< infant 0) '(-1 -1 -1)
    (let ((old (- (- M (* 2 N)) (* 2 infant)))
      (adult (+ (- (* 3 N) M) infant)))
      (if (and (>= adult 0) (>= old 0))
        (list adult old infant) 
        (solve (- infant 1))))))

; 表示用関数
(define (display-list ls)
  (if (not (null? ls))
    (begin (display (car ls))
      (if (null? (cdr ls))
        (display "\n") (display " "))
      (display-list (cdr ls)))))

(display-list (solve N))
