# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# define timeout (milliseconds) for multipurpose_modmap
define_timeout(1000)

# define timeout for simyltaneous key press detection
define_simultaneous_key_timeout(250)

'''
define_simultaneous_keymap('org.fcitx.Fcitx', re.compile('mozc'), {
    (Key.J, Key.D)          : [Key.A], # あ
    (Key.K)                 : [Key.I], # い
    (Key.J)                 : [Key.U], # う
    (Key.D, Key.SEMICOLON)  : [Key.E], # え
    (Key.D, Key.L)          : [Key.O], # お

    (Key.D)                 : [Key.K, Key.A], # か
    (Key.C)                 : [Key.K, Key.I], # き
    (Key.H)                 : [Key.K, Key.U], # く
    (Key.L, Key.E)          : [Key.K, Key.E], # け
    (Key.I)                 : [Key.K, Key.O], # こ

    (Key.S, Key.L)          : [Key.S, Key.A], # さ
    (Key.L)                 : [Key.S, Key.I], # し
    (Key.Z)                 : [Key.S, Key.U], # す
    (Key.D, Key.N)          : [Key.S, Key.E], # せ
    (Key.S, Key.SEMICOLON)  : [Key.S, Key.O],  # そ

    (Key.M)                 : [Key.T, Key.A], # た
    (Key.T)                 : [Key.T, Key.I], # ち
    (Key.B)                 : [Key.T, Key.U], # つ
    (Key.N)                 : [Key.T, Key.E], # て
    (Key.S)                 : [Key.T, Key.O], # と

    (Key.SEMICOLON)         : [Key.N, Key.A], # 
    (Key.W)                 : [Key.N, Key.I], # 
    (Key.L, Key.B)          : [Key.N, Key.U], # 
    (Key.D, Key.M)          : [Key.N, Key.E], # 
    (Key.A)                 : [Key.N, Key.O], # 

    (Key.E)                 : [Key.H, Key.A], # は
    (Key.P)                 : [Key.H, Key.I], # ひ
    (Key.K, Key.E)          : [Key.H, Key.U], # ふ
    (Key.D, Key.H)          : [Key.H, Key.E], # へ
    (Key.K, Key.A)          : [Key.H, Key.O], # ほ

    (Key.X)                 : [Key.M, Key.A], # ま
    (Key.D, Key.O)          : [Key.M, Key.I], # み
    (Key.K, Key.V)          : [Key.M, Key.U], # む
    (Key.L, Key.W)          : [Key.M, Key.E], # め
    (Key.K, Key.F)          : [Key.M, Key.O], # も

    (Key.S, Key.O)          : [Key.Y, Key.A], # や
    (Key.K, Key.G)          : [Key.Y, Key.U], # ゆ
    (Key.D, Key.I)          : [Key.Y, Key.O], # よ

    (Key.S, Key.J)          : [Key.R, Key.A], # ら
    (Key.L, Key.F)          : [Key.R, Key.I], # り
    (Key.V)                 : [Key.R, Key.U], # る
    (Key.K, Key.D)          : [Key.R, Key.E], # れ
    (Key.L, Key.V)          : [Key.R, Key.O], # ろ

    (Key.S, Key.N)          : [Key.W, Key.A], # わ
    (Key.L, Key.A)          : [Key.W, Key.O], # を
    (Key.F)                 : [Key.N, Key.N], # ん

# punctuations

    (Key.Q)                 : [Key.MINUS], # ー
    (Key.R)                 : [Key.COMMA], # 、
    (Key.DOT)               : [Key.DOT], # 。
    (Key.F, Key.V)          : [Key.LEFT_SHIFT, Key.KEY_1], # !
    (Key.N, Key.J)          : [Key.LEFT_SHIFT, Key.SLASH], # ?

# functional

# dakuonn

    (Key.O)                 : [Key.G, Key.A], # が
    (Key.L, Key.C)          : [Key.G, Key.I], # ぎ
    (Key.Y)                 : [Key.G, Key.U], # ぐ
    (Key.O, Key.P)          : [Key.G, Key.E], # げ  ## this is specific to ANSI US
    (Key.K, Key.W)          : [Key.G, Key.O], # ご

    (Key.L, Key.X)          : [Key.Z, Key.A], # ざ
    (Key.S, Key.K)          : [Key.Z, Key.I], # じ
    (Key.L, Key.G)          : [Key.Z, Key.U], # ず
    (Key.L, Key.Z)          : [Key.Z, Key.E], # ぜ
    (Key.K, Key.X)          : [Key.Z, Key.O], # ぞ

    (Key.S, Key.M)          : [Key.D, Key.A], # だ
    (Key.L, Key.Q)          : [Key.D, Key.I], # ぢ
    (Key.K, Key.Z)          : [Key.D, Key.U], # づ
    (Key.COMMA)             : [Key.D, Key.E], # で
    (Key.S, Key.I)          : [Key.D, Key.O], # ど

    (Key.U)                 : [Key.B, Key.A], # ば
    (Key.S, Key.H)          : [Key.B, Key.I], # び
    (Key.SLASH)             : [Key.B, Key.U], # ぶ
    (Key.D, Key.COMMA)      : [Key.B, Key.E], # べ
    (Key.K, Key.C)          : [Key.B, Key.O], # ぼ

    (Key.D, Key.U)          : [Key.P, Key.A], # ぱ
    (Key.S, Key.COMMA)      : [Key.P, Key.I], # ぴ
    (Key.D, Key.DOT)        : [Key.P, Key.U], # ぷ
    (Key.S, Key.U)          : [Key.P, Key.E], # ぺ
    (Key.S, Key.DOT)        : [Key.P, Key.O], # ぽ

    (Key.I, Key.V)          : [Key.K, Key.Y, Key.A], # きゃ
    (Key.I, Key.R)          : [Key.K, Key.Y, Key.U], # きゅ
    (Key.I, Key.F)          : [Key.K, Key.Y, Key.O], # きょ

    (Key.O, Key.V)          : [Key.G, Key.Y, Key.A], # ぎゃ
    (Key.O, Key.R)          : [Key.G, Key.Y, Key.U], # ぎゅ
    (Key.O, Key.F)          : [Key.G, Key.Y, Key.O], # ぎょ

    (Key.I, Key.C)          : [Key.S, Key.Y, Key.A], # しゃ
    (Key.I, Key.W)          : [Key.S, Key.Y, Key.U], # しゅ
    (Key.I, Key.E)          : [Key.S, Key.Y, Key.O], # しょ

    (Key.O, Key.C)          : [Key.D, Key.Y, Key.A], # ぢゃ
    (Key.O, Key.W)          : [Key.D, Key.Y, Key.U], # ぢゅ
    (Key.O, Key.E)          : [Key.D, Key.Y, Key.O], # ぢょ

    (Key.I, Key.B)          : [Key.C, Key.Y, Key.A], # ちゃ
    (Key.I, Key.T)          : [Key.C, Key.Y, Key.U], # ちゅ
    (Key.I, Key.G)          : [Key.C, Key.Y, Key.O], # ちょ

    (Key.O, Key.B)          : [Key.N, Key.Y, Key.A], # にゃ
    (Key.O, Key.T)          : [Key.N, Key.Y, Key.U], # にゅ
    (Key.O, Key.G)          : [Key.N, Key.Y, Key.O], # にょ

    (Key.I, Key.Z)          : [Key.H, Key.Y, Key.A], # ひゃ
    (Key.I, Key.Q)          : [Key.H, Key.Y, Key.U], # ひゅ
    (Key.I, Key.A)          : [Key.H, Key.Y, Key.O], # ひょ

    (Key.I, Key.KEY_2)      : [Key.B, Key.Y, Key.A], # びゃ
    (Key.I, Key.KEY_3)      : [Key.B, Key.Y, Key.U], # びゅ
    (Key.I, Key.KEY_4)      : [Key.B, Key.Y, Key.O], # びょ

    (Key.O, Key.KEY_2)      : [Key.P, Key.Y, Key.A], # ぴゃ
    (Key.O, Key.KEY_3)      : [Key.P, Key.Y, Key.U], # ぴゅ
    (Key.O, Key.KEY_4)      : [Key.P, Key.Y, Key.O], # ぴょ

    (Key.D, Key.SLASH)      : [Key.V, Key.U], # ゔ

    (Key.L, Key.KEY_2)      : [Key.M, Key.Y, Key.A], # みゃ
    (Key.L, Key.KEY_3)      : [Key.M, Key.Y, Key.U], # みゅ
    (Key.L, Key.KEY_4)      : [Key.M, Key.Y, Key.O], # みょ

    (Key.O, Key.Z)          : [Key.R, Key.Y, Key.A], # りゃ
    (Key.O, Key.Q)          : [Key.R, Key.Y, Key.U], # りゅ
    (Key.O, Key.A)          : [Key.R, Key.Y, Key.O], # りょ

    (Key.L, Key.KEY_1)      : [Key.X, Key.Y, Key.A], # ゃ
    (Key.I, Key.KEY_1)      : [Key.X, Key.Y, Key.U], # ゅ
    (Key.O, Key.KEY_1)      : [Key.X, Key.Y, Key.O], # ょ


# dakuonn
    (Key.O): [Key.G, Key.A],

}, 'shingeta')
'''


