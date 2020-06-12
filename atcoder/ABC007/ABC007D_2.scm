(define A (read))
(define B (read))

; 0からNまでで4と9を含まない数の個数
; ls:Nをリストにしたものの逆 n:下から数えた桁数
(define (wo49 ls n ans)
  (if (null? ls) ans
    (wo49 (cdr ls) (+ n 1)
      (+ (if (or (= (car ls) 4) (= (car ls) 9)) 0 ans)
         (* (expt 8 n) (wo49base (car ls)))))))

; 1桁の場合の、0からn-1までで4と9を含まない数の個数
(define (wo49base n)
  (if (< n 5) n (- n 1)))

; 数値を桁ごとのリストに変換
(define (number->numberlist n)
  (map (lambda (c) (- (char->integer c) (char->integer #\0)))
    (string->list (number->string n))))

; 最終的な答えを計算
(define (ans A B)
  (- (- (+ B 1) (wo49 (reverse (number->numberlist B)) 0 1))
    (- A (wo49 (reverse (number->numberlist (- A 1))) 0 1))))
    
(print (ans A B))
