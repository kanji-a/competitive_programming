(use util.queue)
; 入力
(define R (read))
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

; キューの準備
(define q (make-queue))
; 座標と距離のペアをキューで扱う
(enqueue! q (cons (cons (- sy 1) (- sx 1)) 0))

; 解答の計算
(let solve ()
  (let* ((top (dequeue! q)) (x (car (car top))) (y (cdr (car top)))
    (xp (+ x 1)) (xm (- x 1)) (yp (+ y 1)) (ym (- y 1))
    (d (cdr top)))
    (if (and (= x (- gx 1)) (= y (- gy 1)))
      (begin (display d) (display "\n"))
      ; 近傍マスの距離確定とエンキュー
      (begin
        ; 右のマス
        (if (char=? (vector-ref (vector-ref c y) xp) #\.)
          (begin (vector-set! (vector-ref c y) xp #\#)
            (enqueue! q (cons (cons xp y) (+ d 1)))))
        ; 下のマス
        (if (char=? (vector-ref (vector-ref c yp) x) #\.)
          (begin (vector-set! (vector-ref c yp) x #\#)
            (enqueue! q (cons (cons x yp) (+ d 1)))))
        ; 左のマス
        (if (char=? (vector-ref (vector-ref c y) xm) #\.)
          (begin (vector-set! (vector-ref c y) xm #\#)
            (enqueue! q (cons (cons xm y) (+ d 1)))))
        ; 上のマス
        (if (char=? (vector-ref (vector-ref c ym) x) #\.)
          (begin (vector-set! (vector-ref c ym) x #\#)
            (enqueue! q (cons (cons x ym) (+ d 1)))))
        (solve)))))
