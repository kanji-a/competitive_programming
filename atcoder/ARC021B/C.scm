; 入力
(define K (read))
(define N (read))
(define AD (let loop ((n N))
  (if (zero? n) '()
    (cons (cons (read) (read)) (loop (- n 1))))))

; 建築限度額
(define L (fold max 0
    (map (^ (x) (+ (car x) (* K (cdr x)))) AD)))

; 増築回数がK以下になるような最大の増築限度額を求める
(define (ub n l u)
  (if (= (- u l) 1) (- u 1)
    (let ((m (quotient (+ l u) 2)))
      (if (<= (L2total-times m) n)
        (ub n m u)
        (ub n l m)))))

; 増築限度額Lから合計増築回数を求める
(define (L2times L A D)
  (if (>= (- L A) 0) (+ (quotient (- L A) D) 1) 0))

; 増築限度額Lから合計増築回数を求める
(define (L2total-times L)
  (fold + 0 (map (^ (x) (L2times L (car x) (cdr x))) AD)))

; 増築限度額Lから合計増築費用を求める
(define (L2ans L)
  (+ (fold + 0
    (map (^ (x) (sum-of-aseq (car x) (cdr x)
                 (L2times L (car x) (cdr x)))) AD))
    (* (+ L 1) (max (- K (L2total-times L)) 0))))

; 等差数列の和
(define (sum-of-aseq a d n)
  (* (+ a (/ (* (- n 1) d) 2)) n))

(print (L2ans (ub K -1 (+ L 1))))
