alias python='python3'
alias c='clear'
alias v='vim'
alias lla="ls -la"
alias la="lla | awk '{print \$1,\$2,\$9}'"
alias bp='vim ~/.bash_profile'
alias s='source ~/.bash_profile'
alias gs='git status'
alias gd='git diff'
alias ga='git add --all'
alias gc='git commit'
alias gp='git push origin master'
alias bc='cp ~/.bash_profile .'
alias p='python'
alias pi='pip3 install'
alias ki='pkg install'
function r(){ ./$@; }
