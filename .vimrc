call plug#begin()

Plug 'tpope/vim-sensible'
Plug 'morhetz/gruvbox'

Plug 'preservim/nerdtree'

call plug#end()

autocmd vimenter * ++nested colorscheme gruvbox
set bg=dark

set mouse=a
set relativenumber
set nowrap

set tabstop=4
set shiftwidth=4
set expandtab

let g:NERDTreeWinSize=10

" Start NERDTree when Vim is started without file arguments.
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists('s:std_in') | NERDTree | endif
" Exit Vim if NERDTree is the only window remaining in the only tab.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | call feedkeys(":quit\<CR>:\<BS>") | endif
