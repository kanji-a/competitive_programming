; /////////////////////////////////////////////
; N個の入力をlistに入れる
; /////////////////////////////////////////////
(define N (read))
(define ls (let loop ((n N))
  (if (zero? n)
    '() (cons (read) (loop (- n 1))))))

; /////////////////////////////////////////////
; 迷路の読み込み
; /////////////////////////////////////////////
; ベクタのベクタを使用
(define C (read))
(define sy (read))
(define sx (read))
(define gy (read))
(define gx (read))
; 残った改行文字の処理
(read-char)
; cの宣言
; cの要素をベクターにする
(define c (make-vector R))
(let loop-r ((raw 0))
  (if (< raw R)
    (begin
      (vector-set! c raw (make-vector C))
      (loop-r (+ raw 1)))))

; cに値をセット
(let loop-r ((raw 0))
  (if (< raw R)
    (begin
      (let loop-c ((col 0))
        (if (< col C)
          (begin
            (vector-set! (vector-ref c raw) col (read-char))
            (loop-c (+ col 1)))))
      (read-char)
      (loop-r (+ raw 1)))))

; /////////////////////////////////////////////
; にぶたん
; lは下限-1、uは上限+1
; /////////////////////////////////////////////
; 上界
(define (ub f n l u)
  (if (= (- u l) 1) (- u 1)
    (let ((m (quotient (+ l u) 2)))
      (if (<= (f m) n)
        (ub f n m u)
        (ub f n l m)))))

; 上界(ベクタ)
(define (vub f vec n l u)
  (if (= (- u l) 1) (- u 1)
    (let ((m (quotient (+ l u) 2)))
      (if (<= (f (vector-ref vec m)) n)
        (vub f vec n m u)
        (vub f vec n l m)))))

; 下界
(define (lb f n l u)
  (if (= (- u l) 1) u
    (let ((m (quotient (+ l u) 2)))
      (if (>= (f m) n)
        (lb f n l m)
        (lb f n m u)))))

; 下界(ベクタ)
(define (vlb f vec n l u)
  (if (= (- u l) 1) u
    (let ((m (quotient (+ l u) 2)))
      (if (>= (f (vector-ref vec m)) n)
        (vlb f vec n l m)
        (vlb f vec n m u)))))

; /////////////////////////////////////////////
; その他
; /////////////////////////////////////////////
; 等差数列の和
(define (sum-of-aseq a d n)
  (* (+ a (/ (* (- n 1) d) 2)) n))
