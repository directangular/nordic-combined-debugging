(defun demo2-run ()
  (interactive)
  (let ((compilation-buffer-name-function (lambda (mode)
                                            (format "*demo2-run*"))))
    (compile (format "cd %s && ./run.sh"
                     (file-name-directory buffer-file-name)))))
