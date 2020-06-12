; 入力の受付
(define N (read))
(define deck (let loop ((n N))
  (if (zero? n)
    '() (cons (read) (loop (- n 1))))))

; LISの長さごとの末尾nのDP表を更新
(define (lis-len ls dp)
  (if (null? ls) dp
    (begin (update-dp dp (car ls))
      (lis-len (cdr ls) dp))))

; nを読んでDP表を更新
(define (update-dp dp n)
  (vector-set! dp (vector-lower-bound dp n -1 (- N 1)) n))

; 下界のインデックスを二分探索
(define (vector-lower-bound vec n l u)
  (if (= (- u l) 1) u
    (let ((m (quotient (+ l u) 2)))
      (if (>= (vector-ref vec m) n)
        (vector-lower-bound vec n l m)
        (vector-lower-bound vec n m u)))))

; DP用の∞で初期化されたベクタを用意
(define dp (make-vector N +inf.0))

(print (- N (vector-lower-bound (lis-len deck dp) +inf.0 -1 N)))
