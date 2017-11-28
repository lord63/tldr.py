function _tldr_autocomplete {
    commands=$(tldr list)
    COMPREPLY=()
    if [ $COMP_CWORD = 2 ]; then
        COMPREPLY=(`compgen -W "$commands" -- $2`)
    fi
}

complete -F _tldr_autocomplete tldr
