# Demo 2: text editor integrations

## Emacs

Just eval the `demo2.el` buffer and run `M-x demo2-run`.  When you visit
http://localhost.localdomain:5000/ you should get a server error, as well
as a highlighted stack trace in your compilation buffer where the app is
running.

<small>
In this simple example app you could just use [File
Variables](https://www.gnu.org/software/emacs/manual/html_node/emacs/Specifying-File-Variables.html)
to set up a custom `compile-command`, but that technique doesn't scale
well, plus it might annoy your non-Emacs teammates.
</small>

## VS Code

TODO