# [Global modemap] Change modifier keys as in xmodmap
define_modmap({
    Key.CAPSLOCK: Key.LEFT_CTRL
})

# [Conditional modmap] Change modifier keys in certain applications
define_conditional_modmap(re.compile(r'Emacs'), {
    Key.RIGHT_CTRL: Key.ESC,
})

# [Multipurpose modmap] Give a key two meanings. A normal key when pressed and
# released, and a modifier key when held down with another key. See Xcape,
# Carabiner and caps2esc for ideas and concept.
#define_multipurpose_modmap(
    # Enter is enter when pressed and released. Control when held down.
    #{Key.ENTER: [Key.ENTER, Key.RIGHT_CTRL]}

    # Capslock is escape when pressed and released. Control when held down.
    # {Key.CAPSLOCK: [Key.ESC, Key.LEFT_CTRL]
    # To use this example, you can't remap capslock with define_modmap.
#)

# [Conditional multipurpose modmap] Multipurpose modmap in certain conditions,
# such as for a particular device.
define_conditional_multipurpose_modmap(lambda wm_class, device_name: device_name.startswith("Microsoft"), {
   # Left shift is open paren when pressed and released.
   # Left shift when held down.
   Key.LEFT_SHIFT: [Key.KPLEFTPAREN, Key.LEFT_SHIFT],

   # Right shift is close paren when pressed and released.
   # Right shift when held down.
   Key.RIGHT_SHIFT: [Key.KPRIGHTPAREN, Key.RIGHT_SHIFT]
})

