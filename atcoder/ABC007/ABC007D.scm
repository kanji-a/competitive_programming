; 0からNまでで4と9を含まない数の個数
; l:Nをリストにしたもの d:Nの桁数
(define wo49
  (lambda (l d)
    (if (= d 1)
      (wo49base (car l))
      (+ (* (expt 8 (- d 1)) (wo49base (- (car l) 1)))
        (if (or (= (car l) 4) (= (car l) 9))
          0
          (wo49 (cdr l) (- d 1)))))))

; 0から9までで4と9を含まない数の個数
(define wo49base
  (lambda (n)
    (cond ((< 8 n) (- n 1))
          ((< n 4) (+ n 1))
          (else n))))

; 数値の桁数
(define digits
  (lambda (n)
    (string-length (number->string n))))

; 数値を桁ごとのリストに変換
(define number->numberlist
  (lambda (n)
    (map (lambda (c) (- (char->integer c) (char->integer #\0)))
      (string->list (number->string n)))))

; 最終的な答えを計算
(define ans
  (lambda (A B)
    (- (- (+ B 1) (wo49 (number->numberlist B) (digits B)))
      (- A (wo49 (number->numberlist (- A 1)) (digits (- A 1)))))))
    
(define A (read))
(define B (read))
(display (ans A B))
(display "\n")
