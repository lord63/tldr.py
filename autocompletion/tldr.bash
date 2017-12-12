_tldr_completion() {
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _TLDR_COMPLETE=complete $1 ) )

    if [ $COMP_CWORD = 2 ]; then
        command_name=${COMP_WORDS[COMP_CWORD-1]}
        if [[ "$command_name" == "find" ]] || [[ "$command_name" == "locate" ]]; then
            pages=$(tldr list)
            COMPREPLY=(`compgen -W "$pages" -- $2`)
        fi
    fi

    return 0
}

complete -F _tldr_completion -o default tldr;
