Отчет по покрытию теста

| Name                  | Stmts | Miss | Cover | Missing |
|-----------------------|-------|------|-------|---------|
| list_analyzer.py      |  22   |  1   |  95%  |   61    |
| test_list_analyzer.py |  65   |  1   |  98%  |   139   |
| TOTAL                 |  87   |  2   |  98%  |         |

Отчет от pylint 

Module list_analyzer 
- list_analyzer.py:54:12: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
------------------------------------------------------------------
Module test_list_analyzer
- test_list_analyzer.py:122:0: C0301: Line too long (111/100) (line-too-long)
- test_list_analyzer.py:135:0: C0301: Line too long (111/100) (line-too-long)

------------------------------------------------------------------
Your code has been rated at 9.66/10 (previous run: 9.40/10, +0.25)