#define_per_im_keymap(re.compile('mozc'),{
#    K()
#}, "ja-JP specific mappings")

# Keybindings for Firefox/Chrome
define_keymap(re.compile("Firefox|Google-chrome"), {
    # Ctrl+Alt+j/k to switch next/previous tab
    K("C-M-j"): K("C-TAB"),
    K("C-M-k"): K("C-Shift-TAB"),
    # Type C-j to focus to the content
    K("C-j"): K("C-f6"),

    # type forward-slash to invoke in-page search
    #K('/'): K('^C-f'),

    # very naive "Edit in editor" feature (just an example)
    #K("C-o"): [K("C-a"), K("C-c"), launch(["gedit"]), sleep(0.5), K("C-v")]
}, "Firefox and Chrome")

# Keybindings for Zeal https://github.com/zealdocs/zeal/
define_keymap(re.compile("Zeal"), {
    # Ctrl+s to focus search area
    K("C-s"): K("C-k"),
}, "Zeal")

# Emacs-like keybindings in non-Emacs applications
define_keymap(lambda wm_class: wm_class not in ("Emacs", "URxvt", "Terminator", "Terminal", "Gnome-terminal"), {
    # Cursor
    K("C-b"): with_mark(K("left")),
    K("C-f"): with_mark(K("right")),
    K("C-p"): with_mark(K("up")),
    K("C-n"): with_mark(K("down")),
    K("C-h"): with_mark(K("backspace")),
    # Forward/Backward word
    K("M-b"): with_mark(K("C-left")),
    K("M-f"): with_mark(K("C-right")),
    # Beginning/End of line
    K("C-a"): with_mark(K("home")),
    K("C-e"): with_mark(K("end")),
    # Page up/down
    K("M-v"): with_mark(K("page_up")),
    K("C-v"): with_mark(K("page_down")),
    # Beginning/End of file
    K("M-Shift-comma"): with_mark(K("C-home")),
    K("M-Shift-dot"): with_mark(K("C-end")),
    # Newline
    K("C-m"): K("enter"),
    K("C-j"): K("enter"),
    K("C-o"): [K("enter"), K("left")],
    # Copy
    K("C-w"): [K("C-x"), set_mark(False)],
    K("M-w"): [K("C-c"), set_mark(False)],
    K("C-y"): [K("C-v"), set_mark(False)],
    # Delete
    K("C-d"): [K("delete"), set_mark(False)],
    K("M-d"): [K("C-delete"), set_mark(False)],
    # Kill line
    K("C-k"): [K("Shift-end"), K("C-x"), set_mark(False)],
    # Undo
    K("C-slash"): [K("C-z"), set_mark(False)],
    K("C-Shift-ro"): K("C-z"),
    # Mark
    K("C-space"): set_mark(True),
    K("C-M-space"): with_or_set_mark(K("C-right")),
    # Search
    K("C-s"): K("F3"),
    K("C-r"): K("Shift-F3"),
    K("M-Shift-key_5"): K("C-h"),
    # Cancel
    K("C-g"): [K("esc"), set_mark(False)],
    # Escape
    K("C-q"): escape_next_key,
    # C-x YYY
    K("C-x"): {
        # C-x h (select all)
        K("h"): [K("C-home"), K("C-a"), set_mark(True)],
        # C-x C-f (open)
        K("C-f"): K("C-o"),
        # C-x C-s (save)
        K("C-s"): K("C-s"),
        # C-x k (kill tab)
        K("k"): K("C-f4"),
        # C-x C-c (exit)
        K("C-c"): K("C-q"),
        # cancel
        K("C-g"): pass_through_key,
        # C-x u (undo)
        K("u"): [K("C-z"), set_mark(False)],
    }
}, "Emacs-like keys")
