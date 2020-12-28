# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# define timeout for simyltaneous key press detection
define_simultaneous_key_timeout(50)

# Specify the key to disable simultaneous layout
# you will need to specify the original key name, even if this was re-mapped to something else
define_simultaneous_toggle_key(Key.RIGHT_ALT)
define_keymap(None, 
    {K("C-RIGHT_BRACE"): enable_simul_switch},
    "simul_layout_enable")
define_keymap(None, 
    {K("C-LEFT_BRACE"): disable_simul_switch},
    "simul_layout_enable")

#define_simultaneous_keymap('org.fcitx.Fcitx', re.compile('mozc'), {
define_simultaneous_keymap({
    # Without shifts..
    (Key.Q)         : [Key.MINUS], # ー
    (Key.W)         : [Key.N, Key.I], # に
    (Key.E)         : [Key.H, Key.A], # は
    (Key.R)         : [Key.COMMA], # 、
    (Key.T)         : [Key.T, Key.I], # ち
    (Key.Y)         : [Key.G, Key.U], # ぐ
    (Key.U)         : [Key.B, Key.A], # ば
    (Key.I)         : [Key.K, Key.O], # こ
    (Key.O)         : [Key.G, Key.A], # が
    (Key.P)         : [Key.H, Key.I], # ひ
    (Key.O, Key.P)  : [Key.G, Key.E], # げ  ## this is specific to ANSI US
    (Key.A)         : [Key.N, Key.O], # の
    (Key.S)         : [Key.T, Key.O], # と
    (Key.D)         : [Key.K, Key.A], # か
    (Key.F)         : [Key.N, Key.N], # ん
    (Key.G)         : [Key.L, Key.T, Key.U], # っ
    (Key.H)         : [Key.K, Key.U], # く
    (Key.J)         : [Key.U], # う
    (Key.K)         : [Key.I], # い
    (Key.L)         : [Key.S, Key.I], # し
    (Key.SEMICOLON) : [Key.N, Key.A], # な
    (Key.Z)         : [Key.S, Key.U], # す
    (Key.X)         : [Key.M, Key.A], # ま
    (Key.C)         : [Key.K, Key.I], # き
    (Key.V)         : [Key.R, Key.U], # る
    (Key.B)         : [Key.T, Key.U], # つ
    (Key.N)         : [Key.T, Key.E], # て
    (Key.M)         : [Key.T, Key.A], # た
    (Key.COMMA)     : [Key.D, Key.E], # で
    (Key.DOT)       : [Key.DOT], # 。
    (Key.SLASH)     : [Key.B, Key.U], # ぶ

    # Cross-over Shifts..
    (Key.D, Key.K)  : [Key.R, Key.E], # れ 
    (Key.D, Key.L)  : [Key.O], # お
    (Key.S, Key.L)  : [Key.S, Key.A], # さ
    (Key.S, Key.K)  : [Key.Z, Key.I], # じ

    # With Left-Middle Shift..
    (Key.D, Key.Y)          : [Key.W, Key.I], # うぃ
    (Key.D, Key.U)          : [Key.P, Key.A], # ぱ
    (Key.D, Key.I)          : [Key.Y, Key.O], # よ
    (Key.D, Key.O)          : [Key.M, Key.I], # み
    (Key.D, Key.P)          : [Key.W, Key.E], # うぇ
    (Key.D, Key.H)          : [Key.H, Key.E], # へ
    (Key.D, Key.J)          : [Key.A], # あ
    #(Key.D, Key.K)          : [Key.R, Key.E], # れ
    #(Key.D, Key.L)          : [Key.O], # お
    (Key.D, Key.SEMICOLON)  : [Key.E], # え
    (Key.D, Key.N)          : [Key.S, Key.E], # せ
    (Key.D, Key.M)          : [Key.N, Key.E], # ね
    (Key.D, Key.COMMA)      : [Key.B, Key.E], # べ
    (Key.D, Key.DOT)        : [Key.P, Key.U], # ぷ
    (Key.D, Key.SLASH)      : [Key.V, Key.U], # ゔ

    # With Right-Middle Shift..
    (Key.K, Key.KEY_1)      : [Key.X, Key.A], # ぁ
    (Key.K, Key.KEY_2)      : [Key.X, Key.I], # ぃ
    (Key.K, Key.KEY_3)      : [Key.X, Key.U], # ぅ
    (Key.K, Key.KEY_4)      : [Key.X, Key.E], # ぇ
    (Key.K, Key.KEY_5)      : [Key.X, Key.O], # ぉ
    (Key.K, Key.Q)          : [Key.F, Key.A], # ふぁ
    (Key.K, Key.W)          : [Key.G, Key.O], # ご
    (Key.K, Key.E)          : [Key.H, Key.U], # ふ
    (Key.K, Key.R)          : [Key.F, Key.I], # ふぃ
    (Key.K, Key.T)          : [Key.F, Key.E], # ふぇ
    (Key.K, Key.A)          : [Key.H, Key.O], # ほ
    #(Key.K, Key.S)          : [Key.Z, Key.I], # じ
    #(Key.K, Key.D)          : [Key.R, Key.E], # れ
    (Key.K, Key.F)          : [Key.M, Key.O], # も
    (Key.K, Key.G)          : [Key.Y, Key.U], # ゆ
    (Key.K, Key.Z)          : [Key.D, Key.U], # づ
    (Key.K, Key.X)          : [Key.Z, Key.O], # ぞ
    (Key.K, Key.C)          : [Key.B, Key.O], # ぼ
    (Key.K, Key.V)          : [Key.M, Key.U], # む
    (Key.K, Key.B)          : [Key.F, Key.O], # ふぉ

    # With Left-Ring Shift..
    (Key.S, Key.Y)          : [Key.S, Key.H, Key.E], # しぇ
    (Key.S, Key.U)          : [Key.P, Key.E], # ぺ
    (Key.S, Key.I)          : [Key.D, Key.O], # ど
    (Key.S, Key.O)          : [Key.Y, Key.A], # や
    (Key.S, Key.P)          : [Key.J, Key.E], # じぇ
    (Key.S, Key.H)          : [Key.B, Key.I], # び
    (Key.S, Key.J)          : [Key.R, Key.A], # ら
    #(Key.S, Key.K)          : [Key.Z, Key.I], # じ
    #(Key.S, Key.L)          : [Key.S, Key.A], # さ
    (Key.S, Key.SEMICOLON)  : [Key.S, Key.O],  # そ
    (Key.S, Key.N)          : [Key.W, Key.A], # わ
    (Key.S, Key.M)          : [Key.D, Key.A], # だ
    (Key.S, Key.COMMA)      : [Key.P, Key.I], # ぴ
    (Key.S, Key.DOT)        : [Key.P, Key.O], # ぽ
    (Key.S, Key.SLASH)      : [Key.C, Key.H, Key.E], # ちぇ

    # With Right-Ring Shift..
    (Key.L, Key.KEY_1)      : [Key.X, Key.Y, Key.A], # ゃ
    (Key.L, Key.KEY_2)      : [Key.M, Key.Y, Key.A], # みゃ
    (Key.L, Key.KEY_3)      : [Key.M, Key.Y, Key.U], # みゅ
    (Key.L, Key.KEY_4)      : [Key.M, Key.Y, Key.O], # みょ
    (Key.L, Key.KEY_5)      : [Key.X, Key.W, Key.A], # ゎ
    (Key.L, Key.Q)          : [Key.D, Key.I], # ぢ
    (Key.L, Key.W)          : [Key.M, Key.E], # め
    (Key.L, Key.E)          : [Key.K, Key.E], # け
    (Key.L, Key.R)          : [Key.T, Key.H, Key.I], # てぃ
    (Key.L, Key.T)          : [Key.D, Key.H, Key.I], # でぃ
    (Key.L, Key.A)          : [Key.W, Key.O], # を
    #(Key.L, Key.S)          : [Key.S, Key.A], # さ
    #(Key.L, Key.D)          : [Key.O], # お
    (Key.L, Key.F)          : [Key.R, Key.I], # り
    (Key.L, Key.G)          : [Key.Z, Key.U], # ず
    (Key.L, Key.Z)          : [Key.Z, Key.E], # ぜ
    (Key.L, Key.X)          : [Key.Z, Key.A], # ざ
    (Key.L, Key.C)          : [Key.G, Key.I], # ぎ
    (Key.L, Key.V)          : [Key.R, Key.O], # ろ
    (Key.L, Key.B)          : [Key.N, Key.U], # ぬ

    # [Han]Dakuonn ([半]濁音) -- With O Shift
    (Key.O, Key.KEY_1)      : [Key.X, Key.Y, Key.A], # ゃ
    (Key.O, Key.KEY_2)      : [Key.P, Key.Y, Key.A], # ぴゃ
    (Key.O, Key.KEY_3)      : [Key.P, Key.Y, Key.U], # ぴゅ
    (Key.O, Key.KEY_4)      : [Key.P, Key.Y, Key.O], # ぴょ
    (Key.O, Key.Q)          : [Key.R, Key.Y, Key.U], # りゅ
    (Key.O, Key.W)          : [Key.J, Key.U], # じゅ
    (Key.O, Key.E)          : [Key.J, Key.O], # じょ
    (Key.O, Key.R)          : [Key.G, Key.Y, Key.U], # ぎゅ
    (Key.O, Key.T)          : [Key.N, Key.Y, Key.U], # にゅ
    (Key.O, Key.A)          : [Key.R, Key.Y, Key.O], # りょ
    (Key.O, Key.F)          : [Key.G, Key.Y, Key.O], # ぎょ
    (Key.O, Key.G)          : [Key.N, Key.Y, Key.O], # にょ
    (Key.O, Key.Z)          : [Key.R, Key.Y, Key.A], # りゃ
    (Key.O, Key.C)          : [Key.J, Key.A], # じゃ
    (Key.O, Key.V)          : [Key.G, Key.Y, Key.A], # ぎゃ
    (Key.O, Key.B)          : [Key.N, Key.Y, Key.A], # にゃ

    # [Han]Dakuonn ([半]濁音) -- With I Shift
    (Key.I, Key.KEY_1)      : [Key.X, Key.Y, Key.U], # ゅ
    (Key.I, Key.KEY_2)      : [Key.B, Key.Y, Key.A], # びゃ
    (Key.I, Key.KEY_3)      : [Key.B, Key.Y, Key.U], # びゅ
    (Key.I, Key.KEY_4)      : [Key.B, Key.Y, Key.O], # びょ
    (Key.I, Key.Q)          : [Key.H, Key.Y, Key.U], # ひゅ
    (Key.I, Key.W)          : [Key.S, Key.Y, Key.U], # しゅ
    (Key.I, Key.E)          : [Key.S, Key.Y, Key.O], # しょ
    (Key.I, Key.R)          : [Key.K, Key.Y, Key.U], # きゅ
    (Key.I, Key.T)          : [Key.C, Key.H, Key.U], # ちゅ
    (Key.I, Key.A)          : [Key.H, Key.Y, Key.O], # ひょ
    (Key.I, Key.F)          : [Key.K, Key.Y, Key.O], # きょ
    (Key.I, Key.G)          : [Key.C, Key.H, Key.O], # ちょ
    (Key.I, Key.Z)          : [Key.H, Key.Y, Key.A], # ひゃ
    (Key.I, Key.C)          : [Key.S, Key.Y, Key.A], # しゃ
    (Key.I, Key.V)          : [Key.K, Key.Y, Key.A], # きゃ
    (Key.I, Key.B)          : [Key.C, Key.H, Key.A], # ちゃ

# remaining key augument
    (Key.A, Key.SEMICOLON)  : [Key.SEMICOLON],
    (Key.A, Key.SLASH)      : [Key.SLASH],
    (Key.Z, Key.J)          : [Key.Z, Key.L],
    (Key.Z, Key.H)          : [Key.Z, Key.K],
    (Key.Z, Key.N)          : [Key.Z, Key.H],
    (Key.Z, Key.M)          : [Key.Z, Key.J],
    (Key.Z, Key.SLASH)      : [Key.Z, Key.DOT],


}, 'shingeta')



