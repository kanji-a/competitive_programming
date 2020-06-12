(define seed (read))
(define x 123456789)
(define y 362436069)
(define z 521288629)
(define w seed)
(define t 0)

(define point (make-vector 5))
(vector-map! (make-vector 2) point)

(let loop-i ((i 0))
  (if (< i 5)
    (let loop-j ((j 0))
      (if (< j 2)
        (begin
          (set! t (logxor #?=x (ash x 11)))
          (set! x y)
          (set! y z)
          (set! z w)
          (set! w (logxor (logxor w (ash w -19)) (logxor t (ash t -8))))
          (let ((v (- (modulo w 100000) 50000)))
            (begin
              (if (>= v 0) (set! v (+ v 1)))
              (vector-set! (vector-ref point i) j v)))
          (loop-j (+ j 1)))))
    (loop-i (+ i 1))))

(print point)
    
