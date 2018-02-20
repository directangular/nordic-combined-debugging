(defun demo3-run ()
  (interactive)
  (let ((compilation-buffer-name-function (lambda (mode)
                                            (format "*demo3-run*"))))
    (compile (format "cd %s && ./run.sh"
                     (file-name-directory buffer-file-name)))))