'''
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

    (Key.SEMICOLON)         : [Key.N, Key.A], # な
    (Key.W)                 : [Key.N, Key.I], # に
    (Key.L, Key.B)          : [Key.N, Key.U], # ぬ
    (Key.D, Key.M)          : [Key.N, Key.E], # ね
    (Key.A)                 : [Key.N, Key.O], # の

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
    (Key.G)                 : [Key.L, Key.T, Key.U], # っ

# punctuations and funcitonal
    (Key.Q)                 : [Key.MINUS], # ー
    (Key.R)                 : [Key.COMMA], # 、
    (Key.DOT)               : [Key.DOT], # 。
    (Key.F, Key.V)          : [Key.LEFT_SHIFT, Key.KEY_1], # !
    (Key.N, Key.J)          : [Key.LEFT_SHIFT, Key.SLASH], # ?
    (Key.F, Key.G)          : [Key.LEFT_BRACE, Key.RIGHT_BRACE, Key.ENTER, Key.LEFT], # 

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

# remaining key augument
    (Key.A, Key.SEMICOLON)  : [Key.SEMICOLON],
    (Key.A, Key.SLASH)      : [Key.SLASH],
    (Key.Z, Key.J)          : [Key.Z, Key.L],
    (Key.Z, Key.H)          : [Key.Z, Key.K],
    (Key.Z, Key.N)          : [Key.Z, Key.H],
    (Key.Z, Key.M)          : [Key.Z, Key.J],
    (Key.Z, Key.SLASH)      : [Key.Z, Key.DOT],


'''
