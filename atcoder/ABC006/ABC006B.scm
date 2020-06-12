(define n (read))

(define (trib a b c cnt)
  (if (= cnt n) a
    (trib b c (modulo (+ a b c) 10007) (+ cnt 1))))

(begin (display (trib 0 0 1 1)) (display "\n"))
