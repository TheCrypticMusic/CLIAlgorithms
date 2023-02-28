from rich.console import Console
from rich.table import Table
from rich import box


console = Console()


def draw_binary_search_table(
    table_name, lowest_col_number, highest_col_number, row_data, index_of_target, mid
):
    table = Table(box=box.SIMPLE, title=table_name, show_footer=True)

    for index in range(lowest_col_number, highest_col_number + 1):

        if index == index_of_target:
            if mid == index_of_target:
                table.add_column("FOUND", style="blue")
            else:
                table.add_column("T", style="green")
        elif index == mid:
            table.add_column("M", style="cyan")
        elif index == lowest_col_number:
            table.add_column("L", style="yellow")
        elif index == highest_col_number:
            table.add_column("U", style="red")
        else:
            table.add_column()

    s_b_list = list(map(str, row_data))
    index = list(map(str, range(lowest_col_number, highest_col_number + 1)))
    table.add_row(*index)
    table.add_column()
    table.add_row(*s_b_list[lowest_col_number : highest_col_number + 1])

    console.print(table)


def draw_linear_search_table(table_name, row_data,current_number_index, target_index):
    table = Table(box=box.SIMPLE, title=table_name, show_footer=True)
    
    for index in range(current_number_index, len(row_data)):
        if index == target_index:
            table.add_column("TI", style="red")
        elif index == current_number_index:
            table.add_column("C", style="green")
        else:
            table.add_column()
        # if index == tar:
        #     if mid == index_of_target:
        #         table.add_column("FOUND", style="blue")
        #     else:
        #         table.add_column("T", style="green")
        # elif index == mid:
        #     table.add_column("M", style="cyan")
        # elif index == lowest_col_number:
        #     table.add_column("L", style="yellow")
        # elif index == highest_col_number:
        #     table.add_column("U", style="red")
        # else:
        #     table.add_column()

    s_b_list = list(map(str, row_data))
    index = list(map(str, range(current_number_index, len(row_data))))
    table.add_row(*index)
    table.add_column()
    table.add_row(*s_b_list[current_number_index : len(row_data)])

    console.print(table)

def draw_table_key(**caption_fields):
    for fields in caption_fields.values():
        print(fields)


def to_list(user_input: str) -> list:
    str_list = user_input.split(" ")
    ordered_list = list(map(int, str_list))
    return ordered_list
