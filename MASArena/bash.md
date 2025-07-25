`BENCHMARK=${1:-math}`: 传入为空则默认math

`TRAIN_SIZE=${7:-}`: 传入为空则为空

`./run.sh [benchmark_name]...[train_size] [test_size]`: 不传入数据则用`""`占位

`if/else` 逻辑语法：
```bash
# `-n`: non-zero. Return true (0)
if [ -n "$OPTIMIZER" ]; then      
    echo "Optimizer: $OPTIMIZER"
elif [ -n "&PARAMETER" ]; then
    echo "algernon miao"
else
    echo "Agent System: $AGENT_SYSTEM"
fi
```

### kimi-k2
在 Bash 的测试命令（`[ ]`、`[[ ]]` 或 `test`）里，  
以 **减号开头** 的字母/符号叫 **“一元或二元测试运算符”**（test operators）。  
它们用来比较数字、判断字符串、检测文件/目录等。  

------------------------------------------------
1. 数字比较（binary）
------------------------------------------------
| 运算符 | 英文全称记忆 | 含义 | 示例 |
|---|---|---|---|
| `-eq` | **e**qual | 等于 | `[ $a -eq $b ]` |
| `-ne` | **n**ot **e**qual | 不等于 | `[ $a -ne $b ]` |
| `-lt` | **l**ess **t**han | 小于 | `[ $a -lt $b ]` |
| `-le` | **l**ess or **e**qual | 小于等于 | `[ $a -le $b ]` |
| `-gt` | **g**reater **t**han | 大于 | `[ $a -gt $b ]` |
| `-ge` | **g**reater or **e**qual | 大于等于 | `[ $a -ge $b ]` |

------------------------------------------------
2. 字符串比较
------------------------------------------------
| 运算符 | 含义 | 示例 |
|---|---|---|
| `=` 或 `==` | 两串相等 | `[ "$s1" = "$s2" ]` |
| `!=` | 两串不等 | `[ "$s1" != "$s2" ]` |
| `<` | 按字典序小于 | `[[ $s1 < $s2 ]]` |
| `>` | 按字典序大于 | `[[ $s1 > $s2 ]]` |

------------------------------------------------
3. 一元字符串/变量测试
------------------------------------------------
| 运算符 | 英文记忆 | 含义 | 示例 |
|---|---|---|---|
| `-z` | **z**ero | 长度是否为 0 | `[ -z "$s" ]` |
| `-n` | **n**on-zero | 长度是否 > 0 | `[ -n "$s" ]` |

------------------------------------------------
4. 文件/目录一元测试
------------------------------------------------
| 运算符 | 英文记忆 | 含义 | 示例 |
|---|---|---|---|
| `-e` | **e**xists | 文件/目录存在 | `[ -e path ]` |
| `-f` | **f**ile | 存在且是普通文件 | `[ -f file.txt ]` |
| `-d` | **d**irectory | 存在且是目录 | `[ -d /tmp ]` |
| `-L` / `-h` | **l**ink / **h**ard link | 存在且是符号链接 | `[ -L linkname ]` |
| `-r` | **r**eadable | 存在且可读 | `[ -r file ]` |
| `-w` | **w**ritable | 存在且可写 | `[ -w file ]` |
| `-x` | e**x**ecutable | 存在且可执行 | `[ -x script.sh ]` |
| `-s` | **s**ize | 存在且大小 > 0 | `[ -s file ]` |
| `-S` | **S**ocket | 存在且是 socket | `[ -S /dev/log ]` |

------------------------------------------------
5. 文件二元比较
------------------------------------------------
| 运算符 | 含义 | 示例 |
|---|---|---|
| `file1 -nt file2` | file1 比 file2 **n**ewer | `[ a -nt b ]` |
| `file1 -ot file2` | file1 比 file2 **o**lder | `[ a -ot b ]` |
| `file1 -ef file2` | 指向同一 **i-node**（硬链） | `[ a -ef b ]` |

------------------------------------------------
6. 逻辑组合
------------------------------------------------

现代推荐（`[[ ]]` 或外部命令）：
```bash
[[ -f file && -r file ]]
[[ -z $s || -z $t ]]
```