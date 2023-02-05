from rich.console import Console
from rich.table import Table


console = Console()

def draw_binary_search_table(table_name, lowest_col_number,  highest_col_number, row_data, index_of_target, mid):
    table = Table(title=table_name)
   
    
    for index in range(lowest_col_number, highest_col_number + 1):
        if (index == index_of_target):
            table.add_column(f"{index}", style="magenta")
        elif (index == mid):
            table.add_column(f"{index}", style="blink bold red underline on white")
        else:
            table.add_column(f"{index}")
        
    
    s_b_list = list(map(str, row_data))  
    table.add_row(*s_b_list[lowest_col_number:highest_col_number + 1])
    print(f"{table_name}\nLower Bound: {lowest_col_number}\nHigher Bound: {highest_col_number}\nIndex of Target: {index_of_target}\nMid Point: {mid}")

    console.print(table)