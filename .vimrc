set relativenumber 
set nowrap

syntax enable
filetype plugin indent on

autocmd BufNewFile,BufRead *.rs set filetype=rust

call plug#begin()
Plug 'tpope/vim-sensible'
Plug 'morhetz/gruvbox'
Plug 'jalvesaq/nvim-r'
Plug 'rust-lang/rust.vim'
Plug 'dense-analysis/ale'
call plug#end()

let g:LanguageClient_serverCommands = {
\ 'rust': ['rust-analyzer'],
\ }

let g:ale_linters = {'rust': ['analyzer']}

let g:ale_fixers = { 'rust': ['rustfmt', 'trim_whitespace', 'remove_trailing_lines'] }

" Optional, configure as-you-type completions
set completeopt=menu,menuone,preview,noselect,noinsert
let g:ale_completion_enabled = 1

nnoremap <C-LeftMouse> :ALEGoToDefinition<CR>
