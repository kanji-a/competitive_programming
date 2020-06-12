; 入力受け取り
(define N (read))
(define bridge (let loop ((n (- N 1)))
  (if (zero? n) '()
     (cons (cons (read) (read)) (loop (- n 1))))))

; エッジ情報
(define graph (make-vector N))
(let loop ((n 0))
  (if (< n N)
    (begin (vector-set! graph n (list))
           (loop (+ n 1)))))
(let loop ((n 0) (ls bridge))
  (if (< n (- N 1))
    (begin (vector-set! graph (- (caar ls) 1) (append (vector-ref graph (- (caar ls) 1)) (list (- (cdar ls) 1))))
           (vector-set! graph (- (cdar ls) 1) (append (vector-ref graph (- (cdar ls) 1)) (list (- (caar ls) 1))))
           (loop (+ n 1) (cdr ls)))))

; エッジ情報を木に変換
(define (g2t parent current graph)
  (begin (vector-set! graph current (remove (^ (x) (= x parent)) (vector-ref graph current)))
         (let ((children (vector-ref graph current)))
           (if (not (null? #?=children))
             (map (^ (x) (g2t current x graph)) children)))))
(g2t -1 0 graph)
(print graph)

(define (f x)
  (+ (g x) (fold * (map g ()))))

(define (g x)
  (fold * (map f ())))

